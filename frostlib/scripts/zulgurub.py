# zulgurub creature Scripts:
# Scriptklassen erben von der Basisscriptklasse
import basescript

class boss_arlokk(basescript.script_npc):
    def __init__(self):
        
        self.SAY_AGGRO = -1309011
        self.SAY_FEAST_PANTHER = -1309012
        self.SAY_DEATH = -1309013

        self.SPELL_SHADOWWORDPAIN = 23952
        self.SPELL_GOUGE = 24698
        self.SPELL_MARK = 24210
        self.SPELL_CLEAVE = 26350
        self.SPELL_PANTHER_TRANSFORM = 24190

        self.MODEL_ID_NORMAL = 15218
        self.MODEL_ID_PHANTER = 15215
        self.MODEL_ID_BLANK = 11686

        self.NPC_ZULIAN_PROWLER = 15101

        self.TIMER_SHADOWWORDPAIN = basescript.script_timer(8,8)
        self.TIMER_GOUGE = basescript.script_timer(14,14)
        self.TIMER_MARK = basescript.script_timer(35,35)
        self.TIMER_CLEAVE = basescript.script_timer(4,4)
        self.TIMER_VANISH = basescript.script_timer(60,60)
        self.TIMER_VISIBLE = basecript.script_timer(6,6)

        self.TIMER_SUMMON = basescript.script_timer(5,5)
        self.SUMMON_COUNT = 0

        self.IS_PHASE_TWO = false
        self.IS_VANISHED = false

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
            if self.TIMER_SHADOWWORPAIN.ready():
                self.cast(self.target(), self.SPELL_SHADOWWORDPAIN)
                self.TIMER_SHADOWWORDPAIN.newtime(15,15)
                self.TIMER_SHADOWWORDPAIN.reset()

            if self.TIMER_MARK.ready():
                helpvar = self.randtarget()
                self.cast(helpvar), self.SPELL_MARK)
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
                
        
