# blackrock_depths creature Scripts:
# Scriptklassen erben von der Basisscriptklasse

import basescript

class boss_ambassador_flamelash(basescript.script_npc):
    def __init__(self):
        self.SPELL_FIREBLAST    = 15573

        self.TIMER_FIREBLAST     = basescript.script_timer(2,2)
        self.TIMER_SPIRIT        = basescript.script_timer(24,24)

    def reset(self):
        self.TIMER_FIREBLAST.reset(2,2)
        self.TIMER_SPIRIT.reset(24,24)


    def SummonSpirits(self, target):    ## Muss noch gemacht werden
        """
        Auszug aus ScriptDev2 vom C++ Sourcecode:
    
        45     void SummonSpirits(Unit* victim)
        46     {
        47         Rand = rand()%10;
        48         switch(urand(0, 1))
        49         {
        50             case 0: RandX -= Rand; break;
        51             case 1: RandX += Rand; break;
        52         }
        53         Rand = 0;
        54         Rand = rand()%10;
        55         switch(urand(0, 1))
        56         {
        57             case 0: RandY -= Rand; break;
        58             case 1: RandY += Rand; break;
        59         }
        60         Summoned = DoSpawnCreature(9178, RandX, RandY, 0, 0, TEMPSUMMON_TIMED_OR_CORPSE_DESPAWN, 60000);
        61         if (Summoned)
        62             ((CreatureAI*)Summoned->AI())->AttackStart(victim);
        63     }
        """
        pass

    def update(self):
        if not self.hastarget():
            return

        if self.TIMER_FIREBALST.ready():
            self.cast(self.target(), self.SPELL_FIREBLAST)
            self.TIMER_FIREBLAST.newtime(7,7)
            self.TIMER_FIREBLAST.reset()

        if self.TIMER_SPIRIT.ready():
            self.SummonSpirits(self.target())
            self.SummonSpirits(self.target())
            self.SummonSpirits(self.target())
            self.SummonSpirits(self.target())

            self.TIMER_SPIRIT.newtime(30,30)
            self.TIMER_SPIRIT.reset()

        self.domeleeattack()

class boss_anubshiah(basescript.script_npc):
    def __init__(self):
        self.SPELL_SHADOWBOLT       = 17228
        self.SPELL_CURSEOFTONGUES   = 15470
        self.SPELL_CURSEOFWAKNESS   = 17227
        self.SPELL_DEMONARMOR       = 11735
        self.SPELL_ENVELOPINGWEB    = 15471

        self.TIMER_SHADOWBOLT       = basescript.script_timer(7,7)
        self.TIMER_CURSEOFTONGUES   = basescript.script_timer(24,24)
        self.TIMER_CURSEOFWEAKNESS  = basescript.script_timer(12,12)
        self.TIMER_DEMONARMOR       = basescript.script_timer(3,3)
        self.TIMER_ENVELOPINGWEB    = basescript.script_timer(16,16)


    def reset(self):
        self.TIMER_SHADOWBOLT.reset(7,7)
        self.TIMER_CURSEOFTONGUES(24,24)
        self.TIMER_CURSEOFWEAKNESS.reset(12,12)
        self.TIMER_DEMONARMOR.reset(3,3)
        self.TIMER_ENVELOPINGWEB.reset(16,16)

    def update(self):
        if not self.hastarget():
            return

        if self.TIMER_SHADOWBOLT.ready():
            self.cast(self.target(),self.SPELL_SHADOWBOLT)
            self.TIMER_SHADOWBOLT.newtime(7,7)
            self.TIMER_SHADOWBOLT.reset()

        if self.TIMER_CURSEOFTONGUES.ready():
            target = self.randtarget()
            if target:
                self.cast(target, self.SPELL_SPELL_CURSEOFTONGUES)
                self.TIMER_CURSEOFTONGUES.newtime(18,18)
                self.TIMER_CURSEOFTONGUES.reset()

        if self.TIMER_CURSEOFWEAKNESS.ready():
            self.cast(self.target(), self.SPELL_CURSEOFWEAKNESS)
            self.TIMER_CURSEOFWEAKNESS.newtime(45,45)
            self.TIMER_CURSEOFWEAKNESS.reset()

        if self.TIMER_DEMONARMOR.ready():
            self.cast(self.guid(), self.SPELL_DOMONARMOR)
            self.TIMER_DEMONARMOR.newtime(300,300)
            self.TIMER_DEMONARMOR.reset()
            
        if self.TIMER_ENVELOPINGWEB.ready():
            target = self.randtarget()
            if target:
                self.cast(target, self.SPELL_ENVELOPINGWEB)
                self.TIMER_ENVELOPINGWEB.newtime(12,12)
                self.TIMER_ENVELOPINGWEB.reset()

        self.fomeleeattack()
        
        
