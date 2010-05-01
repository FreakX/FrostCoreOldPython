# -*- coding: cp1252 -*-
#from . import frostlib as frostlib
##
## Scripte werden in Instancen geladen, d.h. jede instanz ist ein Modul
## Für Creatures die nicht in Instanzen stehen sind die Module
## northrend.py , kalimdor.py, eastern_kingdoms.py, outland.py
##
## Alles in einer try Schleife, um Fehlende Scripts vorzubeugen
#try:
## Scripts:

## BasisScript:
import basescript

## Implementiert:


## Nicht Implementiert
import deadmines
import ragefire_chasm
import wailing_caverns
import shadowfang_keep
import stockades
import gnomeregan
import razorfen_kraul
import scarlet_monastery
import razorfen_downs
import uldaman
import zulfarrak
import mauraudon
import sunken_temple
import blackrock_depths
import dire_maul
import blackrock_spire
import stratholme
import scholomance
import ahnqiraj_ruins
import zulgurub
import molten_core
import onyxias_lair
import blackwing_lair
import ahnqiraj_temple
import hellfire_ramparts
import blood_furnace
import slave_pens
import underbog
import mana_tombs
import auchenai_crypts
import durnholde_time # ? Höhlen der Zeit: Durnholde
import sethekk_halls
import steamvault
import shattered_halls
import dark_portal_time # ? Höhlen der Zeit: Das dunkle Portal
import mechanar
import botanika
import schadow_labyrinth
import arkatraz
import magister_terace # ? Terrasse der Magister
import karazhan
import zulaman
import gruuls_lair
import magtheridons_lair
import serpentshrine_cavern
import eye_of_the_storm
import mountain_hyjal # ? Höhlen der Zeit: Schlacht am Berg Hyjal
import black_temple
import sunwellplateau
import utgarde_keep
import nexus
import azjol_nerub
import ahnkahet
import draktharon_keep
import violet_hold
import grundrak
import halls_of_stone
import utgarde_pinnacle
import halls_of_lightning
import oculus
import stratholme
import trial_of_the_champion
import forge_of_souls
import pit_of_saron
import halls_of_reflection
import vault_of_archavon
import naxxramas
import obsidian_sanctum
import eye_of_eternety
import ulduar
import trial_of_the_crusader
import icecrown


reload(deadmines)
reload(ragefire_chasm)
reload(wailing_caverns)
reload(shadowfang_keep)
reload(stockades)
reload(gnomeregan)
reload(razorfen_kraul)
reload(scarlet_monastery)
reload(razorfen_downs)
reload(uldaman)
reload(zulfarrak)
reload(mauraudon)
reload(sunken_temple)
reload(blackrock_depths)
reload(dire_maul)
reload(blackrock_spire)
reload(stratholme)
reload(scholomance)
reload(ahnqiraj_ruins)
reload(zulgurub)
reload(molten_core)
reload(onyxias_lair)
reload(blackwing_lair)
reload(ahnqiraj_temple)
reload(hellfire_ramparts)
reload(blood_furnace)
reload(slave_pens)
reload(underbog)
reload(mana_tombs)
reload(auchenai_crypts)
reload(durnholde_time) # ? Höhlen der Zeit: Durnholde
reload(sethekk_halls)
reload(steamvault)
reload(shattered_halls)
reload(dark_portal_time) # ? Höhlen der Zeit: Das dunkle Portal
reload(mechanar)
reload(botanika)
reload(schadow_labyrinth)
reload(arkatraz)
reload(magister_terace) # ? Terrasse der Magister
reload(karazhan)
reload(zulaman)
reload(gruuls_lair)
reload(magtheridons_lair)
reload(serpentshrine_cavern)
reload(eye_of_the_storm)
reload(mountain_hyjal) # ? Höhlen der Zeit: Schlacht am Berg Hyjal
reload(black_temple)
reload(sunwellplateau)
reload(utgarde_keep)
reload(nexus)
reload(azjol_nerub)
reload(ahnkahet)
reload(draktharon_keep)
reload(violet_hold)
reload(grundrak)
reload(halls_of_stone)
reload(utgarde_pinnacle)
reload(halls_of_lightning)
reload(oculus)
reload(stratholme)
reload(trial_of_the_champion)
reload(forge_of_souls)
reload(pit_of_saron)
reload(halls_of_reflection)
reload(vault_of_archavon)
reload(naxxramas)
reload(obsidian_sanctum)
reload(eye_of_eternety)
reload(ulduar)
reload(trial_of_the_crusader)
reload(icecrown)
"""
except:
    print "Error while loading Scripts!"
    exit()
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
