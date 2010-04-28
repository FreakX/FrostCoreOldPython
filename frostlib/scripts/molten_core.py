# molten_core creature Scripts:
# Scriptklassen erben von der Basisscriptklasse
import basescript

class boss_baron_geddon(object): #Hier eigendlich die basisscriptclass rein^^
    def __init__(self):
        self.EMOTE_SERVICE = -1409000
        self.SPELL_INFERNO = 19695
        self.SPELL_IGNITEMANA = 19659
        self.SPELL_LIVINGBOMB = 20475
        self.SPELL_ARMAGEDDOM = 20479

        self.TIMER_INFERNO = basescript.script_timer(45,45)
        self.TIMER_IGNITEMANA = basescript.script_timer(30,30)
        self.TIMER_LIVINGBOMB = basescript.script_timer(35,35)

    def update(self):
        if self.gethealthpercent() <= 2:
            self.castinterrupt()
            self.cast(self.unit, self.SPELL_ARMAGEDDOM)
            self.say(self.EMOTE_SERVICE)
            return
        
        if self.TIMER_INFERNO.ready():
            self.cast(self.target,self.SPELL_INFERNO)
            self.TIMER_INFERNO.reset()

        if self.TIMER_IGNITEMANA.ready():
            self.cast(self.randtarget,self.SPELL_IGNITEMANA)
            self.TIMER_IGNITEMANA.reset()

        if self.TIMER_LIVINGBOMB.ready():
            self.cast(self.randtarget, self.SPELL_LIVINGBOMB)
            self.TIMER_LIVINGBOMB.reset()

        self.domeleeattack()
        
            
