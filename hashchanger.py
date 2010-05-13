import frostlib
frostlib_hash = frostlib.hash.GetHashofDirs("frostlib", 1)
f = open("logon.cfg", 'r')
data = f.readlines()
f.close()
f = open("logon.cfg", 'w')
for lines in data:
    if not "FROSTLIB_HASH" in lines:
        f.write(lines)
    else:
        f.write("FROSTLIB_HASH="+frostlib_hash + "\n")
    print lines
f.close

f = open("world.cfg", 'r')
data = f.readlines()
f.close()
f = open("world.cfg", 'w')
for lines in data:
    if not "FROSTLIB_HASH" in lines:
        f.write(lines)
    else:
        f.write("FROSTLIB_HASH="+frostlib_hash + "\n")
    print lines
f.close
