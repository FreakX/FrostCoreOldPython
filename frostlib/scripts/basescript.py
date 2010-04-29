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
    def summon_npc(self, cre_id):
        print "Summon NPC: " + str(cre_id)
    def guid(self):
        return 123456789
    

class script_timer:
    def __init__(self, mininter,maxinter):
        self.mininter = int(mininter*1000)
        self.maxinter = int(maxinter*1000)
        self.inter = float(random.randint(self.mininter,self.maxinter)/1000)
        self.lastcast = time.time()

    def ready(self):
        now = time.time()
        diff = now - self.lastcast
        if diff >= self.inter:
            return True
        else:
            return False

    def newtime(self, mininter, maxinter):
        self.mininter = int(mininter*1000)
        self.maxinter = int(maxinter*1000)

        
    def reset(self, mininter=0, maxinter=0):
        if mininter != 0 and maxinter != 0:
            self.mininter = int(mininter*1000)
            self.maxinter = int(maxinter*1000)
        self.lastcast = time.time()
        self.inter = float(random.randint(self.mininter,self.maxinter)/1000)

        
