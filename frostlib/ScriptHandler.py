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
            script_text_obj = frostlib.classes.script_text(script_id,
                                                           script_text)
            self.wscript_texts[script_id] = script_text_obj
            p.update_time(cur)
            cur += 1
            if str(p) != pold:
                frostlib.nout(str(p))
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
                    frostlib.nout(str(p))
                    pold = str(p)
            except:
                frostlib.nout("Error while loading Script Text " + str(currentry) + " deDE")

        for entry in range(0,resultcount_es):
            try:
                currentry = result_es[entry]
                script_id = int(currentry[0])
                script_text = str(currentry[1])
                self.wscript_texts[script_id].set_lang("esES", script_text)
                p.update_time(cur)
                cur += 1
                if str(p) != pold:
                    frostlib.nout(str(p))
                    pold = str(p)
            except:
                frostlib.nout("Error while loading Script Text " + str(currentry) + " esES")

        for entry in range(0,resultcount_fr):
            try:
                currentry = result_fr[entry]
                script_id = int(currentry[0])
                script_text = str(currentry[1])
                self.wscript_texts[script_id].set_lang("frFR", script_text)
                p.update_time(cur)
                cur += 1
                if str(p) != pold:
                    frostlib.nout(str(p))
                    pold = str(p)

            except:
                frostlib.nout("Error while loading Script Text " + str(currentry) + " frFR")

        for entry in range(0,resultcount_ru):
            try:
                currentry = result_ru[entry]
                script_id = int(currentry[0])
                script_text = str(currentry[1])
                self.wscript_texts[script_id].set_lang("ruRU", script_text)
                p.update_time(cur)
                cur += 1
                if str(p) != pold:
                    frostlib.nout(str(p))
                    pold = str(p)
            except:
                frostlib.nout("Error while loading Script Text " + str(currentry) + " ruRU")
    
    
    
    def script_setmodelid(self, changer, modelid):
        """ Setzt Modelid's """
        print str(time.strftime("%M:%S")) + " Creature " + str(changer) + " changing Modelid to " + str(modelid)
    def script_castspell(self, caster, target, spellid):
        """ Castet Spells """
        print str(time.strftime("%M:%S")) + " Creature " + str(caster) + " casting Spellid: " + str(spellid) + " on " + str(target)
        pass
    def script_say(self, say, textid):
        """ Sagt Texte

        say -> Creature die Text sagt"""
        print str(time.strftime("%M:%S")) + " Creature " + str(say) + " Saying: " + str(textid)
        #try:
        text = self.wscript_texts[int(textid)]
        try:
            print str(time.strftime("%M:%S")) + " enUS: " + str(text.getlocalizedtext("enUS"))
        except:
            print "Error"
        try:
            print str(time.strftime("%M:%S")) + " deDE: " + str(text.getlocalizedtext("deDE"))
        except:
            print "Error"
        try:
            print str(time.strftime("%M:%S")) + " esES: " + str(text.getlocalizedtext("esES"))
        except:
            print "Error"
        try:
            print str(time.strftime("%M:%S")) + " frFR: " + str(text.getlocalizedtext("frFR"))
        except:
            print "Error"
        try:
            print str(time.strftime("%M:%S")) + " ruRU: " + str(text.getlocalizedtext("ruRU"))
        except:
            print "Error"
        #except:
        #    frostlib.nout("No Script Text with ID: " + str(textid))


        
    def RegisterScript(self, script):
        script.scriptid = self.numscripts
        print ">>> ScriptNumber::>" + str(self.numscripts)
        self.numscripts += 1
        self.wscripts.append(script)
        

