#import frostlib
import random
import hashlib
def bigauthnumber():
    randomint = random.randint(1000,100000000000000000)
    sharandomint = hashlib.sha256()
    sharandomint.update(str(randomint))
    return sharandomint.hexdigest()
    
    
    
