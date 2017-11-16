import math
import sys
import time

Abilities = ['ASPHYXIATE', 'ASSAULT', 'BACKHAND', 'BARGE', 'BERSERK', 'BINDING SHOT', 'BLOOD TENDRILS', 'BOMBARDMENT',
             'CHAIN', 'CLEAVE', 'COMBUST', 'CONCENTRATED BLAST', 'CORRUPTION BLAST', 'CORRUPTION SHOT', 'DAZING SHOT',
             'DEADSHOT', "DEATH'S SWIFTNESS", 'DEBILITATE', 'DECIMATE', 'DEEP IMPACT', 'DESTROY', 'DETONATE',
             'DISMEMBER', 'DRAGON BREATH', 'FLURRY', 'FORCEFUL BACKHAND', 'FRAGMENTATION SHOT', 'FRENZY', 'FURY',
             'HAVOC', 'HURRICANE', 'IMPACT', 'KICK', 'MASSACRE', 'METAMORPHOSIS', 'NEEDLE STRIKE', 'OMNIPOWER',
             'ONSLAUGHT', 'OVERPOWER', 'PIERCING SHOT', 'PULVERISE', 'PUNISH', 'QUAKE', 'RAPID FIRE', 'RICOCHET',
             'SACRIFICE', 'SEVER', 'SHADOW TENDRILS', 'SHATTER', 'SLAUGHTER', 'SLICE', 'SMASH', 'SMOKE TENDRILS',
             'SNAP SHOT', 'SNIPE', 'SONIC WAVE', 'STOMP', 'STORM SHARDS', 'SUNSHINE', 'TIGHT BINDINGS', 'TSUNAMI',
             "TUSKA'S WRATH", 'UNLOAD', 'WILD MAGIC', 'WRACK']

# --- Defining how abilities work --- #

# Cooldowns for casewhere no abilities may be used
AttackSpeedCooldowns = {'FASTEST': 2.4, 'FAST': 3.0, 'AVERAGE': 3.6, 'SLOW': 4.2, 'SLOWEST': 7.2}

# Ability damage of every ability
AbilityDamage = {'ASPHYXIATE': 451.2, 'ASSAULT': 525.6, 'BACKHAND': 60, 'BARGE': 75, 'BERSERK': 0, 'BINDING SHOT': 60,
                 'BLOOD TENDRILS': 324, 'BOMBARDMENT': 131.4, 'CHAIN': 60, 'CLEAVE': 112.8, 'COMBUST': 241.2,
                 'CONCENTRATED BLAST': 152.8, 'CORRUPTION BLAST': 200, 'CORRUPTION SHOT': 200, 'DAZING SHOT': 94.2,
                 'DEADSHOT': 426.13, "DEATH'S SWIFTNESS": 0, 'DEBILITATE': 60, 'DECIMATE': 112.8, 'DEEP IMPACT': 120,
                 'DESTROY': 451.2, 'DETONATE': 225, 'DISMEMBER': 120.6, 'DRAGON BREATH': 112.8, 'FLURRY': 204,
                 'FORCEFUL BACKHAND': 120, 'FRAGMENTATION SHOT': 120.6, 'FRENZY': 610, 'FURY': 152.8, 'HAVOC': 94.2,
                 'HURRICANE': 265, 'IMPACT': 60, 'KICK': 60, 'MASSACRE': 426.13, 'METAMORPHOSIS': 0,
                 'NEEDLE STRIKE': 94.2, 'OMNIPOWER': 300, 'ONSLAUGHT': 532, 'OVERPOWER': 300, 'PIERCING SHOT': 56.4,
                 'PULVERISE': 300, 'PUNISH': 56.4, 'QUAKE': 131.4, 'RAPID FIRE': 451.2, 'RICOCHET': 60, 'SACRIFICE': 60,
                 'SEVER': 112.8, 'SHADOW TENDRILS': 283, 'SHATTER': 0, 'SLAUGHTER': 145, 'SLICE': 75, 'SMASH': 94.2,
                 'SMOKE TENDRILS': 345, 'SNAP SHOT': 265, 'SNIPE': 172, 'SONIC WAVE': 94.2, 'STOMP': 120,
                 'STORM SHARDS': 0, 'SUNSHINE': 0, 'TIGHT BINDINGS': 120, 'TSUNAMI': 250, "TUSKA'S WRATH": 5940,
                 'UNLOAD': 610, 'WILD MAGIC': 265, 'WRACK': 56.4}

# Cooldowns of abilties (in seconds)
AbilityCooldown = {'ASPHYXIATE': 20.4, 'ASSAULT': 30, 'BACKHAND': 15, 'BARGE': 20.4, 'BERSERK': 60, 'BINDING SHOT': 15,
                   'BLOOD TENDRILS': 45, 'BOMBARDMENT': 30, 'CHAIN': 10.2, 'CLEAVE': 7.2, 'COMBUST': 15,
                   'CONCENTRATED BLAST': 5.4, 'CORRUPTION BLAST': 15, 'CORRUPTION SHOT': 15, 'DAZING SHOT': 5.4,
                   'DEADSHOT': 30, "DEATH'S SWIFTNESS": 60, 'DEBILITATE': 30, 'DECIMATE': 7.2, 'DEEP IMPACT': 15,
                   'DESTROY': 20.4, 'DETONATE': 30, 'DISMEMBER': 15, 'DRAGON BREATH': 10.2, 'FLURRY': 20.4,
                   'FORCEFUL BACKHAND': 15, 'FRAGMENTATION SHOT': 15, 'FRENZY': 60, 'FURY': 5.4, 'HAVOC': 10.2,
                   'HURRICANE': 20.4, 'IMPACT': 15, 'KICK': 15, 'MASSACRE': 60, 'METAMORPHOSIS': 60,
                   'NEEDLE STRIKE': 5.4, 'OMNIPOWER': 30, 'ONSLAUGHT': 120, 'OVERPOWER': 60, 'PIERCING SHOT': 3,
                   'PULVERISE': 60, 'PUNISH': 3, 'QUAKE': 20.4, 'RAPID FIRE': 20.4, 'RICOCHET': 10.2, 'SACRIFICE': 30,
                   'SEVER': 15, 'SHADOW TENDRILS': 45, 'SHATTER': 120, 'SLAUGHTER': 30, 'SLICE': 3, 'SMASH': 10.2,
                   'SMOKE TENDRILS': 45, 'SNAP SHOT': 20.4, 'SNIPE': 10.2, 'SONIC WAVE': 5.4, 'STOMP': 15,
                   'STORM SHARDS': 30, 'SUNSHINE': 60, 'TIGHT BINDINGS': 15, 'TSUNAMI': 60, "TUSKA'S WRATH": 120,
                   'UNLOAD': 60, 'WILD MAGIC': 20.4, 'WRACK': 3}

# How long it takes to use each ability
AbilityTime = {'ASPHYXIATE': 5.4, 'ASSAULT': 5.4, 'BACKHAND': 1.8, 'BARGE': 1.8, 'BERSERK': 1.8, 'BINDING SHOT': 1.8,
               'BLOOD TENDRILS': 1.8, 'BOMBARDMENT': 1.8, 'CHAIN': 1.8, 'CLEAVE': 1.8, 'COMBUST': 1.8,
               'CONCENTRATED BLAST': 3.6, 'CORRUPTION BLAST': 1.8, 'CORRUPTION SHOT': 1.8, 'DAZING SHOT': 1.8,
               'DEADSHOT': 1.8, "DEATH'S SWIFTNESS": 1.8, 'DEBILITATE': 1.8, 'DECIMATE': 1.8, 'DEEP IMPACT': 1.8,
               'DESTROY': 4.2, 'DETONATE': 3.6, 'DISMEMBER': 1.8, 'DRAGON BREATH': 1.8, 'FLURRY': 5.4,
               'FORCEFUL BACKHAND': 1.8, 'FRAGMENTATION SHOT': 1.8, 'FRENZY': 4.2, 'FURY': 3.6, 'HAVOC': 1.8,
               'HURRICANE': 1.8, 'IMPACT': 1.8, 'KICK': 1.8, 'MASSACRE': 1.8, 'METAMORPHOSIS': 1.8,
               'NEEDLE STRIKE': 1.8, 'OMNIPOWER': 1.8, 'ONSLAUGHT': 4.8, 'OVERPOWER': 1.8, 'PIERCING SHOT': 1.8,
               'PULVERISE': 1.8, 'PUNISH': 1.8, 'QUAKE': 1.8, 'RAPID FIRE': 5.4, 'RICOCHET': 1.8, 'SACRIFICE': 1.8,
               'SEVER': 1.8, 'SHADOW TENDRILS': 1.8, 'SHATTER': 1.8, 'SLAUGHTER': 1.8, 'SLICE': 1.8, 'SMASH': 1.8,
               'SMOKE TENDRILS': 5.4, 'SNAP SHOT': 1.8, 'SNIPE': 3.6, 'SONIC WAVE': 1.8, 'STOMP': 1.8,
               'STORM SHARDS': 1.8, 'SUNSHINE': 1.8, 'TIGHT BINDINGS': 1.8, 'TSUNAMI': 1.8, "TUSKA'S WRATH": 1.8,
               'UNLOAD': 4.2, 'WILD MAGIC': 4.8, 'WRACK': 1.8}

# Type of ability (B = basic, T = threshold, U = ultimate)
AbilityType = {'ASPHYXIATE': 'T', 'ASSAULT': 'T', 'BACKHAND': 'B', 'BARGE': 'B', 'BERSERK': 'U', 'BINDING SHOT': 'B',
               'BLOOD TENDRILS': 'T', 'BOMBARDMENT': 'T', 'CHAIN': 'B', 'CLEAVE': 'B', 'COMBUST': 'B',
               'CONCENTRATED BLAST': 'B', 'CORRUPTION BLAST': 'B', 'CORRUPTION SHOT': 'B', 'DAZING SHOT': 'B',
               'DEADSHOT': 'U', "DEATH'S SWIFTNESS": 'U', 'DEBILITATE': 'T', 'DECIMATE': 'B', 'DEEP IMPACT': 'T',
               'DESTROY': 'T', 'DETONATE': 'T', 'DISMEMBER': 'B', 'DRAGON BREATH': 'B', 'FLURRY': 'T',
               'FORCEFUL BACKHAND': 'T', 'FRAGMENTATION SHOT': 'B', 'FRENZY': 'U', 'FURY': 'B', 'HAVOC': 'B',
               'HURRICANE': 'U', 'IMPACT': 'B', 'KICK': 'B', 'MASSACRE': 'U', 'METAMORPHOSIS': 'U',
               'NEEDLE STRIKE': 'B', 'OMNIPOWER': 'U', 'ONSLAUGHT': 'U', 'OVERPOWER': 'U', 'PIERCING SHOT': 'B',
               'PULVERISE': 'U', 'PUNISH': 'B', 'QUAKE': 'T', 'RAPID FIRE': 'T', 'RICOCHET': 'B', 'SACRIFICE': 'B',
               'SEVER': 'B', 'SHADOW TENDRILS': 'T', 'SHATTER': 'T', 'SLAUGHTER': 'T', 'SLICE': 'B', 'SMASH': 'B',
               'SMOKE TENDRILS': 'T', 'SNAP SHOT': 'T', 'SNIPE': 'B', 'SONIC WAVE': 'B', 'STOMP': 'T',
               'STORM SHARDS': 'B', 'SUNSHINE': 'U', 'TIGHT BINDINGS': 'T', 'TSUNAMI': 'U', "TUSKA'S WRATH": 'B',
               'UNLOAD': 'U', 'WILD MAGIC': 'T', 'WRACK': 'B'}

# Flag on if you can use abilties (based on adrenaline)
Ready = {'DEBILITATE': False, 'UNLOAD': False, 'TIGHT BINDINGS': False, 'SNIPE': True, 'SNAP SHOT': False,
         'SHADOW TENDRILS': False, 'RICOCHET': True, 'RAPID FIRE': False, 'PIERCING SHOT': True, 'NEEDLE STRIKE': True,
         'FRAGMENTATION SHOT': True, "DEATH'S SWIFTNESS": False, 'DEADSHOT': False, 'DAZING SHOT': True,
         'CORRUPTION SHOT': True, 'BOMBARDMENT': False, 'BINDING SHOT': True, 'WRACK': True, 'WILD MAGIC': False,
         'TSUNAMI': False, 'SUNSHINE': False, 'SONIC WAVE': True, 'SMOKE TENDRILS': False, 'OMNIPOWER': False,
         'METAMORPHOSIS': False, 'IMPACT': True, 'DRAGON BREATH': True, 'DETONATE': False, 'DEEP IMPACT': False,
         'CORRUPTION BLAST': True, 'CONCENTRATED BLAST': True, 'COMBUST': True, 'CHAIN': True, 'ASPHYXIATE': False,
         "TUSKA'S WRATH": True, 'SHATTER': False, 'STORM SHARDS': True, 'SACRIFICE': True, 'ONSLAUGHT': False,
         'PULVERISE': False, 'FRENZY': False, 'BERSERK': False, 'OVERPOWER': False, 'SEVER': True, 'CLEAVE': True,
         'DESTROY': False, 'BACKHAND': True, 'BARGE': True, 'BLOOD TENDRILS': False, 'FLURRY': False,
         'FORCEFUL BACKHAND': False, 'HAVOC': True, 'HURRICANE': False, 'SLAUGHTER': False, 'SLICE': True,
         'SMASH': True, 'ASSAULT': False, 'DECIMATE': True, 'DISMEMBER': True, 'FURY': True, 'KICK': True,
         'PUNISH': True, 'QUAKE': False, 'STOMP': False,
         'MASSACRE': False}

# time DOT abilties last (seconds)
Bleeds = {'BLOOD TENDRILS': 4.8, 'COMBUST': 6, 'CORRUPTION BLAST': 6, 'CORRUPTION SHOT': 6, 'DEADSHOT': 6,
          'DISMEMBER': 6, 'FRAGMENTATION SHOT': 6, 'MASSACRE': 6, 'SHADOW TENDRILS': 1.8, 'SLAUGHTER': 6,
          'SMOKE TENDRILS': 5.4}
Walking_Bleeds = {'COMBUST': 1, 'FRAGMENTATION SHOT': 1, 'SLAUGHTER': 1.5}

# Bleeds that have their first hit affected by damage modifying abilities
SpecialBleeds = ['DEADSHOT', 'MASSACRE', 'SMOKE TENDRILS']

# Abilities that take longer than 1.8 seconds to use but will still have full impact from abilties in list CritBoost
SpecialAbilities = ['DETONATE', 'SNIPE']

# How long stuns, DPS increases .. etc last
Buff_Time = {'BARGE': 6.6, 'BERSERK': 19.8, 'BINDING SHOT': 9.6, 'CONCENTRATED BLAST': 5.4, "DEATH'S SWIFTNESS": 30,
             'DEEP IMPACT': 3.6, 'FORCEFUL BACKHAND': 3.6, 'FURY': 5.4, 'METAMORPHOSIS': 15, 'NEEDLE STRIKE': 3.6,
             'RAPID FIRE': 6, 'STOMP': 3.6, 'SUNSHINE': 30, 'TIGHT BINDINGS': 9.6}

# multiplier for boosted damage
Buff_Effect = {'BERSERK': 2, 'CONCENTRATED BLAST': 1.1, "DEATH'S SWIFTNESS": 1.5, 'FURY': 1.1, 'METAMORPHOSIS': 1.625,
               'NEEDLE STRIKE': 1.07, 'PIERCING SHOT': 2, 'PUNISH': 2, 'SLICE': 1.506, 'SUNSHINE': 1.5, 'WRACK': 2}

# Abilities that do extra damage when target stun or bound
CritBoost = ['BERSERK', 'CONCENTRATED BLAST', "DEATH'S SWIFTNESS", 'FURY', 'METAMORPHOSIS', 'NEEDLE STRIKE', 'SUNSHINE']
Punishing = ['PIERCING SHOT', 'PUNISH', 'SLICE', 'WRACK']

# Abilities that can stun or bind target
Debilitating = ['BARGE', 'BINDING SHOT', 'DEEP IMPACT', 'FORCEFUL BACKHAND', 'RAPID FIRE', 'STOMP', 'TIGHT BINDINGS']
Binds = ['BARGE', 'BINDING SHOT', 'DEEP IMPACT', 'TIGHT BINDINGS']

AoEAverageTargetsHit = 2.5

AoE = ['BOMBARDMENT', 'CHAIN', 'CLEAVE', 'CORRUPTION BLAST', 'CORRUPTION SHOT', 'DRAGON BREATH', 'FLURRY', 'HURRICANE',
       'QUAKE', 'RICOCHET', 'TSUNAMI']


# Will return how much damage an ability bar will do over a given time
def AbilityRotation(Permutation, AttackSpeed, Activate_Bleeds, Gain, Start_Adrenaline, Auto_Adrenaline, Time):
    # --- Defining Variables --- #
    Altered_Bleeds = False
    Current = 0
    Current_Buff = float(1)
    Clock = 0
    Shards = 0
    Adrenaline = Start_Adrenaline
    # --- Calculations begin here --- #
    AbilityPath.append(f'AUTO D: {round(Current, 1)} T: {round(Clock, 1)} A: {Adrenaline}')
    Current += 50
    Adrenaline += Auto_Adrenaline
    if Adrenaline >= 100:
        Adrenaline = 100
        for Ability in UltimateIterator:
            Ready[Ability] = True
        for Ability in ThresholdIterator:
            Ready[Ability] = True
    elif Adrenaline >= 50:
        for Ability in ThresholdIterator:
            Ready[Ability] = True
    elif Adrenaline < 0:
        Adrenaline = 0
    Clock += 0.6
    Clock = round(Clock, 1)
    while Clock < Time:
        for ability in Permutation:
            if Clock < Time:  # TODO: This is used a lot, is it a necessity?
                if Ready[ability] is True:  # Checks if ability can be used
                    Ready[ability] = False
                    # --- Modifying adrenaline as required --- #
                    AbilityPath.append(f'{ability} D: {round(Current, 1)} T: {round(Clock, 1)} A: {Adrenaline}')
                    if ability in BasicIterator:
                        Adrenaline += 8
                    elif ability in ThresholdIterator:
                        Adrenaline -= 15
                    else:
                        Adrenaline = Gain
                    if Adrenaline > 100:
                        Adrenaline = 100
                    # --- Adding shards if they are used, or using them if activated --- #
                    if ability == 'STORM SHARDS':
                        if Shards < 10:
                            Shards += 1
                    elif ability == 'SHATTER':
                        Current += round(Shards * 85, 1)
                        Shards = 0
                    # --- Calculating how much damage abilities should do --- #
                    MoreBinds = False
                    Altered_Bleeds = False
                    Modified_Damage = False
                    Damage_Multiplier = float(1)  # Multiplier for damage due to damage boosting abilities
                    Bleed_Multiplier = float(1)  # Multiplier incase target is bound (and bind about to run out)
                    for Ability in TrackBuff:
                        if Ability in CritBoost:
                            if ((Buff_Time[Ability] - TrackBuff[Ability]) < AbilityTime[ability]) and (
                                        (ability not in SpecialAbilities) and (AbilityTime[ability] > 1.8)):
                                Damage_Multiplier *= ((((Buff_Time[Ability] - TrackBuff[Ability]) / AbilityTime[
                                    ability]) * (Buff_Effect[Ability] - 1)) + 1)
                            else:
                                Damage_Multiplier *= Buff_Effect[Ability]
                        elif (Ability in Binds) and (Activate_Bleeds is True) and (ability in Walking_Bleeds) and (
                                    len(Debilitating) > 0):
                            if (MoreBinds is False) and (Buff_Time[Ability] - TrackBuff[Ability] < Bleeds[ability]):
                                Bleed_Multiplier = Walking_Bleeds[ability] * (
                                    1 + (Buff_Time[Ability] - TrackBuff[Ability]) / Bleeds[ability])
                            else:
                                Bleed_Multiplier = 1
                                MoreBinds = True
                            Altered_Bleeds = True
                    if (Activate_Bleeds is True) and (ability in Walking_Bleeds) and (Altered_Bleeds is False):
                        Bleed_Multiplier = Walking_Bleeds[ability] * 2
                    Altered_Bleeds = False
                    TimeMultiplier = ModifyTime(Time, Clock, ability)
                    if ability in Bleeds:
                        if ability in SpecialBleeds:
                            if (ability == 'SMOKE TENDRILS'):
                                Current += (AbilityDamage[ability] * Damage_Multiplier)
                            else:
                                AbilityDamage[ability] = ((112.8 * Damage_Multiplier) + 313.33)
                                Modified_Damage = True
                        Current += round(AbilityDamage[ability] * Bleed_Multiplier * TimeMultiplier, 1)
                        if Modified_Damage is True:
                            AbilityDamage[ability] = 426.13
                            Modified_Damage = False
                    elif (ability in Punishing) and (Buff_Available() is True):
                        Current += round(AbilityDamage[ability] * Buff_Effect[ability] * Damage_Multiplier *
                                         TimeMultiplier, 1)
                    else:
                        Current += round(AbilityDamage[ability] * Damage_Multiplier * TimeMultiplier, 1)
                    # --- Increasing rotation duration and managing cooldowns --- #
                    Clock += AbilityTime[ability]
                    Clock = round(Clock, 1)
                    TrackCooldown[ability] = float(0)
                    if ability in Buff_Time and ability not in Punishing:
                        TrackBuff[ability] = 0
                        if ability in Buff_Effect:
                            Current_Buff = Current_Buff * Buff_Effect[ability]
                    # Will also manage cooldowns
                    Current_Buff = AdjustCooldowns(Current_Buff, Adrenaline, AbilityTime[ability])
                    break
        # --- Determines whether thresholds or ultimates may be used --- #
        if Clock < Time:
            if Adrenaline == 100:
                for Ability in (a for a in UltimateIterator if a not in TrackCooldown):
                    Ready[Ability] = True
                for Ability in (a for a in ThresholdIterator if a not in TrackCooldown):
                    Ready[Ability] = True
            elif Adrenaline >= 50:
                for Ability in (a for a in ThresholdIterator if a not in TrackCooldown):
                    Ready[Ability] = True
            elif Adrenaline < 50:
                for Ability in ThresholdIterator:
                    Ready[Ability] = False
            if Adrenaline != 100:
                for Ability in UltimateIterator:
                    Ready[Ability] = False
        # --- Determines if any abilities available/ whether auto attacks must be used --- #
        if Clock < Time:
            AbilityAvailable = False
            for _ in (a for a in Permutation if Ready[a]):
                AbilityAvailable = True
                break
            if AbilityAvailable is False:
                if Auto_Available() is True:
                    if (Clock + AttackSpeedCooldowns[AttackSpeed]) <= Time:
                        Clock += AttackSpeedCooldowns[AttackSpeed]
                    else:
                        Clock += (Time - Clock)
                        break
                    AbilityPath.append(f'AUTO D: {round(Current, 1)} T: {round(Clock, 1)} A: {Adrenaline}')
                    if float(Time - Clock) >= 0.6:
                        Current += round(50 * Current_Buff, 1)
                    else:
                        Current += round(float(50 * round(float((Time - Clock) / 0.6), 1)) * Current_Buff, 1)
                    Adrenaline += Auto_Adrenaline
                    Clock += 0.6
                    if Adrenaline > 100:
                        Adrenaline = 100
                    # Will also manage cooldowns
                    Current_Buff = AdjustCooldowns(Current_Buff, Adrenaline, (AttackSpeedCooldowns[AttackSpeed] + 0.6))
                else:
                    Clock += 0.6
                    Current_Buff = AdjustCooldowns(Current_Buff, Adrenaline, 0.6)
                Clock = round(Clock, 1)
    return Current


# Called on during invalid inputs
def Error():
    print('Invalid Input')


def Repair():
    repair = input('Configurations.txt has been modified, perform repair? (Y/N)\n>> ').upper()
    if (repair == 'Y') or (repair == 'YES'):
        import os
        correct_data = ['# Rotation Paramaters', '', 'Adrenaline: ', 'Gain: ', 'AttackSpeed: ', 'Bleeds: ', 'Stuns: ',
                        'Abilities: [,,,]', 'Style: (,)', 'Time: ', '', '# Mode', '', 'units: seconds']
        if os.path.exists('Configurations.txt'):
            os.remove('Configurations.txt')
        with open('Configurations.txt', 'w') as settings:
            for line in correct_data:
                settings.write(line + str('\n'))
        input('Repair successful! fill out settings in Configurations.txt before running calculator again. '
              'Press enter to exit\n>> ')
    sys.exit()


def Compare(lines):
    # configuration followed by line number
    correct_data = {'Adrenaline': 2, 'Gain': 3, 'AttackSpeed': 4, 'Bleeds': 5, 'Stuns': 6, 'Abilities': 7, 'Style': 8,
                    'Time': 9, 'units': 13}
    for setting in correct_data:
        if setting != lines[correct_data[setting]]:
            return False
    return True


def Validate(configurations):
    ErrorLog = []
    Null = False
    for config in configurations:
        if config == '':
            Null = True
    if Null is True:
        ErrorLog.append('One or more settings have been left as null')

    try:
        setting = int(configurations[0])
        if not (0 <= setting <= 100):
            ErrorLog.append('Adrenaline must be between 0 and 100 inclusive')
    except ValueError:
        ErrorLog.append('Adrenaline must be of form integer')

    try:
        setting = int(configurations[1])
        if not (0 <= setting <= 100):
            ErrorLog.append('Gain must be a positive integer between 0 and 100')
    except ValueError:
        ErrorLog.append('Gain must be of form integer')

    if configurations[2].upper() not in ('SLOWEST', 'SLOW', 'AVERAGE', 'FAST', 'FASTEST'):
        ErrorLog.append("AttackSpeed must either be one of the following options: ('slowest, slow, average, fast,"
                        " fastest')")

    setting = configurations[3]
    if not ((setting.lower() == 'false') or (setting.lower() == 'true')):
        ErrorLog.append('Bleeds must be true or false')

    setting = configurations[4]
    if not ((setting.lower() == 'false') or (setting.lower() == 'true')):
        ErrorLog.append('Stuns must be true or false')

    setting = configurations[5]
    if (setting[0] == '[' and setting[-1] == ']'):
        setting = setting[1:-1].split(',')
        Counter = {}
        if len(setting) > 0:
            for ability in setting:
                ability = ability.upper().strip()
                if (ability not in Abilities) and (ability not in Counter):
                    ErrorLog.append(f'{ability.strip()} is not a recognised ability, or is not included in this '
                                    f'calculator')
                if ability in Counter:
                    Counter[ability] += 1
                    if Counter[ability] == 2:
                        ErrorLog.append(f'{(ability.strip())} is referenced 2 or more times within array. Ensure it '
                                        f'is only referenced once')
                else:
                    Counter[ability] = 1
        else:
            ErrorLog.append('No abilities were added')
    else:
        ErrorLog.append("Abilities must start and end with [], With abilities being seperated by comma's (,)")

    setting = configurations[6]
    if (setting[0] == '(' and setting[-1] == ')'):
        setting = setting[1:-1].split(',')
        if setting[0].upper() not in ('MAGIC', 'RANGED', 'MELEE'):
            ErrorLog.append('First option of Style should be either "magic", "ranged" or "melee" (without quotes)')
        if setting[1] not in ('1', '2'):
            ErrorLog.append('Second option of Style should either be 1 or 2 (1 handed / 2 handed weapon)')
    else:
        ErrorLog.append('Style must start and end with (), with each option being seperate by a single comma (,)')

    try:
        setting = float(configurations[7])
        if not (setting > 0):
            ErrorLog.append('Time must be positive, and not equal to zero or negative')
    except ValueError:
        ErrorLog.append('Time must be a positive decimal (float) or a positive integer')

    if configurations[8].upper() not in ('SECONDS', 'TICKS'):
        ErrorLog.append('units must be either "seconds" or "ticks" (without quoets)')

    return ErrorLog


# --- Gets data for setup  --- #
try:
    filedata = []
    configurations = []
    with open('Configurations.txt', 'r') as settings:
        for line in settings:
            filedata.append(line.split(':')[0])
            if ':' in line:
                configurations.append(line.split(':')[1].strip())
    if Compare(filedata) is False:
        Repair()
except:
    Repair()

ErrorLog = Validate(configurations)
if len(ErrorLog) > 0:
    print('Errors were found, which are listed below:\n')
    for error in ErrorLog:
        print(error)
    input('\nCould not complete setup, please change fields accordingly and run calculator again. '
          'Press enter to exit\n>> ')
    sys.exit()

Start_Adrenaline = int(configurations[0])
Gain = int(configurations[1])
AttackSpeed = configurations[2].upper()
Activate_Bleeds = configurations[3]
Bound = configurations[4]
if Bound == 'False':
    Debilitating = []
MyAbilities = []
for ability in configurations[5][1:-1].split(','):
    MyAbilities.append(ability.strip().upper())
# --- Different styles of combat tree give varying amounts of adrenaline from auto attacks --- #
Style = tuple(configurations[6][1:-1].split(','))
if Style[0] == 'MAGIC':
    Auto_Adrenaline = 2
else:
    if Style[1] != '2':
        Auto_Adrenaline = 2
    else:
        Auto_Adrenaline = 3
Time = float(configurations[7])
Units = configurations[8]
if Units == 'ticks':
    Time *= 0.6


# --- Functions are layed out here --- #
# Will check if an auto attack is needed to be used
def Auto_Available():
    for Ability in TrackCooldown:
        if (AbilityCooldown[Ability] - TrackCooldown[Ability]) < AttackSpeedCooldowns[AttackSpeed]:
            return False
    return True


# Will generate an ability bar that has not been analysed yet
def Get_Permutation(MyList, index):
    NewList = []
    Temp_List = list(MyList)
    Denominator = len(Temp_List)
    while len(Temp_List) > 0:
        NewList.append(Temp_List[index % Denominator])
        del Temp_List[index % Denominator]
        index = int(index / Denominator)
        Denominator -= 1
    return NewList


# Converts raw seconds into Years, Weeks, etc...
def Get_Time(Seconds):
    Years = int(Seconds / 31449600)
    Seconds -= Years * 31449600
    Weeks = int(Seconds / 604800)
    Seconds -= Weeks * 604800
    Days = int(Seconds / 86400)
    Seconds -= Days * 86400
    Hours = int(Seconds / 3600)
    Seconds -= Hours * 3600
    Minutes = int(Seconds / 60)
    Seconds -= Minutes * 60
    Time = str(Years) + f' years, {Weeks} weeks, {Days} days, {Hours} hours, {Minutes} minutes and {Seconds} seconds'
    return Time


def ModifyTime(Time, Clock, ability):
    if (ability in Bleeds) and (ability != 'SHADOW TENDRILS') and ((Time - Clock) < Bleeds[ability]):
        return (Time - Clock) / Bleeds[ability]
    else:
        if (ability not in SpecialAbilities) and (AbilityTime[ability] > 1.8) and (
                    (Time - Clock) < AbilityTime[ability]):
            return (Time - Clock) / AbilityTime[ability]
    return 1


# Removes abilities from lists and dictionaries not being used to save runtime and memory
def Remove(CopyOfReady):
    for ability in Abilities:
        if not (ability in MyAbilities):
            del AbilityDamage[ability]
            del AbilityCooldown[ability]
            del AbilityType[ability]
            del AbilityTime[ability]
            del Ready[ability]
            if ability in Walking_Bleeds:
                del Walking_Bleeds[ability]
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


# Determines if enemy vulnerable to extra damage due to stuns or binds
def Buff_Available():
    for ability in Debilitating:
        if ability in TrackBuff:
            return True
    return False


# Decreases Cooldowns of abilities and buffs as well as modifying and damage multipliers
def AdjustCooldowns(Current_Buff, Adrenaline, Time):
    for Ability in TrackCooldown:
        TrackCooldown[Ability] += Time
        TrackCooldown[Ability] = round(TrackCooldown[Ability], 1)
        if TrackCooldown[Ability] >= AbilityCooldown[Ability]:
            TrackCooldown[Ability] = 0
            if Ability in ThresholdIterator:
                if Adrenaline >= 50:
                    Ready[Ability] = True
            elif Ability in UltimateIterator:
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
                    Current_Buff = Current_Buff / Buff_Effect[Ability]
    return Current_Buff


# --- Dictionaries, lists and other data types layed out here --- #
print('Starting process ... ')

CopyOfReady = {}
CopyOfReady = Remove(CopyOfReady)
BasicIterator = [Ability for Ability in AbilityType if AbilityType[Ability] == 'B']
ThresholdIterator = [Ability for Ability in AbilityType if AbilityType[Ability] == 'T']
UltimateIterator = [Ability for Ability in AbilityType if AbilityType[Ability] == 'U']
TrackCooldown = {}
TrackBuff = {}
AbilityPath = []
BestRotation = []
WorstRotation = []
# --- Calculations for estimation of time remaining --- #
Permutations = math.factorial(len(MyAbilities))
Time_Remaining_Calculation = int(Permutations / 10000)
Runthrough = int(0)
# --- Tracking of highest and lowest damaging ability bars  --- #
CurrentHighest = float(0)
CurrentLowest = float('inf')

# --- Gets rotation length --- #
while True:
    try:
        if len(AoE) > 0:  # Only ask if AoE abilities are in MyAbilities
            AoEAverageTargetsHit = float(input('How many targets on average will your AoE abilities hit? '))
            if AoEAverageTargetsHit < 1:
                print("Area of effect abilities should hit at least 1 target per use.")
                continue
        break
    except:
        Error()

if AoEAverageTargetsHit > 1:
    for ability in MyAbilities:
        if ability in AoE:
            # print("Altering average damage of ability " + ability + " from " + str(AbilityDamage[ability]) + " to " + str(AbilityDamage[ability]*AoEAverageTargetsHit))
            AbilityDamage[ability] = AbilityDamage[ability] * AoEAverageTargetsHit

print('Startup Complete! Warning, the more abilities and the higher the time entered, higher wait times will be '
      'reached. A better processor will improve this speed.')
choice = input('Start Calculations? (Y/N) ').upper()
if (choice != 'Y') and (choice != 'YES'):
    sys.exit()
# --- Calculations start here --- #

Start = int(time.time())  # Record time since epoch (UTC) (in seconds)
try:  # Will keep running until Control C (or other) is pressed to end process
    for index in range(0, Permutations):
        Permutation = Get_Permutation(MyAbilities, index)
        Current = AbilityRotation(Permutation, AttackSpeed, Activate_Bleeds, Gain, Start_Adrenaline, Auto_Adrenaline,
                                  Time)
        # --- Reset data ready for next ability bar to be tested
        # and check if any better/worse bars have been found --- #
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
            # print(f'\r===== {round(float(Runthrough/Permutations) * 100, 3)}% ===== Estimated time remaining: {Get_Time(int(End_Estimation - (time.time() - Start)))}; Best found: {CurrentHighest}%' + (' ' * 22), end = '')
            print('\r===== ' + str(round(float(Runthrough / Permutations) * 100, 3)) +
                  '% ===== Estimated time remaining: ' + str(Get_Time(int(End_Estimation - (time.time() - Start)))) +
                  '; Best found: ' + str(CurrentHighest) + '%' + (' ' * 22), end='')
            Time_Remaining_Calculation -= 1
            End_Estimation = int(Time_Remaining_Calculation * (time.time() - Start))
            Start = time.time()
except KeyboardInterrupt:
    print('\nProcess terminated!')
# --- Display results --- #
print(f'\n\nHighest ability damage: {CurrentHighest}%')
print(f'Best ability bar found: {BestBar}')
print(f'{BestRotation}\n')
print(f'Lowest ability damage: {CurrentLowest}%')
print(f'Worst ability bar found: {WorstBar}')
print(WorstRotation)
input('\nPress enter to exit\n')
