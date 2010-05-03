# magister_terace creature Scripts:
# Scriptklassen erben von der Basisscriptklasse
import basescript

class boss_felblood_kaelthas(basescript.script_npc):
    def __init__(self):
        self.SAY_AGGRO = -1585023
        self.SAY_PHOENIX = -1585024
        self.SAY_FLAMESTRIKE = -1585025
        self.SAY_GRAVITY_LAPSE = -1585026
        self.SAY_TIRED = -1585027
        self.SAY_RECAST_GRAVITY = -1585028
        self.SAY_DEATH = -1585029

        #**** Spells ***#

        # Phase 1 spells

        self.SPELL_FIREBALL_NORMAL      = 44189
        self.SPELL_FIREBALL_HEROIC      = 46164
        
        self.SPELL_PHOENIX              = 44194
        self.SPELL_PHOENIX              = 44197

        self.SPELL_FLAME_STRIKE_DUMMY   = 44191
        self.SPELL_FLAME_STRIKE         = 44192

        self.SPELL_SHOCK_BARRIER        = 46165
        self.SPELL_PYROBLAST            = 36819

        # Phase 2 spells

        self.SPELL_GRAVITY_LAPSE_INITIAL    = 44224
        self.SPELL_GRAVITY_LAPSE_CHANNEL    = 44251
        self.SPELL_TELEPORT_CENTER          = 44218
        self.SPELL_GRAVITY_LAPSE_FLY        = 44227
        self.SPELL_GRAVITY_LAPSE_DOT        = 44226
        self.SPELL_ARCANE_SPHERE_PASSIVE    = 44263
        self.SPELL_POWER_FEEDBACK           = 44233

        # Creatures

        self.NPC_FLAME_STRIKE_TRIGGER       = 24666
        self.CREATURE_PHOENIX               = 24674
        self.CREATURE_PHOENIX_EGG           = 24675
        self.CREATURE_ARCANE_SPHERE         = 24708

        self.LOCATIONS = [
            (148.744659, 181.377426),
            (140.823883, 195.403046),
            (156.574188, 195.650482)
            ]
        self.LOCATION_Z = -16.727455

        self.TIMER_FIREBALL                 = basescript.script_timer(4,4)
        self.TIMER_PHOENIX                  = basescript.script_timer(10,10)
        self.TIMER_FLAME_STRIKE             = basescript.script_timer(25,25)
        self.TIMER_COMBAT_PULSE             = basescript.script_timer(10,10)
        self.TIMER_PYROBLAST                = basescript.script_timer(60,60)

        self.TIMER_GRAVITY_LAPSE            = basescript.script_timer(20,20)
        self.GRAVITY_LAPSE_PHASE            = 0

        self.FIRST_GRAVITY_LAPSE            = True
        self.HAS_TAUNTED                    = False

        self.PHASE                          = 0

    def reset(self):
        self.TIMER_FIREBALL.reset(4,4)
        self.TIMER_PHOENIX.reset(10,10)
        self.TIMER_FLAME_STRIKE.reset(25,25)
        self.TIMER_COMBAT_PULSE.reset(10,10)
        self.TIMER_PYROBLAST.reset(60,60)
        self.TIMER_GRAVITY_LAPSE.reset(20,20)

    def update(self):
        if self.PHASE == 1
            if self.instance.mode == "heroic":
                if self.TIMER_PYROBLAST.ready():
                    self.cast(self.guid(), self.SPELL_SHOCK_BARRIER)
                    self.cast(self.target(), self.SPELL_PYROBLAST)
                    self.TIMER_PYROBLAST.newtime(60,60)
                    self.TIMER_PYROBLAST.reset()
            if self.TIMER_FIREBALL.ready():
                if self.instance.mode == "heroic":
                    self.cast(self.target(), self.SPELL_FIREBALL_HEROIC)
                if self.instance.mode == "normal":
                    self.cast(self.target(), self.SPELL_FIREBALL_NORMAL)
                self.TIMER_FIREBALL.newtime(2,6)
                self.TIMER_FIREBALL.reset()

            if self.TIMER_PHOENIX.ready():
                target = self.randtarget():
                randompos = random.randint(0,2)
                posx = self.LOCATIONS[randompos][0]
                posy = self.LOCATIONS[randompos][1]

                spawned_cre = self.spawncreature(self.CREATURE_PHOENIX, posx, posy, self.LOCATION_Z)
                spawned_cre.attack(target)

                self.say(SAY_PHOENIX)

                self.TIMER_PHOENIX.newtime(60,60)
                self.TIMER_PHOENIX.reset()

            if self.TIMER_FLAME_STRIKER.ready():
                ptarget = self.randtarget()
                if ptarget:
                    self.cast(ptarget, self.SPELL_FLAME_STRIKE)
                    self.say(self.SAY_FLAMESTRIKE)
                self.TIMER_FLAME_STRIKE.newtime(15,25)
                self.TIMER_FLAME_STRIKE.reset()

            if self.gethealthpercent() < 50:
                self.TIMER_GRAVITY_LAPSE.newtime(0,0)
                self.GRAVITY_LAPSE_PHASE = 0
                self.TIMER_GRAVITY_LAPSE.reset()
                self.PHASE = 1

            self.domeleeattack()
        if self.PHASE == 1:
            if self.TIMER_GRAVITY_LAPSE.ready():
                if self.GRAVITY_LAPSE_PHASE == 0:           # Gravity Lapse Phase 0
                    if self.FIRST_GRAVITY_LAPSE:
                        self.say(self.SAY_GRAVITY_LAPSE)
                        self.FIRST_GRAVITY_LAPSE == False
                    else:
                        self.say(self.SAY_RECAST_GRAVITY)

                    self.cast(self.guid(), self.SPELL_GRAVITY_LAPSE_INITIAL)
                    self.TIMER_GRAVITY_LAPSE.newtime(2,2)
                    self.TIMER_GRAVITY_LAPSE.reset()
                    self.GRAVITY_LAPSE_PHASE = 1
                    
                elif self.GRAVITY_LAPSE_PHASE == 1:         # Gravity Lapse Phase 1
                    self.TeleportPlayerstoSelf() # Muss noch implementiert werden
                    self.TIMER_GRAVITY_LAPSE.newtime(1,1)
                    self.TIMER_GRAVITY_LAPSE.reset()
                    self.GRAVITY_LAPSE_PHASE = 2
                    
                elif self.GRAVITY_LAPSE_PHASE == 2:         # Gravity Lapse Phase 2
                    self.CastGravityLapseKnockUp() # Muss noch implementiert werden
                    self.TIMER_GRAVITY_LAPSE.newtime(1,1)
                    self.TIMER_GRAVITY_LAPSE.reset()
                    self.GRAVITY_LAPSE_PHASE = 3
                    
                elif self.GRAVITY_LAPSE_PHASE == 3:         # Gravity Lapse Phase 3
                    self.CastGravityLapseFly() # Muss noch implementiert werden
                    self.TIMER_GRAVITY_LAPSE.newtime(30,30)
                    self.TIMER_GRAVITY_LAPSE.reset()
                    self.GRAVITY_LAPSE_PHASE = 4

                    for x in range(0, 3):
                        target = self.randtarget()
                        
                        orb = self.spawncreature(self.CREATURE_ARCANE_SPHERE, self.posx(), self.posy(), self.posz())

                        if target and orb:
                            ob.attack(target)

                        self.cast(self.guid(), self.SPELLGRAVITY_LAPSECHANNEL)

                elif self.GRAVITY_LAPSE_PHASE == 4:         # Gravity Lapse Phase 4
                    self.say(self.SAY_TIRED)
                    self.cast(self.guid(), self.SPELL_POWER_FEEDBACK)
                    self.RemoveGravityLapse() # Muss noch implementiert werden
                    self.TIMER_GRAVITY_LAPSE.newtime(10,10)
                    self.TIMER_GRAVITY_LAPSE.reset()
                    self.GRAVITY_LAPSE_PHASE = 0
                    
                    

                
                    
                    
            
        
