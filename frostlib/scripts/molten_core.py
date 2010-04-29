# molten_core creature Scripts:
# Scriptklassen erben von der Basisscriptklasse
import basescript

class boss_baron_geddon(basescript.script_npc):
    def __init__(self):
        self.EMOTE_SERVICE = -1409000
        self.SPELL_INFERNO = 19695
        self.SPELL_IGNITEMANA = 19659
        self.SPELL_LIVINGBOMB = 20475
        self.SPELL_ARMAGEDDOM = 20479

        self.TIMER_INFERNO = basescript.script_timer(45,45)
        self.TIMER_IGNITEMANA = basescript.script_timer(30,30)
        self.TIMER_LIVINGBOMB = basescript.script_timer(35,35)
        
    def reset(self):
        self.TIMER_INFERNO.reset(45,45)
        self.TIMER_IGNITEMANA.reset(30,30)
        self.TIMER_LIVINGBOMB.reset(35,35)
        
    def update(self):
        if self.gethealthpercent() <= 2:
            self.castinterrupt()
            self.cast(self.guid, self.SPELL_ARMAGEDDOM)
            self.say(self.EMOTE_SERVICE)
            return
        
        if self.TIMER_INFERNO.ready():
            self.cast(self.guid,self.SPELL_INFERNO)
            self.TIMER_INFERNO.reset()

        if self.TIMER_IGNITEMANA.ready():
            self.cast(self.randtarget(),self.SPELL_IGNITEMANA)
            self.TIMER_IGNITEMANA.reset()

        if self.TIMER_LIVINGBOMB.ready():
            self.cast(self.randtarget(), self.SPELL_LIVINGBOMB)
            self.TIMER_LIVINGBOMB.reset()

        self.domeleeattack()

class boss_garr(basescript.script_npc):
    def __init__(self):
        self.SPELL_ANTIMAGICPULSE = 19492
        self.SPELL_MAGMASHACKLES  = 19496
        self.SPELL_ENRAGE         = 19516
        #self.SPELL_ERUPTION       = 19497
        #self.SPELL_IMMOLATE       = 20294
        self.add_npc_id = 00000  # ? Feueranbeter von Garr
        self.add = []

        self.TIMER_ANTIMAGICPULSE = basescript.script_timer(25,25)
        self.TIMER_MAGMASHACKLES  = basescript.script_timer(15,15)
        self.TIMER_CHECKADDS      = basescript.script_timer(2,2)

    def reset(self):
        self.TIMER_ANTIMAGICPULSE.reset(25,25)
        self.TIMER_MAGMASHACKLES.reset(15,15)
        self.TIMER_CHECKADDS.reset(2,2)
        while len(self.add) < 8:
            npc = self.summon_npc(self.add_npc_id)
            self.add.append(npc)
            
    def update(self):
        if self.gethealthpercent() < 20:
            self.cast(self.guid, self.SPELL_ENRAGE)
            return
        
        if self.TIMER_ANTIMAGICPULSE.ready():
            self.cast(self.guid, self.SPELL_ANTIMAGICPULSE)
            self.TIMER_ANTIMAGICPULSE.newtime(10,15)
            self.TIMER_ANTIMAGICPULSE.reset()

            
        if self.TIMER_MAGMASHACKLES.ready():
            self.cast(self.guid, self.SPELL_MAGMASHACKLES)
            self.TIMER_MAGMASHACKLES.newtime(8,12)
            self.TIMER_MAGMASHACKLES.reset()

        if self.TIMER_CHECKADDS.ready():
            while len(self.add) < 8:
                npc = self.summon_npc(self.add_npc_id)
                self.add.append(npc)

        self.domeleeattack()

class boss_lucifron(basescript.script_npc):
    def __init__(self):
        self.SPELL_IMPENDINGDOOM = 19702
        self.SPELL_LUCIFRONCURSE = 19703
        self.SPELL_SHADOWSHOCK   = 20603

        self.TIMER_IMPENDINGDOOM = basescript.script_timer(10,10)
        self.TIMER_LUCIFRONCURSE = basescript.script_timer(20,20)
        self.TIMER_SHADOWSHOCK   = basescript.script_timer(6,6)

    def reset(self):
        self.TIMER_IMPENDINGDOOM.reset(10,10)
        self.TIMER_LUCIFRONCURSE.reset(20,20)
        self.TIMER_SHADOWSCHOCK.reset(6,6)

    def update(self):
        if self.TIMER_IMPENDINGDOOM.ready():
            self.cast(self.target(), self.SPELL_IMPENDINGDOOM)
            self.TIMER_IMPENDINGDOOM.newtime(20,20)
            self.TIMER_IMPENDINGDOOM.reset()
            
        if self.TIMER_LUCIFRONCURSE.ready():
            self.cast(self.target(), self.SPELL_LUCIFRONCURSE)
            self.TIMER_LUCIFRONCURSE.newtime(15,15)
            self.TIMER_LUCIFRONCURSE.reset()

        if self.TIMER_SHADOWSHOCK.ready():
            self.cast(self.target(), self.SPELL_SHADOWSHOCK)
            self.TIMER_SHADOWSHOCK.reset()

        self.domeleeattack()

class boss_magmadar(basescript.script_npc):
    def __init__(self):
        self.EMOTE_GENERIC_FRENZY_KILL = -10000001

        self.SPELL_FRENZY   = 19451
        self.SPELL_MAGMASPIT= 19449
        self.SPELL_PANIC    = 19408
        self.SPELL_LAVABOMB = 19411
        #self.SPELL_LAVABOMB_ALT = 19428  # From Mangos, i dont know why they use it

        self.TIMER_FRENZY = basescript.script_timer(30,30)
        self.TIMER_PANIC  = basescript.script_timer(20,20)
        self.TIMER_LAVABOMB = basescript.script_timer(12,12)

    def reset(self):
        self.TIMER_FRENZY.reset(30,30)
        self.TIMER_PANIC.reset(20,20)
        self.TIMER_LAVABOMB.reset(12,12)
        self.cast(self.guid, self.SPELL_MAGMASPIT)

    def update(self):
        if self.TIMER_FRENZY.ready():
            self.say(self.EMOTE_GENERIC_FRENZY_KILL)
            self.cast(self.guid, self.SPELL_FRENZY)
            self.TIMER_FRENZY.newtime(15,15)
            self.TIMER_FRENZY.reset()

        if self.TIMER_PANIC.ready():
            self.cast(self.target(), self.SPELL_PANIC)
            self.TIMER_PANIC.newtime(35,35)
            self.TIMER_PANIC.reset()

        if self.TIMER_LAVABOMB.ready():
            self.cast(self.randtarget(), self.SPELL_LAVABOMB)
            self.TIMER_LAVABOMB.reset()

        self.domeleeattack()

class boss_gehennas(basescript.script_npc): # Es fehlen noch die adds
    def __init__(self):
        self.SPELL_SHADOWBOLT = 19728
        self.SPELL_RAINOFFIRE = 19717
        self.SPELL_GEHANNASCURSE = 19716

        self.TIMER_SHADOWBOLT = basescript.script_timer(6,6)
        self.TIMER_RAINOFFIRE = basescript.script_timer(10,10)
        self.TIMER_GEHANNASCURSE = basescript.script_timer(12,12)

    def reset(self):
        self.TIMER_SHADOWBOLT.reset(6,6)
        self.TIMER_RAINOFFIRE.reset(10,10)
        self.TIMER_GEHANNASCURSE.reset(12,12)

    def update(self):
        if self.TIMER_SHADOWBOLT.ready():
            self.cast(self.randtarget(), self.SPELL_SHADOWBOLT)
            self.TIMER_SHADOWBOLT.newtime(7,7)
            self.TIMER_SHADOWBOLT.reset()

        if self.TIMER_RAINOFFIRE.ready():
            self.cast(self.randtarget(), self.SPELL_RAINOFFIRE)
            self.TIMER_RAINOFFIRE.newtime(4,12)
            self.TIMER_RAINOFFIRE.reset()

        if self.TIMER_GEHANNASCURSE.ready():
            self.cast(self.target(), self.SPELL_GEHANNASCURSE)
            self.TIMER_GEHANNASCURSE.newtime(22,30)
            self.TIMER_GEHANNASCURSE.reset()


        self.domeleeattack()

class boss_golemagg(basescript.script_npc):
    def __init__(self):
        self.SPELL_MAGMASPLASH = 13879
        self.SPELL_PYROBLAST   = 20228
        self.SPELL_EARTHQUAKE  = 19798
        self.SPELL_ENRAGE      = 19953
        self.SPELL_GOLEMAGG_TRUST = 20553

        self.EMOTE_LOWHP = -1409002
        self.SPELL_MANGLE = 19820

        self.TIMER_PYROBLAST = basescript.script_timer(7,7)
        self.TIMER_EARTHQUAKE = basescript.script_timer(3,3)
        self.TIMER_BUFF = basescript.script_timer(2.5,2.5)
        self.ENRAGED = False

    def reset(self):
        self.TIMER_PYROBLAST.reset(7,7)
        self.TIMER_EARTHQUAKE.reset(3,3)
        self.TIMER_BUFF.reset(2.5,2.5)
        self.ENRAGED = False
        self.cast(self.guid, self.SPELL_MAGMASPLASH)

    def update(self):

        if self.TIMER_PYROBLAST.ready():
            self.cast(self.randtarget(),self.SPELL_PYROBLAST)
            self.TIMER_PYROBLAST.reset()

        if self.ENRAGED == False and self.gethealthpercent < 10:
            self.cast(self.guid, self.SPELL_ENRAGE)
            self.ENRAGED = True

        if self.ENRAGED == True:
            if self.TIMER_EARTHQUAKE.ready():
                self.cast(self.target, self.SPELL_EARTHQUAKE)
                self.TIMER_EARTHQUAKE.reset()

        if self.TIMER_BUFF.ready():
            self.cast(self.target, self.SPELL_GOLEMAGG_TRUST)
            self.TIMER_BUFF.reset()

        self.domeleeattack()
            
        
          
            
        
        
        
            
