# -*- coding: cp1252 -*-
## Basic CreatureScript:
from .. import sworld
import time
import random
class script_npc(object):
    
    def cast(self, target, spellid):
        """
        Wird ausgef�hrt wenn ein Spell aus einem Script heraus
        gecastet wird
        """
        sworld.script_castspell(self.guid() , target, spellid)
    def target(self):
        """
        Gibt das Aktuelle Target der Creature zur�ck,
        der das Script zugewiesen ist
        """
        return "Current Target"
    def randtarget(self):
        """
        Gibt ein Random Target zur�ck, welches sich im Sichtfeld
        der Creature befindet
        """
        return "Random Target"
    def domeleeattack(self):
        """
        L�sst die Creature einen Normalen Schlag ausf�hren
        """
        pass
    def gethealthpercent(self):
        """
        Gibt den Aktuellen Prozentstatus des Lebens zur�ck
        """
        return 20
    def say(self, sth):
        """
        Sagt einen Text, welcher in 5 Sprachen in der DB gespeichert ist
        """
        sworld.script_say(self.guid() , sth)
    def summon_npc(self, cre_id):
        """
        Ruft einen NPC herbei,
        welcher an der Seite der Creature gespawnt wird
        """
        print str(time.strftime("%M:%S")) + " Summon NPC: " + str(cre_id)
        
    def guid(self):
        """
        Gibt sich selber zur�ck
        """
        return self
    def teleporttoplayer(self,player):
        """
        Teleportiert sich zu player
        """
        print  str(time.strftime("%M:%S")) + " Teleport to Player: " + str(player)

    def setdisplayid(self, modelid):
        """
        �ndert die Display ID der Creature
        """
        sworld.script_setmodelid(self.guid(), modelid)
    def set(self, group, key, value):
        """
        Um tiefgreifende �nderungen der Creature zu bewirken
        """
        pass
    def selectable(self):
        """
        Macht die Creature Selektierbar
        """
        print str(time.strftime("%M:%S")) + " Make Selectable"

    def unselectable(self):
        """
        Macht die Creature nicht Selektierbar
        """
        print str(time.strftime("%M:%S")) + " Make Unselectable"

    def attackstop(self):
        """
        H�rt auf Anzugreifen
        """
        print str(time.strftime("%M:%S")) + " Stop Attacking"

    def attack(self,creature):
        """
        F�ngt an creature anzugreifen
        """
        print str(time.strftime("%M:%S")) + " Start Attacking " + str(creature)
        
    def settarget(self,newtar):
        """
        Setzt ein neues Target
        """
        self.target = newtar

    def spawn_creature(self, cre_id, posx, posy, posz, rotation):
        """
        Spawnt eine neue Creature
        """
        print "Creature ID: " + str(cre_id)
        print "Pos X:       " + str(posx)
        print "Pos Y:       " + str(posy)
        print "Pos Z:       " + str(posz)
        print "Orientation: " + str(rotation)
        
class script_timer:
    """
    Interner Script Timer

    Code ist Selbsterkl�rend
    """
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
        
