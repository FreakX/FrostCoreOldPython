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
frostlib.config.loadlogonconf()
frostlib.slogger.info("__________                       _____ _________                     ")
frostlib.slogger.info("___  ____/______________ __________  /___  ____/______ _____________ ")
frostlib.slogger.info("__  /_    __  ___/_  __ \__  ___/_  __/_  /     _  __ \__  ___/_  _ \\")
frostlib.slogger.info("_  __/    _  /    / /_/ /_(__  ) / /_  / /___   / /_/ /_  /    /  __/")
frostlib.slogger.info("/_/       /_/     \____/ /____/  \__/  \____/   \____/ /_/     \___/ ")
frostlib.slogger.info("FrostCore Revision: " + str(frostlib.RELEASE_TYPE) + "-" + str(frostlib.__REVISION__))
frostlib.slogger.info("Checking FrostLIB Hash...")
frostlib_hash = frostlib.hash.GetHashofDirs("frostlib", 1)
frostlib.slogger.info("Current FrostLIB Hash : " + str(frostlib_hash))
frostlib.slogger.info("Saved FrostLIB Hash   : " + str(frostlib.FROSTLIB_HASH))
if frostlib_hash != frostlib.FROSTLIB_HASH:
    frostlib.slogger.info("False FrostLIB HASH")
    frostlib.shutdown()
  
frostlib.slogger.debug("FrostCore Logon is starting...")
# twisted Imports
active_connections = 0

class LogonProtocol(Protocol):

    def dataReceived(self, data):
        d = defer.succeed(frostlib.handler.logonhandler(data))

        def got_info(res):
            if res != "error":
                self.transport.write(res)
            else:
                frostlib.slogger.exception("Malformed Packet...dropping Connection")
                self.transport.loseConnection()

        d = d.addCallback(got_info)
        if not data:
            self.transport.write("")
            


    def connectionMade(self):
        global active_connections
        active_connections = active_connections+1
        frostlib.slogger.info("Accepting Connection from " + str(self.transport.getPeer()[1]) + " on Port " + str(self.transport.getPeer()[2]))

    def connectionLost(self, reason):
        global active_connections
        active_connections = active_connections-1
        frostlib.slogger.info("Connection Lost from " + str(self.transport.getPeer()[1]))

def running():
    import time
    while True:
        time.sleep(frostlib.CONNECTION_INFO_DELAY)
        frostlib.slogger.info(str(active_connections) + " Logon Connections Active")

factory = Factory()
factory.protocol = LogonProtocol
print "FrostCore Logon Ready!"
try:
    reactor.listenTCP(3724, factory)
    print "FrostCore Logon now listen for Connections!"
    if frostlib.CONNECTION_INFO == True:
        reactor.callInThread(running)
    reactor.run()
except:
    frostlib.slogger.exception("Cannot Bind Socket on Port 3724!")
    frostlib.shutdown()
