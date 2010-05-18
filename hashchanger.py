# -*- coding: cp1252 -*-
import frostlib
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
pause = raw_input("Taste drücken zum Beenden ...")
