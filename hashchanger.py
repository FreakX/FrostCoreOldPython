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
