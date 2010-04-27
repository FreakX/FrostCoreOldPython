# -*- coding: cp1252 -*-
import frostlib
##
## Scripte werden in Instancen geladen, d.h. jede instanz ist ein Modul
## Für Creatures die nicht in Instanzen stehen sind die Module
## northrend.py , kalimdor.py, eastern_kingdoms.py, outland.py
##
## Alles in einer try Schleife, um Fehlende Scripts vorzubeugen
try:
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
    """
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
    """

except:
    frostlib.nout("Error while loading Scripts!")
    frostlib.shutdown()
