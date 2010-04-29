## Basic CreatureScript:
import time
import random
class script_npc(object):
    def cast(self, target, spellid):
        print str(time.strftime("%M:%S")) + " Casting Spellid: " + str(spellid) + " on " + str(target)
    def target(self):
        return "Daniel"
    def randtarget(self):
        print str(time.strftime("%M:%S")) +  "Search random Target"
    def domeleeattack(self):
        pass
    def gethealthpercent(self):
        return 20
    def newtarget(self):
        return "newtarget"
    def say(self, sth):
        print "Say: " + str(sth)
    

class script_timer:
    def __init__(self, mininter,maxinter):
        self.mininter = mininter
        self.maxinter = maxinter
        self.inter = random.randint(self.mininter,self.maxinter)
        self.lastcast = time.time()

    def ready(self):
        now = time.time()
        diff = now - self.lastcast
        if diff >= self.inter:
            return True
        else:
            return False

    def newtime(self, mininter, maxinter):
        self.mininter = mininter
        self.maxinter = maxinter

        
    def reset(self, mininter=0, maxinter=0):
        if mininter != 0 and maxinter != 0:
            self.mininter = mininter
            self.maxinter = maxinter
        self.lastcast = time.time()
        self.inter = random.randint(self.mininter,self.maxinter)
        
