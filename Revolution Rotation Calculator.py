#!/usr/bin/env python3
import itertools
import math
import sqlite3
import sys
import time
from typing import List, Dict, Tuple

abilities: List[str] = []

# --- Defining how abilities work --- #

# Define cooldowns for cases where no abilities may be used
attack_speed_cooldowns: Dict[str, float] = {}

# Define ability damage for every ability
ability_damage: Dict[str, float] = {}

# Define the cooldown of abilities (in seconds)
ability_cooldown: Dict[str, float] = {}

# How long it takes to use each ability
ability_time: Dict[str, float] = {}

# Define the type of abilities (B = basic, T = threshold, U = ultimate)
ability_type: Dict[str, str] = {}

# Define a flag to decide if you can use abilities (based on adrenaline)
ability_ready: Dict[str, bool] = {}

# Define the time DOT abilities last (in seconds)
bleeds: Dict[str, float] = {}

# Define damage multiplier of walking bleeds
walking_bleeds: Dict[str, float] = {}

# Define bleed abilities that have their first hit affected by damage modifying abilities
special_bleeds: List[str] = []

# Define abilities that take longer than 1.8 seconds to use but will still have full impact from abilities in the
# crit_boost list
special_abilities: List[str] = []

# How long stuns, DPS increases .. etc last
buff_time: Dict[str, float] = {}

# Define the Multiplier for boosted damage
buff_effect: Dict[str, float] = {}

# Define crit-boosting abilities
crit_boost: List[str] = []

# Define the abilities that do extra damage when the target is stun or bound
punishing: List[str] = []

# Define abilities that can stun or bind the target
debilitating: List[str] = []

# Define abilities that bind the target
binds: List[str] = []

# Define area of effect abilities
aoe: List[str] = []

start_adrenaline: int
gain: int
attack_speed: str
activate_bleeds: bool
my_abilities: List[str]
auto_adrenaline: int
cycle_duration: float


def get_db_ability_data() -> None:
    global abilities, attack_speed_cooldowns, ability_damage, ability_cooldown, ability_time, ability_type, ability_ready, bleeds, walking_bleeds, special_bleeds, special_abilities, buff_time, buff_effect, crit_boost, punishing, debilitating, binds, aoe
    conn = sqlite3.connect("./db/revoDB.db")
    c = conn.cursor()
    user_abilities = "('" + "', '".join(my_abilities) + "')"

    for record in c.execute("SELECT * FROM Ability WHERE upper(Ability.Name) IN " + user_abilities):
        abilities.append(record[0])
        ability_damage[record[0]] = record[2]
        ability_cooldown[record[0]] = record[6]
        ability_time[record[0]] = record[5]
        ability_type[record[0]] = record[1]
        ability_ready[record[0]] = bool(record[3])

    for record in c.execute("SELECT * FROM AttackSpeedCooldown"):
        attack_speed_cooldowns[record[0]] = record[1]

    for record in c.execute("SELECT * FROM BleedingAbility WHERE upper(Name) IN " + user_abilities):
        bleeds[record[0]] = record[1]

    for record in c.execute("SELECT * FROM WalkingAbility WHERE upper(Name) IN " + user_abilities):
        walking_bleeds[record[0]] = record[1]

    for record in c.execute("SELECT * FROM SpecialBleedingAbility WHERE upper(Name) IN " + user_abilities):
        special_bleeds.append(record[0])

    for record in c.execute("SELECT * FROM SpecialAbility WHERE upper(Name) IN " + user_abilities):
        special_abilities.append(record[0])

    for record in c.execute("SELECT * FROM BuffTime WHERE upper(Name) IN " + user_abilities):
        buff_time[record[0]] = record[1]

    for record in c.execute("SELECT * FROM BuffEffect WHERE upper(Name) IN " + user_abilities):
        buff_effect[record[0]] = record[1]

    for record in c.execute("SELECT * FROM CritBoostAbility WHERE upper(Name) IN " + user_abilities):
        crit_boost.append(record[0])

    for record in c.execute("SELECT * FROM PunishingAbility WHERE upper(Name) IN " + user_abilities):
        punishing.append(record[0])

    for record in c.execute("SELECT * FROM DebilitatingAbility WHERE upper(Name) IN " + user_abilities):
        debilitating.append(record[0])

    for record in c.execute("SELECT * FROM BindingAbility WHERE upper(Name) IN " + user_abilities):
        binds.append(record[0])

    for record in c.execute("SELECT * FROM AoeAbility WHERE upper(Name) IN " + user_abilities):
        aoe.append(record[0])

    conn.close()


# Will return how much damage an ability bar will do over a given time
def ability_rotation(permutation: List[str]) -> float:
    # Will check if an auto attack is needed to be used
    def auto_available() -> bool:
        for ability in track_cooldown:
            if (ability_cooldown[ability] - track_cooldown[ability]) < attack_speed_cooldowns[attack_speed]:
                return False
        return True

    # Decreases Cooldowns of abilities and buffs as well as modifying and damage multipliers
    def adjust_cooldowns(current_buff: float, adrenaline: int, cooldown_time: float) -> float:
        for ability in track_cooldown:
            track_cooldown[ability] += cooldown_time
            track_cooldown[ability] = round(track_cooldown[ability], 1)
            if track_cooldown[ability] >= ability_cooldown[ability]:
                track_cooldown[ability] = 0
                if ability in threshold_ability_list:
                    if adrenaline >= 50:
                        ability_ready[ability] = True
                elif ability in ultimate_ability_list:
                    if adrenaline == 100:
                        ability_ready[ability] = True
                else:
                    ability_ready[ability] = True
        for ability in permutation:
            if ability in track_cooldown and track_cooldown[ability] == 0:
                del track_cooldown[ability]
        for ability in track_buff:
            track_buff[ability] += cooldown_time
            track_buff[ability] = round(track_buff[ability], 1)
            if track_buff[ability] >= buff_time[ability]:
                track_buff[ability] = 0
        for ability in permutation:
            if ability in track_buff and track_buff[ability] == 0:
                del track_buff[ability]
                if (ability not in punishing) and (ability in buff_effect):
                    current_buff = current_buff / buff_effect[ability]
        return current_buff

    # Determines if enemy vulnerable to extra damage due to stuns or binds
    def buff_available() -> bool:
        for ability in debilitating:
            if ability in track_buff:
                return True
        return False

    def modify_time(cycle_duration: float, time_elapsed: float, ability: str) -> float:
        if (ability in bleeds) and (ability != "Shadow Tendrils") and (
                    (cycle_duration - time_elapsed) < bleeds[ability]):
            return (cycle_duration - time_elapsed) / bleeds[ability]
        else:
            if (ability not in special_abilities) and (ability_time[ability] > 1.8) and (
                        (cycle_duration - time_elapsed) < ability_time[ability]):
                return (cycle_duration - time_elapsed) / ability_time[ability]
        return 1

    # --- Defining Variables --- #
    damage_dealt: float = 0
    current_buff: float = 1
    time_elapsed: float = 0
    shards: float = 0
    adrenaline = start_adrenaline
    # --- Calculations begin here --- #
    ability_path.append(f"AUTO D: {round(damage_dealt, 1)} T: {round(time_elapsed, 1)} A: {adrenaline}")
    damage_dealt += 50
    adrenaline += auto_adrenaline
    if adrenaline >= 100:
        adrenaline = 100
        for tracked_ability in ultimate_ability_list:
            ability_ready[tracked_ability] = True
        for tracked_ability in threshold_ability_list:
            ability_ready[tracked_ability] = True
    elif adrenaline >= 50:
        for tracked_ability in threshold_ability_list:
            ability_ready[tracked_ability] = True
    elif adrenaline < 0:
        adrenaline = 0
    time_elapsed += 0.6
    time_elapsed = round(time_elapsed, 1)
    while time_elapsed < cycle_duration:
        for ability in permutation:
            # Checks if ability can be used TODO: Check if this is necessary
            if time_elapsed < cycle_duration and ability_ready[ability] is True:
                ability_ready[ability] = False
                # --- Modifying adrenaline as required --- #
                ability_path.append(f"{ability} D: {round(damage_dealt, 1)} T: {round(time_elapsed, 1)}"
                                    f" A: {adrenaline}")
                if ability in basic_ability_list:
                    adrenaline += 8
                elif ability in threshold_ability_list:
                    adrenaline -= 15
                else:
                    adrenaline = gain
                if adrenaline > 100:
                    adrenaline = 100
                # --- Adding shards if they are used, or using them if activated --- #
                if ability == "Storm Shards":
                    if shards < 10:
                        shards += 1
                elif ability == "Shatter":
                    damage_dealt += round(shards * 85, 1)
                    shards = 0
                    # --- Calculating how much damage abilities should do --- #
                more_binds: bool = False
                altered_bleeds: bool = False
                modified_damage: bool = False
                damage_multiplier: float = 1  # Multiplier for damage due to damage boosting abilities
                bleed_multiplier: float = 1  # Multiplier in case target is bound (and bind about to run out)
                for tracked_ability in track_buff:
                    if tracked_ability in crit_boost:
                        if ((buff_time[tracked_ability] - track_buff[tracked_ability]) < ability_time[ability]) and (
                                    (ability not in special_abilities) and (ability_time[ability] > 1.8)):
                            damage_multiplier *= (
                                (((buff_time[tracked_ability] - track_buff[tracked_ability]) / ability_time[ability]) *
                                 (buff_effect[tracked_ability] - 1)) + 1)
                        else:
                            damage_multiplier *= buff_effect[tracked_ability]
                    elif (tracked_ability in binds) and (activate_bleeds is True) and (ability in walking_bleeds) and (
                                len(debilitating) > 0):
                        if (more_binds is False) and (
                                        buff_time[tracked_ability] - track_buff[tracked_ability] < bleeds[ability]):
                            bleed_multiplier = walking_bleeds[ability] * (
                                1 + (buff_time[tracked_ability] - track_buff[tracked_ability]) / bleeds[ability])
                        else:
                            bleed_multiplier = 1
                            more_binds = True
                        altered_bleeds = True
                if (activate_bleeds is True) and (ability in walking_bleeds) and (altered_bleeds is False):
                    bleed_multiplier = walking_bleeds[ability] * 2
                time_multiplier = modify_time(cycle_duration, time_elapsed, ability)
                if ability in bleeds:
                    if ability in special_bleeds:
                        if ability == "Smoke Tendrils":
                            damage_dealt += (ability_damage[ability] * damage_multiplier)
                        else:
                            ability_damage[ability] = ((112.8 * damage_multiplier) + 313.33)
                            modified_damage = True
                    damage_dealt += round(ability_damage[ability] * bleed_multiplier * time_multiplier, 1)
                    if modified_damage is True:
                        ability_damage[ability] = 426.13
                elif (ability in punishing) and (buff_available() is True):
                    damage_dealt += round(ability_damage[ability] * buff_effect[ability] * damage_multiplier *
                                          time_multiplier, 1)
                else:
                    damage_dealt += round(ability_damage[ability] * damage_multiplier * time_multiplier, 1)
                # --- Increasing rotation duration and managing cooldowns --- #
                time_elapsed += ability_time[ability]
                time_elapsed = round(time_elapsed, 1)
                track_cooldown[ability] = float(0)
                if ability in buff_time and ability not in punishing:
                    track_buff[ability] = 0
                    if ability in buff_effect:
                        current_buff = current_buff * buff_effect[ability]
                # Will also manage cooldowns
                current_buff = adjust_cooldowns(current_buff, adrenaline, ability_time[ability])
                break
        # --- Determines whether thresholds or ultimates may be used --- #
        if time_elapsed < cycle_duration:
            if adrenaline == 100:
                for tracked_ability in (a for a in ultimate_ability_list if a not in track_cooldown):
                    ability_ready[tracked_ability] = True
                for tracked_ability in (a for a in threshold_ability_list if a not in track_cooldown):
                    ability_ready[tracked_ability] = True
            elif adrenaline >= 50:
                for tracked_ability in (a for a in threshold_ability_list if a not in track_cooldown):
                    ability_ready[tracked_ability] = True
            elif adrenaline < 50:
                for tracked_ability in threshold_ability_list:
                    ability_ready[tracked_ability] = False
            if adrenaline != 100:
                for tracked_ability in ultimate_ability_list:
                    ability_ready[tracked_ability] = False
        # --- Determines if any abilities available/ whether auto attacks must be used --- #
        if time_elapsed < cycle_duration:
            ability_available = False
            for _ in (a for a in permutation if ability_ready[a]):
                ability_available = True
                break
            if ability_available is False:
                if auto_available() is True:
                    if (time_elapsed + attack_speed_cooldowns[attack_speed]) <= cycle_duration:
                        time_elapsed += attack_speed_cooldowns[attack_speed]
                    else:
                        time_elapsed += (cycle_duration - time_elapsed)
                        break
                    ability_path.append(f"AUTO D: {round(damage_dealt, 1)} T: {round(time_elapsed, 1)} A: {adrenaline}")
                    if float(cycle_duration - time_elapsed) >= 0.6:
                        damage_dealt += round(50 * current_buff, 1)
                    else:
                        damage_dealt += round(float(50 * round(float((cycle_duration - time_elapsed) / 0.6), 1)) *
                                              current_buff, 1)
                    adrenaline += auto_adrenaline
                    time_elapsed += 0.6
                    if adrenaline > 100:
                        adrenaline = 100
                    # Will also manage cooldowns
                    current_buff = adjust_cooldowns(current_buff, adrenaline, (attack_speed_cooldowns[attack_speed] +
                                                                               0.6))
                else:
                    time_elapsed += 0.6
                    current_buff = adjust_cooldowns(current_buff, adrenaline, 0.6)
                time_elapsed = round(time_elapsed, 1)
    return damage_dealt


def setup_config() -> None:
    global start_adrenaline, gain, attack_speed, activate_bleeds, debilitating, my_abilities, auto_adrenaline, cycle_duration

    def compare(lines) -> bool:
        # configuration followed by line number
        correct_data: Dict[str, int] = {"Adrenaline": 2, "Gain": 3, "AttackSpeed": 4, "Bleeds": 5, "Stuns": 6,
                                        "Abilities": 7, "Style": 8, "Time": 9, "units": 13}
        for setting in correct_data:
            if setting != lines[correct_data[setting]]:
                return False
        return True

    def validate(configurations) -> List[str]:
        error_log: List[str] = []
        empty_field: bool = False
        for config in configurations:
            if config == "":
                empty_field = True
        if empty_field is True:
            error_log.append("One or more settings have been left empty.")

        try:
            setting: int = int(configurations[0])
            if not (0 <= setting <= 100):
                error_log.append("Adrenaline must be between 0 and 100 inclusive.")
        except ValueError:
            error_log.append("Adrenaline must be an integer.")

        try:
            setting: int = int(configurations[1])
            if not (0 <= setting <= 100):
                error_log.append("Gain must be a positive integer between 0 and 100 inclusive.")
        except ValueError:
            error_log.append("Gain must be an integer.")

        if configurations[2].upper() not in ("SLOWEST", "SLOW", "AVERAGE", "FAST", "FASTEST"):
            error_log.append("AttackSpeed must either be one of the following options: ('slowest, slow, average, fast,"
                             " fastest').")

        setting: str = configurations[3]
        if not ((setting.lower() == "false") or (setting.lower() == "true")):
            error_log.append("Bleeds must be true or false.")

        setting: str = configurations[4]
        if not ((setting.lower() == "false") or (setting.lower() == "true")):
            error_log.append("Stuns must be true or false.")

        setting: str = configurations[5]
        if setting[0] == "[" and setting[-1] == "]":
            setting = setting[1:-1].split(",")
            counter: Dict[str, int] = {}
            if len(setting) > 0:
                for ability in setting:
                    ability = ability.upper().strip()
                    conn = sqlite3.connect("./db/revoDB.db")
                    c = conn.cursor()
                    c.execute("SELECT 1 FROM Ability WHERE upper(Ability.Name) = ?", (ability,))
                    if c.fetchone() is None and ability not in counter:
                        error_log.append(f"{ability.strip()} is not a recognised ability, or is not included in this "
                                         f"calculator.")
                        conn.close()
                    if ability in counter:
                        counter[ability] += 1
                        if counter[ability] == 2:
                            error_log.append(f"{(ability.strip())} is referenced 2 or more times within array. Ensure "
                                             f"it is only referenced once.")
                    else:
                        counter[ability] = 1
            else:
                error_log.append("No abilities were added")
        else:
            error_log.append("Abilities must be surrounded by square brackets [], and separated by comma's (,).")

        setting: str = configurations[6]
        if setting[0] == "(" and setting[-1] == ")":
            setting = setting[1:-1].split(",")
            if setting[0].upper() not in ("MAGIC", "RANGED", "MELEE"):
                error_log.append("First style option must be 'magic', 'ranged' or 'melee' (without quotes).")
            if setting[1] not in ("1", "2"):
                error_log.append("Second style option must be 1 or 2 (for 1 handed / 2 handed weapon)3")
        else:
            error_log.append("Style must start and end with round brackets (), with each option separated by a single "
                             "comma (,).")

        try:
            setting: float = float(configurations[7])
            if not (setting > 0):
                error_log.append("Time must be a number greater than zero.")
        except ValueError:
            error_log.append("Time must be a number.")

        if configurations[8].upper() not in ("SECONDS", "TICKS"):
            error_log.append("Units must be either 'seconds' or 'ticks' (without quotes).")

        return error_log

    def repair_config_file() -> None:
        repair: str = input("Configurations.txt has been modified, perform repair? (Y/N).\n>> ").upper()
        if (repair == "Y") or (repair == "YES"):
            import os
            correct_data: List[str] = ["# Rotation Parameters", "", "Adrenaline: ", "Gain: ", "AttackSpeed: ",
                                       "Bleeds: ", "Stuns: ", "Abilities: [,,,]", "Style: (,)", "Time: ", "", "# Mode",
                                       "", "units: seconds"]
            if os.path.exists("Configurations.txt"):
                os.remove("Configurations.txt")
            with open("Configurations.txt", "w") as settings:
                for line in correct_data:
                    settings.write(line + str("\n"))
            input("Repair successful! fill out settings in Configurations.txt before running calculator again. "
                  "Press enter to exit.\n>> ")
        sys.exit()

    # --- Gets data for setup  --- #
    filedata: List[str] = []
    configurations: List[str] = []
    try:
        with open("Configurations.txt", "r") as settings:
            for line in settings:
                filedata.append(line.split(":")[0])
                if ":" in line:
                    configurations.append(line.split(":")[1].strip())
        if compare(filedata) is False:
            repair_config_file()
    except:
        repair_config_file()
    error_log = validate(configurations)
    if len(error_log) > 0:
        print("Errors were found!!!\n")
        for error in error_log:
            print(error)
        input("\nCould not complete setup, please change fields accordingly and run the calculator again. "
              "Press enter to exit.\n>> ")
        sys.exit()
    start_adrenaline = int(configurations[0])
    gain = int(configurations[1])
    attack_speed = configurations[2].upper()
    activate_bleeds = configurations[3]
    bound: str = configurations[4]
    if bound == "False":
        debilitating = []
    my_abilities = []
    for ability in configurations[5][1:-1].split(","):
        my_abilities.append(ability.strip().upper())
    # --- Different styles of combat tree give varying amounts of adrenaline from auto attacks --- #
    style: Tuple[str, str] = tuple(configurations[6][1:-1].split(","))
    if style[0] == "MAGIC":
        auto_adrenaline = 2
    else:
        if style[1] != "2":
            auto_adrenaline = 2
        else:
            auto_adrenaline = 3
    cycle_duration = float(configurations[7])
    units: str = configurations[8]
    if units == "ticks":
        cycle_duration *= 0.6


def main() -> None:
    global basic_ability_list, threshold_ability_list, ultimate_ability_list, track_cooldown, track_buff, ability_path, ability_ready

    # Converts raw seconds into Years, Weeks, etc...
    def get_time(seconds: int) -> str:
        years: int = int(seconds / 31449600)
        seconds -= years * 31449600
        weeks: int = int(seconds / 604800)
        seconds -= weeks * 604800
        days: int = int(seconds / 86400)
        seconds -= days * 86400
        hours: int = int(seconds / 3600)
        seconds -= hours * 3600
        minutes: int = int(seconds / 60)
        seconds -= minutes * 60
        eta: str = f"{years} years, {weeks} weeks, {days} days, {hours} hours, {minutes} minutes and {seconds} seconds."
        return eta

    setup_config()
    get_db_ability_data()
    # --- Dictionaries, lists and other data types laid out here --- #
    print("Starting process ...")
    copy_of_ready = dict(ability_ready)
    basic_ability_list = [a for a in ability_type if ability_type[a] == "B"]
    threshold_ability_list = [a for a in ability_type if ability_type[a] == "T"]
    ultimate_ability_list = [a for a in ability_type if ability_type[a] == "U"]
    track_cooldown = {}
    track_buff = {}
    ability_path = []
    best_rotation: List[str] = []
    worst_rotation: List[str] = []
    # --- Calculations for estimation of time remaining --- #
    permutation_count: int = math.factorial(len(abilities))
    time_remaining_calculation: int = permutation_count / 10000
    runthrough: int = 0
    # --- Tracking of highest and lowest damaging ability bars  --- #
    current_highest: float = 0
    current_lowest: float = float("inf")
    # Define the amount of targets affected by area of effect attacks
    aoe_average_targets_hit: float = 2.5
    # --- Gets rotation length --- #
    while True:
        try:
            if len(aoe) > 0:  # Only ask if AoE abilities are in my_abilities
                aoe_average_targets_hit = float(input("How many targets on average will your AoE abilities hit? "))
                if aoe_average_targets_hit < 1:
                    print("Area of effect abilities should hit at least 1 target per use.")
                    continue
            break
        except:
            print("Invalid Input.")
    if aoe_average_targets_hit > 1:
        for ability in abilities:
            if ability in aoe:
                ability_damage[ability] = ability_damage[ability] * aoe_average_targets_hit
    print("Startup Complete! Warning, the more the abilities, and the higher the cycle time, the more time it will take"
          " to process. A better processor will improve this speed.")
    choice: str = input("Start Calculations? (Y/N) ").upper()
    if (choice != "Y") and (choice != "YES"):
        sys.exit()
    # --- Calculations start here --- #
    start: int = int(time.time())  # Record time since epoch (UTC) (in seconds)
    try:  # Will keep running until Control C (or other) is pressed to end process
        for permutation in itertools.permutations(abilities):
            damage_dealt: float = ability_rotation(permutation)
            # --- Reset data ready for next ability bar to be tested
            # and check if any better/worse bars have been found --- #
            ability_ready = dict(copy_of_ready)
            track_cooldown = {}
            track_buff = {}
            if round(damage_dealt, 1) > current_highest:
                current_highest = round(damage_dealt, 1)
                best_rotation = []
                best_rotation = list(ability_path)
                best_bar: List[str] = list(permutation)
                print(f"New best bar with damage {current_highest}: {best_bar}")
            if round(damage_dealt, 1) < current_lowest:
                current_lowest = round(damage_dealt, 1)
                worst_rotation: List[str] = []
                worst_rotation: List[str] = list(ability_path)
                worst_bar = list(permutation)
            ability_path = []
            runthrough += 1
            # --- Time Remaining estimation calculations every 10,000 bars analysed --- #
            if runthrough == 10000:
                end_estimation = int(time_remaining_calculation * (time.time() - start))
            if runthrough % 10000 == 0:
                print(f"\r===== {round(float(runthrough / permutation_count) * 100, 3)}"
                      f"% ===== Estimated time remaining: {get_time(int(end_estimation - (time.time() - start)))}"
                      f"; Best found: {current_highest}%" + (" " * 22), end="")
                time_remaining_calculation -= 1
                end_estimation = int(time_remaining_calculation * (time.time() - start))
                start = time.time()
    except KeyboardInterrupt:
        print("\nProcess terminated!")
    # --- Display results --- #
    print(f"\n\nHighest ability damage: {current_highest}%")
    print(f"Best ability bar found: {best_bar}")
    print(f"{best_rotation}\n")
    print(f"Lowest ability damage: {current_lowest}%")
    print(f"Worst ability bar found: {worst_bar}")
    print(worst_rotation)
    input("\nPress enter to exit\n")


# Execute main() function
if __name__ == "__main__":
    main()
