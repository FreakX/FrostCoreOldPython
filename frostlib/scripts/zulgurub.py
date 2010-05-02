# zulgurub creature Scripts:
# Scriptklassen erben von der Basisscriptklasse
import basescript

class boss_arlokk(basescript.script_npc):
    def __init__(self):
        self.mindmg = 100
        self.maxdmg = 200
        self.SAY_AGGRO = -1309011
        self.SAY_FEAST_PANTHER = -1309012
        self.SAY_DEATH = -1309013

        self.SPELL_SHADOWWORDPAIN = 23952
        self.SPELL_GOUGE = 24698
        self.SPELL_MARK = 24210
        self.SPELL_CLEAVE = 26350
        self.SPELL_PANTHER_TRANSFORM = 24190

        self.MODEL_ID_NORMAL = 15218
        self.MODEL_ID_PANTHER = 15215
        self.MODEL_ID_BLANK = 11686

        self.NPC_ZULIAN_PROWLER = 15101

        self.TIMER_SHADOWWORDPAIN = basescript.script_timer(8,8)
        self.TIMER_GOUGE = basescript.script_timer(14,14)
        self.TIMER_MARK = basescript.script_timer(35,35)
        self.TIMER_CLEAVE = basescript.script_timer(4,4)
        self.TIMER_VANISH = basescript.script_timer(60,60)
        self.TIMER_VISIBLE = basescript.script_timer(6,6)

        self.TIMER_SUMMON = basescript.script_timer(5,5)
        self.SUMMON_COUNT = 0

        self.IS_PHASE_TWO = False
        self.IS_VANISHED = False

        self.MARKED_GUID = 0

    def reset(self):
        self.TIMER_SHADOWWORDPAIN.reset(8,8)
        self.TIMER_GOUGE.reset(14,14)
        self.TIMER_MARK.reset(35,35)
        self.TIMER_CLEAVE.reset(4,4)
        self.TIMER_VANISH.reset(60,60)
        self.TIMER_VISIBLE.reset(6,6)

        self.TIMER_SUMMON.reset(5,5)

        self.setdisplayid(self.MODEL_ID_NORMAL)
        self.selectable()

    def update(self):
        if self.IS_PHASE_TWO == False:
            if self.TIMER_SHADOWWORDPAIN.ready():
                self.cast(self.target(), self.SPELL_SHADOWWORDPAIN)
                self.TIMER_SHADOWWORDPAIN.newtime(15,15)
                self.TIMER_SHADOWWORDPAIN.reset()

            if self.TIMER_MARK.ready():
                helpvar = self.randtarget()
                self.cast(helpvar, self.SPELL_MARK)
                self.MARKED_GUID = helpvar
                self.TIMER_MARK.newtime(15,15)
                self.TIMER_MARK.reset()

        else:
            if self.TIMER_CLEAVE.ready():
                self.cast(self.target(), self.SPELL_CLEAVE)
                self.TIMER_CLEAVE.newtime(16,16)
                self.TIMER_CLEAVE.reset()

            if self.TIMER_GOUGE.ready():
                self.cast(self.target(), self.SPELL_GOUGE)
                self.TIMER_GOUGE.newtime(17,27)
                self.TIMER_GOUGE.reset()

        if self.SUMMON_COUNT <= 30:
            if self.TIMER_SUMMON.ready():
                self.summon_npc(self.NPC_ZULIAN_PROWLER)
                self.TIMER_SUMMON.newtime(5,5)
                self.TIMER_SUMMON.reset()
        if self.TIMER_VANISH.ready():
            self.setdisplayid(self.MODEL_ID_BLANK)
            self.unselectable()

            self.attackstop()
            
            self.IS_VANISHED = True

            self.TIMER_VANISH.newtime(45,45)
            self.TIMER_VANISH.reset()
            self.TIMER_VISIBLE.reset()

        if self.IS_VANISHED:
            if self.TIMER_VISIBLE.ready():
                self.setdisplayid(self.MODEL_ID_PANTHER)
                self.selectable()
                self.set("BASE_ATTACK", "MINDAMAGE", self.mindmg + ((self.mindmg/100) * 35))
                self.set("BASE_ATTACK", "MAXDAMAGE", self.maxdmg + ((self.maxdmg/100) * 35))
                self.set("BASE_ATTACK", "TYPE", "PHYSICAL")

                self.settarget(self.randtarget)

                self.IS_PHASE_TWO = True
                self.IS_VANISHED = False

        self.domeleeattack()

class boss_gahzranka(basescript.script_npc):
    def __init__(self):
        self.SPELL_FROSTBREATH = 16099
        self.SPELL_MASSIVEGEYSER = 22421
        self.SPELL_SLAM = 24326

        self.TIMER_FROSTBREATH = basescript.script_timer(8,8)
        self.TIMER_MASSIVEGEYSER = basescript.script_timer(25,25)
        self.TIMER_SLAM = basescript.script_timer(17,17)

    def reset(self):
        self.TIMER_FROSTBREATH.reset(8,8)
        self.TIMER_MASSIVEGEYSER.reset(25,25)
        self.TIMER_SLAM.reset(17,17)

    def update(self):
        if self.TIMER_FROSTBREATH.ready():
            self.cast(self.target(), self.SPELL_FROSTBREATH)
            self.TIMER_FROSTBREATH.newtime(7,11)
            self.TIMER_FROSTBREATH.reset()

        if self.TIMER_MASSIVEGEYSER.ready():
            self.cast(self.target(), self.SPELL_MASSIVEGEYSER)
            self.TIMER_MASSIVEGEYSER.newtime(22,32)
            self.TIMER_MASSIVEGEYSER.reset()

        if self.TIMER_SLAM.ready():
            self.cast(self.target(), self.SPELL_SLAM)
            self.TIMER_SLAM.newtime(12,20)
            self.TIMER_SLAM.reset()

        self.domeleeattack()

class boss_grilek(basescript.script_npc):
    def __init__(self):
        self.SPELL_AVARTAR = 24646
        self.SPELL_GROUNDTREMOR = 6524
        
        self.TIMER_AVARTAR = basescript.script_timer(15,25)
        self.TIMER_GROUNDTREMOR = basescript.script_timer(8,16)

    def reset(self):
        self.TIMER_AVARTAR.reset(15,25)
        self.TIMER_GROUNDTREMOR.reset(8,16)

    def update(self):
        if self.TIMER_AVARTAR.ready():
            self.cast(self.guid(), self.SPELL_AVARTAR)

            self.attack(self.randtarget())

            self.TIMER_AVARTAR.newtime(25,35)
            self.TIMER_AVARTAR.reset()

        if self.TIMER_GROUNDTREMOR.ready():
            self.cast(self.target(), self.SPELL_GROUNDTREMOR)

            self.TIMER_GROUNDTREMOR.newtime(12,16)
            self.TIMER_GROUNDTREMOR.reset()

        self.domeleeattack()

class boss_hakkar(basescript.script_npc):
       
    def __init__(self):
        self.SAY_AGGRO = -1309020
        self.SAY_FLEEING = -1309021
        self.SAY_MINION_DESTROY = -1309022
        self.SAY_PROTECT_ALTAR = -1309023
    
        self.SPELL_BLOODSIPHON = 24322
        self.SPELL_CORRUPTEDBLOOD = 24328
        self.SPELL_CAUSEINSANITY = 24327
        self.SPELL_WILLOFHAKKAR = 24178
        self.SPELL_ENRAGE = 24318
        self.SPELL_ASPECTOFJEKLIK = 24687
        self.SPELL_ASPECTOFVENOXIS = 24688
        self.SPELL_ASPECTOFMARLI = 24686
        self.SPELL_ASPECTOFTHEKAL = 24689
        self.SPELL_ASPECTOFARLOKK = 24690
        
        self.TIMER_BLOODSIPHON = basescript.script_timer(90,90)
        self.TIMER_CORRUPTEDBLOOD = basescript.script_timer(25,25)
        self.TIMER_CAUSEINSANITY = basescript.script_timer(17,17)
        self.TIMER_WILLOFHAKKAR = basescript.script_timer(17,17)
        self.TIMER_ENRAGE = basescript.script_timer(60,60)

        self.STATUS_JEKLIK = False
        self.STATUS_VENOXIS = False
        self.STATUS_MARLI = False
        self.STATUS_THEKAL = False
        self.STATUS_ARLOKK = False
        
        self.TIMER_CHECKJEKLIK = basescript.script_timer(1,1)
        self.TIMER_CHECKVENOXIS = basescript.script_timer(2,2)
        self.TIMER_CHECKMARLI = basescript.script_timer(3,3)
        self.TIMER_CHECKTHEKAL = basescript.script_timer(4,4)
        self.TIMER_CHECKARLOKK = basescript.script_timer(5,5)
        
        self.TIMER_ASPECTOFJEKLIK = basescript.script_timer(4,4)
        self.TIMER_ASPECTOFVENOXIS = basescript.script_timer(7,7)
        self.TIMER_ASPECTOFMARLI = basescript.script_timer(12,12)
        self.TIMER_ASPECTOFTHEKAL = basescript.script_timer(8,8)
        self.TIMER_ASPECTOFARLOKK = basescript.script_timer(18,18)

        self.ENRAGED = False

    def reset(self):
        self.TIMER_BLOODSIPHON.reset(90,90)
        self.TIMER_CORRUPTEDBLOOD.reset(25,25)
        self.TIMER_CAUSEINSANITY.reset(17,17)
        self.TIMER_WILLOFHAKKAR.reset(17,17)
        self.TIMER_ENRAGE.reset(60,60)
        
        self.TIMER_CHECKJEKLIK.reset(1,1)
        self.TIMER_CHECKVENOXIS.reset(2,2)
        self.TIMER_CHECKMARLI.reset(3,3)
        self.TIMER_CHECKTHEKAL.reset(4,4)
        self.TIMER_CHECKARLOKK.reset(5,5)
        
        self.TIMER_ASPECTOFJEKLIK.reset(4,4)
        self.TIMER_ASPECTOFVENOXIS.reset(7,7)
        self.TIMER_ASPECTOFMARLI.reset(12,12)
        self.TIMER_ASPECTOFTHEKAL.reset(8,8)
        self.TIMER_ASPECTOFARLOKK.reset(18,18)

    def update(self):
        if self.TIMER_BLOODSIPHON.ready():
            self.cast(self.target(), self.SPELL_BLOODSIPHON)

            self.TIMER_BLOODSIPHON.reset()

        if self.TIMER_CORRUPTEDBLOOD.ready():
            self.cast(self.target(), self.SPELL_CORRUPTEDBLOOD)

            self.TIMER_CORRUPTEDBLOOD.newtime(30,45)
            self.TIMER_CORRUPTEDBLOOD.reset()

        if self.TIMER_CAUSEINSANITY.ready():
            self.cast(self.randtarget(), self.SPELL_CAUSEINSANITY)

            self.TIMER_CAUSEINSANITY.newtime(35, 43)
            self.TIMER_CAUSEINSANITY.reset()

        if self.TIMER_WILLOFHAKKAR.ready():
            self.cast(self.randtarget(), self.SPELL_WILLOFHAKKAR)

            self.TIMER_WILLOFHAKKAR.newtime(25,35)
            self.TIMER_WILLOFHAKKAR.reset()

        if self.TIMER_CHECKJEKLIK.ready():
            if self.STATUS_JEKLIK != True:
                if self.TIMER_ASPECTOFJEKLIK.ready():
                    self.cast(self.target(), self.SPELL_ASPECTOFJEKLIK)
                    
                    self.TIMER_ASPECTOFJEKLIK.newtime(10,14)
                    self.TIMER_ASPECTOFJEKLIK.reset()

            self.TIMER_CHECKJEKLIK.reset()

        if self.TIMER_CHECKVENOXIS.ready():
            if self.STATUS_VENOXIS != True:
                if self.TIMER_ASPECTOFVENOXIS.ready():
                    self.cast(self.target(), self.SPELL_ASPECTOFVENOXIS)
                    
                    self.TIMER_ASPECTOFVENOXIS.newtime(8,8)
                    self.TIMER_ASPECTOFVENOXIS.reset()
                    
            self.TIMER_CHECKVENOXIS.newtime(1,1)
            self.TIMER_CHECKVENOXIS.reset()

        if self.TIMER_CHECKMARLI.ready():
            if self.STATUS_MARLI != True:
                if self.TIMER_ASPECTOFMARLI.ready():
                    self.cast(self.target(), self.SPELL_ASPECTOFMARLI)
                    
                    self.TIMER_ASPECTOFMARLI.newtime(10,10)
                    self.TIMER_ASPECTOFMARLI.reset()
                    
            self.TIMER_CHECKMARLI.newtime(1,1)
            self.TIMER_CHECKMARLI.reset()

        if self.TIMER_CHECKTHEKAL.ready():
            if self.STATUS_THEKAL != True:
                if self.TIMER_ASPECTOFTHEKAL.ready():
                    self.cast(self.target(), self.SPELL_ASPECTOFTHEKAL)
                    
                    self.TIMER_ASPECTOFTHEKAL.newtime(15,15)
                    self.TIMER_ASPECTOFTHEKAL.reset()
                    
            self.TIMER_CHECKTHEKAL.newtime(1,1)
            self.TIMER_CHECKTHEKAL.reset()

        if self.TIMER_CHECKARLOKK.ready():
            if self.STATUS_ARLOKK != True:
                if self.TIMER_ASPECTOFARLOKK.ready():
                    self.cast(self.target(), self.SPELL_ASPECTOFARLOKK)
                    
                    self.TIMER_ASPECTOFARLOKK.newtime(10,15)
                    self.TIMER_ASPECTOFARLOKK.reset()
                    
            self.TIMER_CHECKARLOKK.newtime(1,1)
            self.TIMER_CHECKARLOKK.reset()

        self.domeleeattack()

        
            
        

        
        
        
    
                
        
