# -*- coding: cp1252 -*-
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

us = raw_input("Revision ändern?")
ja = ["ja", "yes", "1"]
if us in ja:
    f = open("frostlib/__init__.py", 'r')
    data = f.readlines()
    f.close()
    f = open("frostlib/__init__.py", 'w')
    for lines in data:
        if not "__REVISION__" in lines:
            f.write(lines)
        else:
            a = lines
            a = a.split()
            revision = a[2]
            f.write("__REVISION__ = "+ str(int(revision) + 1) + "\n")
    f.close
    print "Revision set to " + str(int(revision) + 1)

frostlib_hash = frostlib.hash.GetHashofDirs("frostlib", 0)
f = open("logon.cfg", 'r')
data = f.readlines()
f.close()
f = open("logon.cfg", 'w')
for lines in data:
    if not "frostlib_hash" in lines:
        f.write(lines)
    else:
        f.write("frostlib_hash = "+frostlib_hash + "\n")
f.close
print "Set Logon Hash to: " + str(frostlib_hash)
f = open("world.cfg", 'r')
data = f.readlines()
f.close()
f = open("world.cfg", 'w')
for lines in data:
    if not "frostlib_hash" in lines:
        f.write(lines)
    else:
        f.write("frostlib_hash = "+frostlib_hash + "\n")
f.close
print "Set World Hash to: " + str(frostlib_hash)

pause = raw_input("Taste drücken zum Beenden ...")
