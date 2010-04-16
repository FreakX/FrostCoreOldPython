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
   */
"""
import frostlib
INI_FILE_WORLD = "world.ini"
INI_FILE_LOGON = "logon.ini"
def getkey(line):
    #swallow everything up to the =
    return line[ : line.find('=') ].strip()

def getval(line):
    #swallow everything after the =
    return line[ line.find('=') + 1 : ].strip()

def loadlogonconf():
    try:
        confdict = {}
        f = open(INI_FILE_LOGON, 'r')
        data = f.readlines()
        for line in data:
            key = getkey(line)
            value = getval(line)
            confdict[key] = value
        try:
            frostlib.LOG_LEVEL = int(confdict["LOG_LEVEL"])
            frostlib.DEBUG_MODE = int(confdict["DEBUG_MODE"])
            frostlib.CONNECTION_INFO = int(confdict["CONNECTION_INFO"])
            frostlib.CONNECTION_INFO_DELAY = int(confdict["CONNECTION_INFO_DELAY"])
            frostlib.CLIENT_AUTH_INFO = int(confdict["CLIENT_AUTH_INFO"])
            frostlib.AUTHBUILD_ACCEPT = int(confdict["AUTHBUILD_ACCEPT"])
            frostlib.HASH = str(confdict["FROSTLIB_HASH"])
    

        except:
            print "Error while loading Config"
        print "Logon configuration successfully loaded"
    except:
        print "No valid INI File found"

            
def loadworldconf():
    try:
        confdict = {}
        f = open(INI_FILE_WORLD, 'r')
        data = f.readlines()
        for line in data:
            key = getkey(line)
            value = getval(line)
            confdict[key] = value
        print "World configuration successfully loaded"
    except:
        print "No valid INI File found"
