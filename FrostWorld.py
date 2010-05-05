
# (c) FreakX,P13RR3

import frostlib
from time import sleep
import warnings
warnings.filterwarnings("ignore")
frostlib.config.loadworldconf()
frostlib.nout("__________                       _____ _________                     ")
frostlib.nout("___  ____/______________ __________  /___  ____/______ _____________ ")
frostlib.nout("__  /_    __  ___/_  __ \__  ___/_  __/_  /     _  __ \__  ___/_  _ \\")
frostlib.nout("_  __/    _  /    / /_/ /_(__  ) / /_  / /___   / /_/ /_  /    /  __/")
frostlib.nout("/_/       /_/     \____/ /____/  \__/  \____/   \____/ /_/     \___/ ")
frostlib.dout("FrostCore Revision: " + str(frostlib.RELEASE_TYPE) + "-" + str(frostlib.REVISION))
frostlib.dout("Checking FrostLIB Hash...")
frostlib_hash = frostlib.hash.GetHashofDirs("frostlib", 1)
frostlib.dout("FrostLIB Hash: " + str(frostlib_hash))
if frostlib_hash != frostlib.HASH:
    frostlib.nout("False FrostLIB HASH")
    frostlib.shutdown()

frostlib.dout("Loading Data...")
frostlib.sworld.connect_db()
frostlib.sworld.loaditems()
frostlib.sworld.loaditems_localized()
frostlib.sworld.load_creatures()
frostlib.sworld.loadscripttexts()
frostlib.dout("Loading Data Completed !")

# Debug Code for Dev
if frostlib.DEBUG_MODE == True:
    
    frostlib.dout("Debugging Scripts...")
    frostlib.sworld.wscripts.append(frostlib.scripts.molten_core.boss_gehennas())
    frostlib.sworld.wscripts.append(frostlib.scripts.molten_core.boss_baron_geddon())
    frostlib.sworld.wscripts.append(frostlib.scripts.molten_core.boss_garr())
    frostlib.sworld.wscripts.append(frostlib.scripts.molten_core.boss_lucifron())
    frostlib.sworld.wscripts.append(frostlib.scripts.molten_core.boss_magmadar())
    frostlib.sworld.wscripts.append(frostlib.scripts.molten_core.boss_gehennas())
    frostlib.sworld.wscripts.append(frostlib.scripts.molten_core.boss_golemagg())
    frostlib.sworld.wscripts.append(frostlib.scripts.molten_core.boss_shazzrah())
    frostlib.sworld.wscripts.append(frostlib.scripts.molten_core.boss_sulfuron_harbringer())
    frostlib.sworld.wscripts.append(frostlib.scripts.molten_core.mob_sulfuron_harbringer())
    frostlib.sworld.wscripts.append(frostlib.scripts.molten_core.boss_majordomo_executus())
    frostlib.sworld.wscripts.append(frostlib.scripts.zulgurub.boss_hakkar())
    frostlib.sworld.wscripts.append(frostlib.scripts.zulgurub.boss_arlokk())
    frostlib.sworld.wscripts.append(frostlib.scripts.zulgurub.boss_gahzranka())
    frostlib.sworld.wscripts.append(frostlib.scripts.zulgurub.boss_grilek())
    frostlib.sworld.wscripts.append(frostlib.scripts.zulgurub.boss_hazzarah())
    frostlib.sworld.wscripts.append(frostlib.scripts.zulgurub.boss_jeklik())
frostlib.dout("FrostCore World is starting...")
# twisted Imports
from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor, threads, defer

active_connections = 0

class WorldProtocol(Protocol):
    """
    World Protokoll Klasse

    Wird von twisted verwendet um das Netzwerk zu verwalten
    """

    def dataReceived(self, data):
        d = defer.succeed(frostlib.handler.worldhandler(data))

        def got_info(res):
            if res != "error":
                self.transport.write(res)
            else:
                print "Malformed Packet...dropping Connection"
                self.transport.loseConnection()

        d = d.addCallback(got_info)
        if not data:
            self.transport.write("")
            


    def connectionMade(self):
        global active_connections
        active_connections = active_connections+1
        print "Accepting Connection from " + str(self.transport.getPeer()[1]) + " on Port " + str(self.transport.getPeer()[2])

    def connectionLost(self, reason):
        global active_connections
        active_connections = active_connections-1
        print "Connection Lost from " + str(self.transport.getPeer()[1])

def running():
    """
    Zeigt die aktuellen offenen Connections an
    """
    import time
    while True:
        time.sleep(frostlib.CONNECTION_INFO_DELAY)
        print str(active_connections) + " World Connections Active"

def update_scripts():
    """
    Aktualisiert die Scripts in der World
    """
    while True:
        try:
            frostlib.sworld.update_scripts()
        except:
            frostlib.dout("Error in FrostScript")
factory = Factory()
factory.protocol = WorldProtocol
print "FrostCore World Ready!"
reactor.callInThread(update_scripts)
try:
    reactor.listenTCP(8085, factory)
    print "FrostCore World now listen for Connections!"
    if frostlib.CONNECTION_INFO == True:
        reactor.callInThread(running)
    reactor.run()
except:
    frostlib.nout("Cannot Bind Socket on Port 8085!")
    frostlib.shutdown()
