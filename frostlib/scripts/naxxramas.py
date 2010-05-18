# naxxramas creature Scripts:
# Scriptklassen erben von der Basisscriptklasse

import basescript

class boss_anubrekhan(basescript.script_npc):
    def __init__(self):
        self.SAY_GREET          = -1533000
        self.SAY_AGGRO1         = -1533001
        self.SAY_AGGRO2              = -1533002
        self.SAY_AGGRO3              = -1533003
        self.SAY_TAUNT1              = -1533004
        self.SAY_TAUNT2              = -1533005
        self.SAY_TAUNT3              = -1533006
        self.SAY_TAUNT4              = -1533007
        self.SAY_SLAY                = -1533008


        self.SPELL_IMPALE                = 28783                    #May be wrong spell id. Causes more dmg than I expect
        self.SPELL_IMPALE_H              = 56090
        
        self.SPELL_LOCUSTSWARM           = 28785                    #This is a self buff that triggers the dmg debuff
        self.SPELL_LOCUSTSWARM_H         = 54021
        
        self.SPELL_SUMMONGUARD           = 29508

        self.SPELL_SELF_SPAWN_5          = 29105                   #This spawns 5 corpse scarabs ontop of us (most likely the pPlayer casts this on death)
        self.SPELL_SELF_SPAWN_10         = 28864
        
        self.SPELL_ACID_SPIT             = 28969
        self.SPELL_ACID_SPIT_H           = 56098
        
        self.SPELL_CLEAVE                = 40504
        self.SPELL_FRENZY                = 8269
        self.NPC_CRYPT_GUARD             = 16573
        self.NPC_SMALL_SPAWN             = 16698

        self.IS_REGULAR_MODE            = True
        
        self.TIMER_IPMALE = basescript.script_timer(15,15)
        self.TIMER_LOCUS_SWARM = basescript.script_timer(80,120)
        self.TIMER_SUMMON = basescript.script_timer(25,25)

    def reset():
        self.TIMER_IPMALE.reset(15,15)
        self.TIMER_LOCUS_SWARM.reset(80,120)
        self.TIMER_SUMMON.reset(25,25)

    ## TODO: def update(self):
        
        

        
