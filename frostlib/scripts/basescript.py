## Basic CreatureScript:
import time
import random
        

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
    def reset(self):
        self.lastcast = time.time()
        self.inter = random.randint(self.mininter,self.maxinter)
        
