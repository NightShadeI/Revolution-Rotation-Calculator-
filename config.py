"""
Cooldown times for the case where no abilities may be used.
"""
ATTACK_SPEED_COOLDOWNS = [
    {
        'name': 'Fastest',
        'time': 2.4,
    },
    {
        'name': 'Fast',
        'time': 3.0,
    },
    {
        'name': 'Average',
        'time': 3.6,
    },
    {
        'name': 'Slow',
        'time': 4.2,
    },
    {
        'name': 'Slowest',
        'time': 7.2,
    },
]

"""
The average number of targets hit when using AoE abilities
"""
AOE_AVERAGE_TARGETS_HIT = 2.5

"""
Format:
    ABILITIES = [
        {
            'name': '<ability name>',
            'cooldown': <number>, # Number of seconds that the ability goes on cooldown for
            'type': '<ultimate | threshold | basic>',
            'damage': <number>, # Set to zero for no on-hit damage
            'time': <number>, # How long an ability takes to use in seconds
            'debilitating': <True | False>, # Whether the abilities can stun or bind target
            'binds': <True | False>, # Whether the abilities can bind target,
            'punishing': <True | False>, # Whether the abilities does extra damage to targets that are stunned or bound
            'aoe': <True | False>,
            # Abilities that take longer than 1.8 seconds by default aren't affected by crit-boot. Use this to override.
            'crit_boost_affected': <True | False>,
            # Fill out these settings if it's a buffing ability
            'buff': {
                'time': <number>, # Duration of the buff in seconds
                'crit_boost': <True | False>, # Whether or not this ability buffs your crit-chance
                'multiplier': <number>, # Multiplier for boosted damage
            },
            # Fill out these settings if it's an ability that applies a bleed
            'bleed': {
                'time': <number>, # Duration of the bleed effect
                # Whether or not the first hit of this bleed is affected by damage modifying abilities 
                'first_hit_buffable': <True | False>,
            },
        }
    ]
"""
ABILITIES = [
    {
        'name': 'Asphyxiate',
        'cooldown': 20.4,
        'type': 'threshold',
        'damage': 451.2,
        'time': 5.4,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': False
    },
    {
        'name': 'Assault',
        'cooldown': 30,
        'type': 'threshold',
        'damage': 525.6,
        'time': 5.4,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': False
    },
    {
        'name': 'Backhand',
        'cooldown': 15,
        'type': 'basic',
        'damage': 60,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True
    },
    {
        'name': 'Barge',
        'cooldown': 20.4,
        'type': 'basic',
        'damage': 75,
        'time': 1.8,
        'debilitating': True,
        'binds': True,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True,
        'buff': {
            'time': 6.6,
            'crit_boost': False
        }
    },
    {
        'name': 'Berserk',
        'cooldown': 60,
        'type': 'ultimate',
        'damage': 0,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True,
        'buff': {
            'time': 19.8,
            'crit_boost': True,
            'multiplier': 2
        }
    },
    {
        'name': 'Binding Shot',
        'cooldown': 15,
        'type': 'basic',
        'damage': 60,
        'time': 1.8,
        'debilitating': True,
        'binds': True,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True,
        'buff': {
            'time': 9.6,
            'crit_boost': False
        }
    },
    {
        'name': 'Blood Tendrils',
        'cooldown': 45,
        'type': 'threshold',
        'damage': 324,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True,
        'bleed': {
            'time': 4.8,
            'first_hit_buffable': False
        }
    },
    {
        'name': 'Bombardment',
        'cooldown': 30,
        'type': 'threshold',
        'damage': 131.4,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': True,
        'crit_boost_affected': True
    },
    {
        'name': 'Chain',
        'cooldown': 10.2,
        'type': 'basic',
        'damage': 60,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': True,
        'crit_boost_affected': True
    },
    {
        'name': 'Cleave',
        'cooldown': 7.2,
        'type': 'basic',
        'damage': 112.8,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': True,
        'crit_boost_affected': True
    },
    {
        'name': 'Combust',
        'cooldown': 15,
        'type': 'basic',
        'damage': 241.2,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True,
        'bleed': {
            'time': 6,
            'first_hit_buffable': False
        }
    },
    {
        'name': 'Concentrated Blast',
        'cooldown': 5.4,
        'type': 'basic',
        'damage': 152.8,
        'time': 3.6,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': False,
        'buff': {
            'time': 5.4,
            'crit_boost': True,
            'multiplier': 1.1
        }
    },
    {
        'name': 'Corruption Blast',
        'cooldown': 15,
        'type': 'basic',
        'damage': 200,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': True,
        'crit_boost_affected': True,
        'bleed': {
            'time': 6,
            'first_hit_buffable': False
        }
    },
    {
        'name': 'Corruption Shot',
        'cooldown': 15,
        'type': 'basic',
        'damage': 200,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': True,
        'crit_boost_affected': True,
        'bleed': {
            'time': 6,
            'first_hit_buffable': False
        }
    },
    {
        'name': 'Dazing Shot',
        'cooldown': 5.4,
        'type': 'basic',
        'damage': 94.2,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True
    },
    {
        'name': 'Deadshot',
        'cooldown': 30,
        'type': 'ultimate',
        'damage': 426.13,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True,
        'bleed': {
            'time': 6,
            'first_hit_buffable': True
        }
    },
    {
        'name': 'Death\'s Swiftness',
        'cooldown': 60,
        'type': 'ultimate',
        'damage': 0,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True,
        'buff': {
            'time': 30,
            'crit_boost': True,
            'multiplier': 1.5
        }
    },
    {
        'name': 'Debilitate',
        'cooldown': 30,
        'type': 'threshold',
        'damage': 60,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True
    },
    {
        'name': 'Decimate',
        'cooldown': 7.2,
        'type': 'basic',
        'damage': 112.8,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True
    },
    {
        'name': 'Deep Impact',
        'cooldown': 15,
        'type': 'threshold',
        'damage': 120,
        'time': 1.8,
        'debilitating': True,
        'binds': True,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True,
        'buff': {
            'time': 3.6,
            'crit_boost': False
        }
    },
    {
        'name': 'Destroy',
        'cooldown': 20.4,
        'type': 'threshold',
        'damage': 451.2,
        'time': 4.2,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': False
    },
    {
        'name': 'Detonate',
        'cooldown': 30,
        'type': 'threshold',
        'damage': 225,
        'time': 3.6,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': False
    },
    {
        'name': 'Dismember',
        'cooldown': 15,
        'type': 'basic',
        'damage': 120.6,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True,
        'bleed': {
            'time': 6,
            'first_hit_buffable': False
        }
    },
    {
        'name': 'Dragon Breath',
        'cooldown': 10.2,
        'type': 'basic',
        'damage': 112.8,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': True,
        'crit_boost_affected': True
    },
    {
        'name': 'Flurry',
        'cooldown': 20.4,
        'type': 'threshold',
        'damage': 204,
        'time': 5.4,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': True,
        'crit_boost_affected': False
    },
    {
        'name': 'Forceful Backhand',
        'cooldown': 15,
        'type': 'threshold',
        'damage': 120,
        'time': 1.8,
        'debilitating': True,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True,
        'buff': {
            'time': 3.6,
            'crit_boost': False
        }
    },
    {
        'name': 'Fragmentation Shot',
        'cooldown': 15,
        'type': 'basic',
        'damage': 241.2,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True,
        'bleed': {
            'time': 6,
            'first_hit_buffable': False
        }
    },
    {
        'name': 'Frenzy',
        'cooldown': 60,
        'type': 'ultimate',
        'damage': 610,
        'time': 4.2,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': False
    },
    {
        'name': 'Fury',
        'cooldown': 5.4,
        'type': 'basic',
        'damage': 152.8,
        'time': 3.6,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': False,
        'buff': {
            'time': 5.4,
            'crit_boost': True,
            'multiplier': 1.1
        }
    },
    {
        'name': 'Havoc',
        'cooldown': 10.2,
        'type': 'basic',
        'damage': 94.2,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True
    },
    {
        'name': 'Hurricane',
        'cooldown': 20.4,
        'type': 'threshold',
        'damage': 265,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': True,
        'crit_boost_affected': True
    },
    {
        'name': 'Impact',
        'cooldown': 15,
        'type': 'basic',
        'damage': 60,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True
    },
    {
        'name': 'Kick',
        'cooldown': 15,
        'type': 'basic',
        'damage': 60,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True
    },
    {
        'name': 'Massacre',
        'cooldown': 60,
        'type': 'ultimate',
        'damage': 426.13,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True,
        'bleed': {
            'time': 6,
            'first_hit_buffable': True
        }
    },
    {
        'name': 'Metamorphosis',
        'cooldown': 60,
        'type': 'ultimate',
        'damage': 0,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True,
        'buff': {
            'time': 15,
            'crit_boost': True,
            'multiplier': 1.625
        }
    },
    {
        'name': 'Needle Strike',
        'cooldown': 5.4,
        'type': 'basic',
        'damage': 94.2,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True,
        'buff': {
            'time': 3.6,
            'crit_boost': True,
            'multiplier': 1.07
        }
    },
    {
        'name': 'Omnipower',
        'cooldown': 30,
        'type': 'ultimate',
        'damage': 300,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True
    },
    {
        'name': 'Onslaught',
        'cooldown': 120,
        'type': 'ultimate',
        'damage': 532,
        'time': 4.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': False
    },
    {
        'name': 'Overpower',
        'cooldown': 60,
        'type': 'ultimate',
        'damage': 300,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True
    },
    {
        'name': 'Piercing Shot',
        'cooldown': 3,
        'type': 'basic',
        'damage': 56.4,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': True,
        'aoe': False,
        'crit_boost_affected': True
    },
    {
        'name': 'Pulverise',
        'cooldown': 60,
        'type': 'ultimate',
        'damage': 300,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True
    },
    {
        'name': 'Punish',
        'cooldown': 3,
        'type': 'basic',
        'damage': 56.4,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': True,
        'aoe': False,
        'crit_boost_affected': True
    },
    {
        'name': 'Quake',
        'cooldown': 20.4,
        'type': 'threshold',
        'damage': 131.4,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': True,
        'crit_boost_affected': True
    },
    {
        'name': 'Rapid Fire',
        'cooldown': 20.4,
        'type': 'threshold',
        'damage': 451.2,
        'time': 5.4,
        'debilitating': True,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': False,
        'buff': {
            'time': 6,
            'crit_boost': False
        }
    },
    {
        'name': 'Ricochet',
        'cooldown': 10.2,
        'type': 'basic',
        'damage': 60,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': True,
        'crit_boost_affected': True
    },
    {
        'name': 'Sacrifice',
        'cooldown': 30,
        'type': 'basic',
        'damage': 60,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True
    },
    {
        'name': 'Sever',
        'cooldown': 15,
        'type': 'basic',
        'damage': 112.8,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True
    },
    {
        'name': 'Shadow Tendrils',
        'cooldown': 45,
        'type': 'threshold',
        'damage': 283,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True,
        'bleed': {
            'time': 1.8,
            'first_hit_buffable': False
        }
    },
    {
        'name': 'Shatter',
        'cooldown': 120,
        'type': 'threshold',
        'damage': 0,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True
    },
    {
        'name': 'Slaughter',
        'cooldown': 30,
        'type': 'threshold',
        'damage': 435,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True,
        'bleed': {
            'time': 6,
            'first_hit_buffable': False
        }
    },
    {
        'name': 'Slice',
        'cooldown': 3,
        'type': 'basic',
        'damage': 75,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': True,
        'aoe': False,
        'crit_boost_affected': True
    },
    {
        'name': 'Smash',
        'cooldown': 10.2,
        'type': 'basic',
        'damage': 94.2,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True
    },
    {
        'name': 'Smoke Tendrils',
        'cooldown': 45,
        'type': 'threshold',
        'damage': 345,
        'time': 5.4,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': False,
        'bleed': {
            'time': 5.4,
            'first_hit_buffable': False
        }
    },
    {
        'name': 'Snap Shot',
        'cooldown': 20.4,
        'type': 'threshold',
        'damage': 265,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True
    },
    {
        'name': 'Snipe',
        'cooldown': 10.2,
        'type': 'basic',
        'damage': 172,
        'time': 3.6,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True
    },
    {
        'name': 'Sonic Wave',
        'cooldown': 5.4,
        'type': 'basic',
        'damage': 94.2,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True
    },
    {
        'name': 'Stomp',
        'cooldown': 15,
        'type': 'threshold',
        'damage': 120,
        'time': 1.8,
        'debilitating': True,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True,
        'buff': {
            'time': 3.6,
            'crit_boost': False
        }
    },
    {
        'name': 'Storm Shards',
        'cooldown': 30,
        'type': 'basic',
        'damage': 0,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True
    },
    {
        'name': 'Sunshine',
        'cooldown': 60,
        'type': 'ultimate',
        'damage': 0,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True,
        'buff': {
            'time': 30,
            'crit_boost': True,
            'multiplier': 1.5
        }
    },
    {
        'name': 'Tight Bindings',
        'cooldown': 15,
        'type': 'threshold',
        'damage': 120,
        'time': 1.8,
        'debilitating': True,
        'binds': True,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True,
        'buff': {
            'time': 9.6,
            'crit_boost': False
        }
    },
    {
        'name': 'Tsunami',
        'cooldown': 60,
        'type': 'ultimate',
        'damage': 250,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': True,
        'crit_boost_affected': True
    },
    {
        'name': 'Tuska\s Wrath',
        'cooldown': 120,
        'type': 'basic',
        'damage': 5940,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True
    },
    {
        'name': 'Unload',
        'cooldown': 60,
        'type': 'ultimate',
        'damage': 610,
        'time': 4.2,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': False
    },
    {
        'name': 'Wild Magic',
        'cooldown': 20.4,
        'type': 'threshold',
        'damage': 265,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': False,
        'aoe': False,
        'crit_boost_affected': True
    },
    {
        'name': 'Wrack',
        'cooldown': 3,
        'type': 'basic',
        'damage': 56.4,
        'time': 1.8,
        'debilitating': False,
        'binds': False,
        'punishing': True,
        'aoe': False,
        'crit_boost_affected': True
    }
]
