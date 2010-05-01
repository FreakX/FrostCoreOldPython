## Basic CreatureScript:
import time
import random
class script_npc(object):
    def cast(self, target, spellid):
        print str(time.strftime("%M:%S")) + " Casting Spellid: " + str(spellid) + " on " + str(target)
    def target(self):
        return "Current Target"
    def randtarget(self):
        return "Random Target"
    def domeleeattack(self):
        pass
    def gethealthpercent(self):
        return 20
    def newtarget(self):
        return "New Target"
    def say(self, sth):
        print str(time.strftime("%M:%S")) + " Say: " + str(sth)
        
    def summon_npc(self, cre_id):
        print str(time.strftime("%M:%S")) + " Summon NPC: " + str(cre_id)
        
    def guid(self):
        return "GUID from Script"

    def teleporttoplayer(self,player):
        print  str(time.strftime("%M:%S")) + " Teleport to Player: " + str(player)

    def setdisplayid(self, modelid):
        print str(time.strftime("%M:%S")) + " Change Displayid to: " + str(modelid)

    def set(self, group, key, value):
        pass

    def selectable(self):
        print str(time.strftime("%M:%S")) + " Make not Selectable"

    def unselectable(self):
        print str(time.strftime("%M:%S")) + " Make Selectable"

    def attackstop(self):
        print str(time.strftime("%M:%S")) + " Stop Attacking"

    def attack(self):
        print str(time.strftime("%M:%S")) + " Start Attacking"

    def settarget(self,newtar):
        self.target = newtar

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
if __name__ == "__main__":
    import doctest
    doctest.testmod()
        
