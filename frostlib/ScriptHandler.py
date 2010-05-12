# -*- coding: cp1252 -*-
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
        


        
    def RegisterScript(self, script):
        script.scriptid = self.numscripts
        frostlib.slogger.info(">>> ScriptNumber::>" + str(self.numscripts))
        self.numscripts += 1
        self.wscripts.append(script)
        

