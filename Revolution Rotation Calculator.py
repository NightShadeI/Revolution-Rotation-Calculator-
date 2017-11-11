import math
import time

import config


def extract(key):
    return {ability['name'].upper(): ability[key] for ability in config.ABILITIES if key in ability}


Abilities = [ability['name'].upper() for ability in config.ABILITIES]
# --- Defining how abilities work --- #
AttackSpeedCooldowns = {str(speed['name']).upper(): speed['time'] for speed in config.ATTACK_SPEED_COOLDOWNS}
AbilityDamage = extract('damage')  # Ability damage of every ability
AbilityCooldown = extract('cooldown')  # Cooldowns of abilities (in seconds)
# Type of ability (B = basic, T = threshold, U = ultimate)
AbilityType = {key: value[0].upper() for (key, value) in extract('type').items()}
# Flag on if you can use abilties (based on adrenaline)
Ready = {ability['name'].upper(): ability['type'] == 'basic' for ability in config.ABILITIES}
# Number of seconds DOT abilities last
Bleeds = {key: value['time'] for (key, value) in extract('bleed').items()}
# Bleeds that have their first hit affected by damage modifying abilities
SpecialBleeds = [key for (key, value) in extract('bleed').items() if value['first_hit_buffable']]
# Abilities that take longer than 1.8 seconds to use but will still have full impact from abilties in list CritBoost
SpecialAbilities = [key for (key, value) in extract('crit_boost_affected').items() if value]
# How long stuns, DPS increases .. etc last
Buff_Time = {key: value['time'] for (key, value) in extract('buff').items()}
# Multiplier for boosted damage
Buff_Effect = {key: value['multiplier'] for (key, value) in extract('buff').items() if 'multiplier' in value}
CritBoost = [key for (key, value) in extract('buff').items() if value.get('crit_boost', False)]
# Abilities that do extra damage when target stun or bound
Punishing = [key for (key, value) in extract('punishing').items() if value]
# Abilities that can stun or bind target
Debilitating = [key for (key, value) in extract('debilitating').items() if value]
Binds = [key for (key, value) in extract('binds').items() if value]
AoEAverageTargetsHit = config.AOE_AVERAGE_TARGETS_HIT
AoE = [key for (key, value) in extract('aoe').items() if value]

def AbilityRotation(Permutation, AttackSpeed, Activate_Bleeds, Ring, Start_Adrenaline, Auto_Adrenaline, Time): # Will return how much damage an ability bar will do over a given time
    # --- Defining Variables --- #
    Altered_Bleeds = False
    Current = 0
    Current_Buff = float(1)
    Clock = 0
    Shards = 0
    Adrenaline = Start_Adrenaline
    # --- Calculations begin here --- #
    AbilityPath.append('AUTO' + ' D: ' + str(round(Current,1)) + ' T: ' + str(round(Clock, 1)) + ' A: ' + str(Adrenaline))
    Current += 50
    Adrenaline += Auto_Adrenaline
    if Adrenaline > 100:
            Adrenaline = 100
    if Adrenaline < 0:
        Adrenaline = 0
    if Adrenaline >= 50:
        for Ability in AbilityType:
            if AbilityType[Ability] == 'T':
                Ready[Ability] = True
            elif Adrenaline == 100:
                for Ability in AbilityType:
                    if AbilityType[Ability] == 'U':
                        Ready[Ability] = True
    Clock += 0.6
    Clock = round(Clock, 1)
    while Clock < Time:
        for ability in Permutation:
            if Clock < Time:
                if Ready[ability] == True: # Checks if ability can be used
                    Ready[ability] = False
                    # --- Modifying adrenaline as required --- #
                    AbilityPath.append(ability + ' D: ' + str(round(Current,1)) + ' T: ' + str(round(Clock, 1)) + ' A: ' + str(Adrenaline))
                    if AbilityType[ability] == 'B':
                        Adrenaline += 8
                    elif AbilityType[ability] == 'T':
                        Adrenaline -= 15
                    else:
                        Adrenaline -= (75 - Ring)  
                    if Adrenaline > 100:
                        Adrenaline = 100
                    # --- Adding shards if they are used, or using them if activated --- #
                    if ability == 'STORM SHARDS':
                        if Shards < 10:
                            Shards += 1
                    if ability == 'SHATTER':
                        Current += round(Shards * 85, 1)
                        Shards = 0
                    # --- Calculating how much damage abilities should do --- #
                    Warning = False
                    Multiplier = float(1)
                    for Ability in TrackBuff:
                        if ((Buff_Time[Ability] - TrackBuff[Ability]) < AbilityTime[ability]) and (Ability in CritBoost):
                            Warning = True # Determins if abilties increasing potential damage next hit will runout during ability usage.
                            Multiplier = Multiplier * ((Buff_Time[Ability] - TrackBuff[Ability])/AbilityTime[ability])
                    if ability in Bleeds:
                        if (Activate_Bleeds == True) and (Altered_Bleeds == False):
                            for Ability in Binds:
                                if Ability in TrackBuff:
                                    Alter_Bleeds(Activate_Bleeds)
                                    Altered_Bleeds = True
                        if ability in SpecialBleeds:
                            AbilityDamage[ability] = ((112.8 * Current_Buff) + 313.33)
                        if (Time - Clock) >= Bleeds[ability]:
                            Current += round(AbilityDamage[ability], 1)
                        else:
                            Current += round((float(float(Time - Clock)/Bleeds[ability]) * AbilityDamage[ability]), 1)
                        if (Activate_Bleeds == True) and (Altered_Bleeds == True):
                            Condition = False
                            for Ability in Binds:
                                if Ability in TrackBuff:
                                    Condition = True
                            if Condition == False:
                                Alter_Bleeds(Activate_Bleeds)
                                Altered_Bleeds = False
                    else:
                        if (ability in Punishing) and (Buff_Available() == True):
                            if (Time - Clock) >= AbilityTime[ability]:
                                Current += round(AbilityDamage[ability] * Buff_Effect[ability] * Current_Buff, 1)
                            else:
                                Current += round(AbilityDamage[ability] * Buff_Effect[ability] * Current_Buff * ((Time - Clock)/AbilityTime[ability]), 1)
                        
                        else:
                            if (Warning == True) and (Current_Buff > 1) and (AbilityTime[ability] > 1.8) and (ability not in SpecialAbilities):
                                if (Time - Clock) >= AbilityTime[ability]:
                                    Current += round(AbilityDamage[ability] * (((Current_Buff - 1) * Multiplier)+1) , 1)
                                else:
                                    Current += round(AbilityDamage[ability] * (((Current_Buff - 1) * Multiplier)+1) * ((Time - Clock)/AbilityTime[ability]) , 1)
                            else:
                                if (Time - Clock) >= AbilityTime[ability]:
                                    Current += round(AbilityDamage[ability] * Current_Buff, 1)
                                else:
                                    Current += round(AbilityDamage[ability] * Current_Buff * ((Time - Clock)/AbilityTime[ability]), 1)
                    # --- Increasing rotation duration and managing cooldowns --- #
                    Clock += AbilityTime[ability]
                    Clock = round(Clock,1)
                    TrackCooldown[ability] = float(0)
                    if ability in Buff_Time:
                        if ability not in Punishing:
                            TrackBuff[ability] = 0
                            if (ability not in Punishing) and (ability in Buff_Effect):
                                Current_Buff = Current_Buff * Buff_Effect[ability]
                    Current_Buff = AdjustCooldowns(Current_Buff, Adrenaline, AbilityTime[ability]) # Will also manage cooldowns
                    break
        # --- Determines whether thresholds or ultimates may be used --- # 
        if Clock < Time:
            if Adrenaline >= 50:
                for Ability in AbilityType:
                    if AbilityType[Ability] == 'T':
                        if Ability not in TrackCooldown:
                            Ready[Ability] = True
                    if Adrenaline == 100:
                        for Ability in AbilityType:
                            if AbilityType[Ability] == 'U':
                                if Ability not in TrackCooldown:
                                    Ready[Ability] = True
            if Adrenaline < 50:
                for Ability in AbilityType:
                    if AbilityType[Ability] == 'T':
                        Ready[Ability] = False
            if Adrenaline != 100:
                for Ability in AbilityType:
                    if AbilityType[Ability] == 'U':
                        Ready[Ability] = False
        # --- Determines if any abilities available/ whether auto attacks must be used --- #
        if Clock < Time:
            AbilityAvailable = False
            for ability in Permutation:
                if Ready[ability] == True:
                    AbilityAvailable = True
            if AbilityAvailable == False:
                if Auto_Available() == True:
                    if (Clock + AttackSpeedCooldowns[AttackSpeed]) <= Time:
                        Clock +=  AttackSpeedCooldowns[AttackSpeed]
                        Clock = round(Clock, 1)
                    else:
                        Clock += (Time - Clock)
                        Clock = round(Clock, 1)
                        break
                    AbilityPath.append('AUTO' + ' D: ' + str(round(Current,1)) + ' T: ' + str(round(Clock, 1)) + ' A: ' + str(Adrenaline))
                    if float(Time - Clock) >= 0.6:
                        Current += round(50 * Current_Buff, 1)
                    else:
                        Current += round(float(50 * round(float((Time - Clock)/0.6), 1)) * Current_Buff, 1) 
                    Adrenaline += Auto_Adrenaline
                    Clock += 0.6
                    if Adrenaline > 100:
                        Adrenaline = 100
                    Current_Buff = AdjustCooldowns(Current_Buff, Adrenaline, (AttackSpeedCooldowns[AttackSpeed] + 0.6)) # Will also manage cooldowns
                else:
                    Clock += 0.6
                    Clock = round(Clock, 1)
                    Current_Buff = AdjustCooldowns(Current_Buff, Adrenaline, 0.6)
    return Current

def Error(): # Called on during invalid inputs
    print('Invalid Input')

# --- Gets data for setup  --- #
while True:
    try:
        Start_Adrenaline = int(input('How much adrenaline will you start rotation with? '))
        break
    except: Error()
AttackSpeed = input('What is your stated attack speed? ').upper()
while not AttackSpeed in AttackSpeedCooldowns:
    print('Expected fastest, fast, average, slow or slowest.')
    AttackSpeed = input('What is your stated attack speed? ').upper()
Ring = input('Will you be using a ring of vigour? (Y/N) ')
if Ring.upper() == 'Y' or Ring.upper() == 'YES':
    Ring = 10
else: Ring = 0
Activate_Bleeds = False
Activate_Bleeds = input('Will you be walking enemy with bleeds?(Y/N) ').upper()
if Activate_Bleeds != 'Y' and Activate_Bleeds != 'YES':
    for item in AbilityDamage:
        # --- Adjusts DOT multiplier that occurs when an enemy moves during bleed --- #
        if item == 'FRAGMENTATION SHOT' or item == 'COMBUST':
            AbilityDamage[item] = AbilityDamage[item]/2 
        elif item == 'SLAUGHTER':
            AbilityDamage[item] = AbilityDamage[item]/3
else: Activate_Bleeds = True
# --- Different styles of combat tree give varying amounts of adrenaline from auto attacks --- #
Auto_Adrenaline = input('What style will you be using? ').upper()
if Auto_Adrenaline == 'MAGIC':
    Auto_Adrenaline = 2
else:
    Auto_Adrenaline = input('One handed or two handed weapon?(1/2) ').upper()
    if Auto_Adrenaline != '2':
        Auto_Adrenaline = 2
    else:
        Auto_Adrenaline = 3
Bound = input('Can the enemy be stun or bound?(Y/N) ').upper()
if Bound != 'Y' or Bound != 'YES':
    Debilitating = []
# --- Functions are layed out here --- #
def Auto_Available(): # Will check if an auto attack is needed to be used
    Is_Available = True
    for Ability in TrackCooldown:
        if (AbilityCooldown[Ability] - TrackCooldown[Ability]) < AttackSpeedCooldowns[AttackSpeed]:
            return False
    return True
            
def Get_Permutation(MyList, index): # Will generate an ability bar that has not been analysed yet
    NewList = []
    Temp_List = list(MyList)
    Denominator = len(Temp_List)
    while len(Temp_List) > 0:
        NewList.append(Temp_List[index%Denominator])
        del Temp_List[index%Denominator]
        index = int(index/Denominator)
        Denominator -= 1
    return NewList

def Get_Time(Seconds): # Converts raw seconds into Years, Weeks, etc...
    Years = int(Seconds/31449600)
    Seconds -= Years * 31449600
    Weeks = int(Seconds/604800)
    Seconds -= Weeks * 604800
    Days = int(Seconds/86400)
    Seconds -= Days * 86400
    Hours = int(Seconds/3600)
    Seconds -= Hours * 3600
    Minutes = int(Seconds/60)
    Seconds -= Minutes * 60
    Time = str(Years) + ' years, ' + str(Weeks) + ' weeks, ' + str(Days) + ' days, ' + str(Hours) + ' hours, ' + str(Minutes) + ' minutes and ' + str(Seconds) + ' seconds'
    return Time

def Alter_Bleeds(Activate_Bleeds):
    if 'FRAGMENTATION SHOT' in AbilityDamage:
        if AbilityDamage['FRAGMENTATION SHOT'] == 120.6:
            AbilityDamage['FRAGMENTATION SHOT'] *= 2
        if AbilityDamage['FRAGMENTATION SHOT'] == 241.2:
            AbilityDamage['FRAGMENTATION SHOT'] /= 2
    if 'COMBUST' in AbilityDamage:
        if AbilityDamage['COMBUST'] == 120.6:
            AbilityDamage['COMBUST'] *= 2
        if AbilityDamage['COMBUST'] == 241.2:
            AbilityDamage['COMBUST'] /= 2
    if 'SLAUGHTER' in AbilityDamage:
        if AbilityDamage['SLAUGHTER'] == 145:
            AbilityDamage['SLAUGHTER'] *= 3
        if AbilityDamage['SLAUGHTER'] == 435:
            AbilityDamage['SLAUGHTER'] /= 3
            
def Remove(CopyOfReady): # Removes abilities from lists and dictionaries not being used to save runtime and memory
    for ability in Abilities:
        if not (ability in MyAbilities):
            del AbilityDamage[ability]
            del AbilityCooldown[ability]
            del AbilityType[ability]
            del AbilityTime[ability]
            del Ready[ability]
            if ability in Bleeds:
                del Bleeds[ability]
            if ability in Buff_Time:
                del Buff_Time[ability]
            if ability in Buff_Effect:
                del Buff_Effect[ability]
            if ability in Punishing:
                Punishing.remove(ability)
            if ability in Debilitating:
                Debilitating.remove(ability)
            if ability in CritBoost:
                CritBoost.remove(ability)
            if ability in SpecialBleeds:
                SpecialBleeds.remove(ability)
            if ability in SpecialAbilities:
                SpecialAbilities.remove(ability) 
            if ability in AoE:
                AoE.remove(ability)
    return dict(Ready)

def Buff_Available(): # Determines if enemy vulnerable to extra damage due to stuns or binds
    for ability in Debilitating:
        if ability in TrackBuff:
            return True
    return False


def AdjustCooldowns(Current_Buff, Adrenaline, Time): # Decreases Cooldowns of abilities and buffs as well as modifying and damage multipliers
    for Ability in TrackCooldown:
        TrackCooldown[Ability] += Time
        TrackCooldown[Ability] = round(TrackCooldown[Ability], 1)
        if TrackCooldown[Ability] >= AbilityCooldown[Ability]:
            TrackCooldown[Ability] = 0
            if AbilityType[Ability] == 'T':
                if Adrenaline >= 50:
                    Ready[Ability] = True
            elif AbilityType[Ability] == 'U':
                if Adrenaline == 100:
                    Ready[Ability] = True
            else:
                Ready[Ability] = True
    for Ability in Permutation:
        if Ability in TrackCooldown:
            if TrackCooldown[Ability] == 0:
                del TrackCooldown[Ability]
    for Ability in TrackBuff:
        TrackBuff[Ability] += Time
        TrackBuff[Ability] = round(TrackBuff[Ability], 1)
        if TrackBuff[Ability] >= Buff_Time[Ability]:
            TrackBuff[Ability] = 0
    for Ability in Permutation:
        if Ability in TrackBuff:
            if TrackBuff[Ability] == 0:
                del TrackBuff[Ability]
                if (Ability not in Punishing) and (Ability in Buff_Effect):
                    Current_Buff = Current_Buff/Buff_Effect[Ability]
    return Current_Buff
    
# --- Gets abilities to be analysed --- #
MyAbilities = []
Counter = 1
AbilityInput = '.'
while AbilityInput:
    AbilityInput = input('Enter ability (' + str(Counter) + '): ').upper()
    if AbilityInput != '':
        # --- Add abilities to list to be analysed --- #
        if AbilityInput in AbilityDamage:
            #print("Ability " + AbilityInput + " deals " + str(AbilityDamage[AbilityInput]) + " damage")
            MyAbilities.append(AbilityInput)
            print('Success!')
            Counter += 1
        else:
            print('Error: No such ability in database. Contact administrator')

# --- Dictionaries, lists and other data types layed out here --- #
print('Starting process ... ')
AbilityTime = extract('time') # How long it takes to use each ability
CopyOfReady = {}
CopyOfReady = Remove(CopyOfReady)
TrackCooldown = {}
TrackBuff = {}
AbilityPath = [] 
BestRotation = []
WorstRotation = []
# --- Calculations for estimation of time remaining --- #
Permutations = math.factorial(len(MyAbilities)) 
Time_Remaining_Calculation = int(Permutations/10000)
Runthrough = int(0)
# --- Tracking of highest and lowest damaging ability bars  --- #
CurrentHighest = float(0)
CurrentLowest = float(100000000000000000000)

# --- Gets rotation length --- #
while True:
    try:
        if len(AoE) > 0: # Only ask if AoE abilities are in MyAbilities
            AoEAverageTargetsHit = float(input('How many targets on average will your AoE abilities hit? '))
            if AoEAverageTargetsHit < 1:
                print("Area of effect abilities should hit at least 1 target per use.")
                continue
        break
    except: Error()
        
if AoEAverageTargetsHit > 1:
    for ability in MyAbilities:
        if ability in AoE:
            #print("Altering average damage of ability " + ability + " from " + str(AbilityDamage[ability]) + " to " + str(AbilityDamage[ability]*AoEAverageTargetsHit))
            AbilityDamage[ability] = AbilityDamage[ability]*AoEAverageTargetsHit
      
while True:
    try:
        Time = float(input('How long will rotation last? WARNING: Longer times require longer wait times, a better processor will improve this speed. \n>> '))
        break
    except: Error()
    
# --- Calculations start here --- #

Start = int(time.time()) # Record time since epoch (UTC) (in seconds)
try: # Will keep running until Control C (or other) is pressed to end process
    for index in range(0, Permutations):
        Permutation = Get_Permutation(MyAbilities, index)
        Current = AbilityRotation(Permutation, AttackSpeed, Activate_Bleeds, Ring, Start_Adrenaline, Auto_Adrenaline, Time)
        # --- Reset data ready for next ability bar to be tested and check if any better/worse bars have been found --- #
        Ready = dict(CopyOfReady)
        TrackCooldown = {}
        TrackBuff = {}
        if (round(Current, 1) > CurrentHighest):
            CurrentHighest = round(Current, 1)
            BestRotation = []
            BestRotation = list(AbilityPath)
            BestBar = list(Permutation)
            print("New best bar with damage " + str(CurrentHighest) + ": " + str(BestBar))
        if round(Current, 1) < CurrentLowest:
            CurrentLowest = round(Current, 1)
            WorstRotation = []
            WorstRotation = list(AbilityPath)
            WorstBar = list(Permutation)
        AbilityPath = []
        Runthrough += 1
        # --- Time Remaining estimation calculations every 10,000 bars analysed --- #
        if Runthrough == 10000:
            End_Estimation = int(Time_Remaining_Calculation * (time.time() - Start))
        if Runthrough % 10000 == 0:
            print(str('\r===== ') + str(round(float(Runthrough/Permutations) * 100, 3)) + str('% ===== ') + str('Estimated time remaining: ') + str(Get_Time(int(End_Estimation - (time.time() - Start)))) + '; Best found: ' + str(CurrentHighest) + '%' +
                  (' ' * 22), end = '')
            Time_Remaining_Calculation -= 1
            End_Estimation = int(Time_Remaining_Calculation * (time.time() - Start))
            Start = time.time()
except KeyboardInterrupt:
    print('\nProcess terminated!')
# --- Display results --- #
print('\n\nHighest ability damage: ' + str(CurrentHighest) + '%')
print('Best ability bar found: ' + str(BestBar))
print(str(BestRotation) + '\n')
print('Lowest ability damage: ' + str(CurrentLowest) + '%')
print('Worst ability bar found: ' + str(WorstBar))
print(str(WorstRotation))
input('\nPress enter to exit\n')
