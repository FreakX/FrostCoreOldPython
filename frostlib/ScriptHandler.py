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
   */
"""

import frostlib
import time
class ScriptHandler(object):
    def loadscripttexts(self):
        """
        Lädt die Script Texte aus der Datenbank
        """
        resultcount_en = self.cursor.execute("SELECT * FROM script_texts_en")
        result_en = self.cursor.fetchall()

        resultcount_de = self.cursor.execute("SELECT * FROM script_texts_de")
        result_de = self.cursor.fetchall()

        resultcount_es = self.cursor.execute("SELECT * FROM script_texts_es")
        result_es = self.cursor.fetchall()

        resultcount_fr = self.cursor.execute("SELECT * FROM script_texts_fr")
        result_fr = self.cursor.fetchall()

        resultcount_ru = self.cursor.execute("SELECT * FROM script_texts_ru")
        result_ru = self.cursor.fetchall()
        
        counter = int(resultcount_en) + int(resultcount_de) + int(resultcount_es) + int(resultcount_fr) + int(resultcount_ru)
        p = frostlib.ProgressBar(int(counter), "Loading Script Texts...")
        pold = str(p)
        cur = 0
        for entry in range(0,resultcount_en):
            #try:
            currentry = result_en[entry]
            script_id = int(currentry[0])
            script_text = str(currentry[1])
            script_text_obj = frostlib.classes.ScriptText(script_id,
                                                           script_text)
            self.wscript_texts[script_id] = script_text_obj
            p.update_time(cur)
            cur += 1
            if str(p) != pold:
                frostlib.slogger.info(str(p))
                pold = str(p)
            #except:
            #    frostlib.nout("Error while loading Script Text " + str(currentry) + " enEN")
        
        for entry in range(0,resultcount_de):
            try:
                currentry = result_de[entry]
                script_id = int(currentry[0])
                script_text = str(currentry[1])
                self.wscript_texts[script_id].set_lang("deDE", script_text)
                p.update_time(cur)
                cur += 1
                if str(p) != pold:
                    frostlib.slogger.info(str(p))
                    pold = str(p)
            except:
                frostlib.slogger.info("Error while loading Script Text " + str(currentry) + " deDE")

        for entry in range(0,resultcount_es):
            try:
                currentry = result_es[entry]
                script_id = int(currentry[0])
                script_text = str(currentry[1])
                self.wscript_texts[script_id].set_lang("esES", script_text)
                p.update_time(cur)
                cur += 1
                if str(p) != pold:
                    frostlib.slogger.info(str(p))
                    pold = str(p)
            except:
                frostlib.slogger.info("Error while loading Script Text " + str(currentry) + " esES")

        for entry in range(0,resultcount_fr):
            try:
                currentry = result_fr[entry]
                script_id = int(currentry[0])
                script_text = str(currentry[1])
                self.wscript_texts[script_id].set_lang("frFR", script_text)
                p.update_time(cur)
                cur += 1
                if str(p) != pold:
                    frostlib.slogger.info(str(p))
                    pold = str(p)

            except:
                frostlib.slogger.info("Error while loading Script Text " + str(currentry) + " frFR")

        for entry in range(0,resultcount_ru):
            try:
                currentry = result_ru[entry]
                script_id = int(currentry[0])
                script_text = str(currentry[1])
                self.wscript_texts[script_id].set_lang("ruRU", script_text)
                p.update_time(cur)
                cur += 1
                if str(p) != pold:
                    frostlib.slogger.info(str(p))
                    pold = str(p)
            except:
                frostlib.slogger.info("Error while loading Script Text " + str(currentry) + " ruRU")
    
        frostlib.slogger.info(">>> Loaded " + str(cur) + " Script Texts")
    
    def script_setmodelid(self, changer, modelid):
        """ Setzt Modelid's """
        frostlib.slogger.info("Creature " + str(changer) + " changing Modelid to " + str(modelid))
    def script_castspell(self, caster, target, spellid):
        """ Castet Spells """
        frostlib.slogger.info("Creature " + str(caster) + " casting Spellid: " + str(spellid) + " on " + str(target))
        pass
    def script_say(self, say, textid):
        """ Sagt Texte

        say -> Creature die Text sagt"""
        frostlib.slogger.info("Creature " + str(say) + " Saying: " + str(textid))
        text = self.wscript_texts[int(textid)]
        try:
            frostlib.slogger.info("enUS: " + str(text.getlocalizedtext("enUS")))
        except:
            frostlib.slogger.warning("No enUS Localization for: " + str(textid))
        try:
            frostlib.slogger.info("deDE: " + str(text.getlocalizedtext("deDE")))
        except:
            frostlib.slogger.warning("No deDE Localization for: " + str(textid))
        try:
            frostlib.slogger.info("esES: " + str(text.getlocalizedtext("esES")))
        except:
            frostlib.slogger.warning("No esES Localization for: " + str(textid))
        try:
            frostlib.slogger.info("frFR: " + str(text.getlocalizedtext("frFR")))
        except:
            frostlib.slogger.warning("No frFR Localization for: " + str(textid))
        try:
            frostlib.slogger.info("ruRU: " + str(text.getlocalizedtext("ruRU")))
        except:
            frostlib.slogger.warning("No ruRU Localization for: " + str(textid))
        
    def GetScriptByName(self, scriptname):
        import scripts as sdb
        scripts = {
            ##########   Zulgurub  ##########
            "boss_arlokk"               : sdb.zulgurub.boss_arlokk,
            "boss_gahzranka"            : sdb.zulgurub.boss_gahzranka,
            "boss_grilek"               : sdb.zulgurub.boss_grilek,
            "boss_hakkar"               : sdb.zulgurub.boss_hakkar,
            "boss_hazzarah"             : sdb.zulgurub.boss_hazzarah,
            "boss_jeklik"               : sdb.zulgurub.boss_jeklik,
            ########## Molten Core ##########
            "boss_baron_geddon"         : sdb.molten_core.boss_baron_geddon,
            "boss_garr"                 : sdb.molten_core.boss_garr,
            "boss_lucifron"             : sdb.molten_core.boss_lucifron,
            "boss_magmadar"             : sdb.molten_core.boss_magmadar,
            "boss_gehennas"             : sdb.molten_core.boss_gehennas,
            "boss_golemagg"             : sdb.molten_core.boss_golemagg,
            "boss_shazzrah"             : sdb.molten_core.boss_shazzrah,
            "boss_sulfuron_harbringer"  : sdb.molten_core.boss_sulfuron_harbringer,
            "mob_sulfuron_harbringer"   : sdb.molten_core.mob_sulfuron_harbringer,
            "boss_majordomo_executus"   : sdb.molten_core.boss_majordomo_executus,
            ########## Naxxramas   ##########
            "boss_anubrekhan"           : sdb.naxxramas.boss_anubrekhan,

            ########## Schwarzfels ##########
            "boss_ambassador_flamelash" : sdb.blackrock_depths.boss_ambassador_flamelash,
            "boss_anubshiah"            : sdb.blackrock_depths.boss_anubshiah
            }
        try:
            return scripts[scriptname]()
        except KeyError:
            return sdb.zulgurub.boss_jeklik()
        

        
    def RegisterScript(self, script):
        script.scriptid = self.numscripts
        script.name = script.__class__.__name__
        frostlib.slogger.info(">>> ScriptNumber::>" + str(self.numscripts))
        self.numscripts += 1
        self.wscripts.append(script)
        

