import __init__
script = []
a = __init__.zulgurub.boss_arlokk()
script.append(a)
a = __init__.molten_core.boss_baron_geddon()
script.append(a)
a = __init__.molten_core.boss_garr()
script.append(a)
a = __init__.molten_core.boss_lucifron()
script.append(a)
a = __init__.molten_core.boss_magmadar()
script.append(a)
a = __init__.molten_core.boss_gehennas()
script.append(a)
a = __init__.molten_core.boss_golemagg()
script.append(a)
while True:
    for x in script:
        try:
            x.update()
        except:
            script.remove(x)


