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

INI_FILE_WORLD = "world.ini"
INI_FILE_LOGON = "logon.ini"
def getkey(line):
    #swallow everything up to the =
    return line[ : line.find('=') ].strip()

def getval(line):
    #swallow everything after the =
    return line[ line.find('=') + 1 : ].strip()

def getlogonconf():
    try:
        confdict = {}
        f = open(INI_FILE_LOGON, 'r')
        data = f.readlines()
        for line in data:
            key = getkey(line)
            value = getval(line)
            confdict[key] = value
        print "Logon configuration successfully loaded"
        return confdict
    except:
        print "No valid INI File found ... will create one"
        try:
            f = open(INI_FILE_WORLD, 'w')
            f.write("char_database_host=127.0.0.1\n")
            f.write("char_database_port=3306\n")
            f.write("char_database_user=root\n")
            f.write("char_database_pw=password\n")
            f.write("logon_database_host=127.0.0.1\n")
            f.write("logon_database_port=3306\n")
            f.write("logon_database_user=root\n")
            f.write("logon_database_pw=password\n")
            print "Created a valid conf file!"
        except:
            print "Error writing new conf file"

            
def getworldconf():
    try:
        confdict = {}
        f = open(INI_FILE_WORLD, 'r')
        data = f.readlines()
        for line in data:
            key = getkey(line)
            value = getval(line)
            confdict[key] = value
        print "World configuration successfully loaded"
        return confdict
    except:
        print "No valid INI File found ... will create one"
        try:
            f = open(INI_FILE_WORLD, 'w')
            f.write("char_database_host=127.0.0.1\n")
            f.write("char_database_port=3306\n")
            f.write("char_database_user=root\n")
            f.write("char_database_pw=password\n")
            f.write("logon_database_host=127.0.0.1\n")
            f.write("logon_database_port=3306\n")
            f.write("logon_database_user=root\n")
            f.write("logon_database_pw=password\n")
            print "Created a valid conf file!"
        except:
            print "Error writing new conf file"
