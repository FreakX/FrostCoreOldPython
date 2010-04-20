import frostlib
frostlib_hash = frostlib.hash.GetHashofDirs("frostlib", 1)
f = open("logon.ini", 'r')
data = f.readlines()
f.close()
f = open("logon.ini", 'w')
for lines in data:
    if not "FROSTLIB_HASH" in lines:
        f.write(lines)
    else:
        f.write("FROSTLIB_HASH="+frostlib_hash + "\n")
    print lines
f.close

f = open("world.ini", 'r')
data = f.readlines()
f.close()
f = open("world.ini", 'w')
for lines in data:
    if not "FROSTLIB_HASH" in lines:
        f.write(lines)
    else:
        f.write("FROSTLIB_HASH="+frostlib_hash + "\n")
    print lines
f.close
