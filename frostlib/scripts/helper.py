import time
import __init__
script = []

a = __init__.zulgurub.boss_arlokk()
script.append(a)
time.sleep(0.1)
a = __init__.molten_core.boss_baron_geddon()
script.append(a)
time.sleep(0.1)
a = __init__.molten_core.boss_garr()
script.append(a)
time.sleep(0.1)
a = __init__.molten_core.boss_lucifron()
script.append(a)
time.sleep(0.1)
a = __init__.molten_core.boss_magmadar()
script.append(a)
time.sleep(0.1)
a = __init__.molten_core.boss_gehennas()
script.append(a)
time.sleep(0.1)
a = __init__.molten_core.boss_golemagg()
script.append(a)
time.sleep(0.1)
a = __init__.molten_core.boss_shazzrah()
script.append(a)
time.sleep(0.1)
a = __init__.molten_core.boss_sulfuron_harbringer()
script.append(a)
time.sleep(0.1)

while True:
    for x in script:
        try:
            x.update()
        except:
            #x.update()
            print "ERROR in " + str(x)
            script.remove(x)


