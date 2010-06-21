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
import socket
import binascii
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 3724))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
while 1:
    data = conn.recv(1024)
    if not data: break
    print data
    conn.send(binascii.unhexlify("000000166008e7dc351c05ceda18e8e32c8859f32e56135422d1c932e04fc05dbeba01010720b79b3e2a87823cab8f5ebfbf8eb10108535006298b5badbd5b53e1895e644b8951b7ad3182af63eccb0e09686a5800569f5076bd552a13e06d074fa2e58464f05f9185fd14551ad97cf9ebe204c7b7d500"))
conn.close()

