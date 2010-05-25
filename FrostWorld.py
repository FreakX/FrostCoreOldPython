"""
  /*
   * FrostCore MMORPG Server Emulator
   * Copyright (C) 2010 <http://frostcore.demonic-legends.de/>
   *
   * Redistributions of source code must retain the above copyright notice,
   * this condition and the following license description.
   *
   * This program is free software: you can redistribute it and/or modify
   * it under the terms of the GNU Affero General Public License as published by
   * the Free Software Foundation, either version 3 of the License, or
   * any later version.
   *
   * This program is distributed in the hope that it will be useful,
   * but WITHOUT ANY WARRANTY; without even the implied warranty of
   * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   * GNU Affero General Public License for more details.
   *
   * You should have received a copy of the GNU Affero General Public License
   * along with this program.  If not, see <http://www.gnu.org/licenses/>.
   *
   * NON PUBLIC VER
   */
"""

import frostlib
from time import sleep
import warnings
warnings.filterwarnings("ignore")
frostlib.config.loadworldconf()
frostlib.slogger.info("__________                       _____ _________                     ")
frostlib.slogger.info("___  ____/______________ __________  /___  ____/______ _____________ ")
frostlib.slogger.info("__  /_    __  ___/_  __ \__  ___/_  __/_  /     _  __ \__  ___/_  _ \\")
frostlib.slogger.info("_  __/    _  /    / /_/ /_(__  ) / /_  / /___   / /_/ /_  /    /  __/")
frostlib.slogger.info("/_/       /_/     \____/ /____/  \__/  \____/   \____/ /_/     \___/ ")
frostlib.slogger.info("FrostCore Revision: " + str(frostlib.RELEASE_TYPE) + "-" + str(frostlib.__REVISION__))
frostlib.slogger.info("Checking FrostLIB Hash...")
frostlib_hash = frostlib.hash.GetHashofDirs("frostlib", 1)
frostlib.slogger.info("FrostLIB Hash: " + str(frostlib_hash))
frostlib.slogger.info("Frostlig.FROSTLIB_HASH: " + str(frostlib.FROSTLIB_HASH))
if frostlib_hash != frostlib.FROSTLIB_HASH:
    frostlib.slogger.info("False FrostLIB HASH")
    frostlib.shutdown()
    
frostlib.slogger.info("Loading Data...")
frostlib.sworld.connect_db()
frostlib.sworld.loaditems()
frostlib.sworld.loaditems_localized()
frostlib.sworld.load_creatures()
frostlib.sworld.loadscripttexts()
frostlib.slogger.info("Loading Data Completed !")

frostlib.slogger.info("FrostCore World is starting...")
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
                frostlib.slogger.debug("Malformed Packet...dropping Connection")
                self.transport.loseConnection()

        d = d.addCallback(got_info)
        if not data:
            self.transport.write("")
            


    def connectionMade(self):
        global active_connections
        active_connections = active_connections+1
        frostlib.slogger.debug("Accepting Connection from " + str(self.transport.getPeer()[1]) + " on Port " + str(self.transport.getPeer()[2])
)
    def connectionLost(self, reason):
        global active_connections
        active_connections = active_connections-1
        frostlib.slogger.debug("Connection Lost from " + str(self.transport.getPeer()[1]))
def developement():
    for x in xrange(0,500):
        frostlib.sworld.GetScriptByName("boss_garr").RegisterScript()
        frostlib.sworld.GetScriptByName("boss_gehennas").RegisterScript()
        frostlib.sworld.GetScriptByName("boss_baron_geddon").RegisterScript()
        frostlib.sworld.GetScriptByName("boss_garr").RegisterScript()
        frostlib.sworld.GetScriptByName("boss_lucifron").RegisterScript()
        frostlib.sworld.GetScriptByName("boss_magmadar").RegisterScript()
        frostlib.sworld.GetScriptByName("boss_gehennas").RegisterScript()
        frostlib.sworld.GetScriptByName("boss_golemagg").RegisterScript()
        frostlib.sworld.GetScriptByName("boss_shazzrah").RegisterScript()
        frostlib.sworld.GetScriptByName("boss_sulfuron_harbringer").RegisterScript()
        frostlib.sworld.GetScriptByName("mob_sulfuron_harbringer").RegisterScript()
        frostlib.sworld.GetScriptByName("boss_majordomo_executus").RegisterScript()
        frostlib.sworld.GetScriptByName("boss_hakkar").RegisterScript()
        frostlib.sworld.GetScriptByName("boss_arlokk").RegisterScript()
        frostlib.sworld.GetScriptByName("boss_gahzranka").RegisterScript()
        frostlib.sworld.GetScriptByName("boss_grilek").RegisterScript()
        frostlib.sworld.GetScriptByName("boss_hazzarah").RegisterScript()
        frostlib.sworld.GetScriptByName("boss_jeklik").RegisterScript()
    
def running():
    """
    Zeigt die aktuellen offenen Connections an
    """
    import time
    while True:
        time.sleep(frostlib.CONNECTION_INFO_DELAY)
        frostlib.slogger.debug(str(active_connections) + " World Connections Active")

def update_scripts():
    """
    Aktualisiert die Scripts in der World
    """
    while True:
        try:
            frostlib.sworld.update_scripts()
        except:
            frostlib.slogger.debug("Error in FrostScript")
factory = Factory()
factory.protocol = WorldProtocol
frostlib.slogger.info("FrostCore World Ready!")
reactor.callInThread(update_scripts)
reactor.callInThread(developement)
try:
    reactor.listenTCP(8085, factory)
    frostlib.slogger.debug("FrostCore World now listen for Connections!")
    if frostlib.CONNECTION_INFO == True:
        reactor.callInThread(running)
    reactor.run()
except:
    frostlib.slogger.info("Cannot Bind Socket on Port 8085!")
    frostlib.shutdown()
