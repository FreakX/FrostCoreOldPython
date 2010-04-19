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
sworld = frostlib.world.world()
sworld.connect_mysql()
sworld.loaditems()
sworld.loaditems_localized()
sworld.load_creatures()

frostlib.dout("FrostCore World is starting...")
# twisted Imports
from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor, threads, defer

active_connections = 0

class LogonProtocol(Protocol):

    def dataReceived(self, data):
        d = defer.succeed(frostlib.handler.logonhandler(data))

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
    import time
    while True:
        time.sleep(frostlib.CONNECTION_INFO_DELAY)
        print str(active_connections) + " World Connections Active"

factory = Factory()
factory.protocol = LogonProtocol
print "FrostCore World Ready!"
try:
    reactor.listenTCP(8085, factory)
    print "FrostCore World now listen for Connections!"
    if frostlib.CONNECTION_INFO == True:
        reactor.callInThread(running)
    reactor.run()
except:
    frostlib.nout("Cannot Bind Socket on Port 8085!")
    frostlib.shutdown()
