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
# World Class
import frostlib
import time

class world(object):
    def __init__(self):
        self.witems = {}
        self.wcreatures = {}
        self.wscripts = []
        self.wscript_texts = {}
        
    def script_castspell(self, caster, target, spellid):
        print str(time.strftime("%M:%S")) + " Creature " + str(caster) + " casting Spellid: " + str(spellid) + " on " + str(target)
    def script_say(self, say, textid):
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
        
    def update_player(self):
        # Player Update Code
        pass
    def update_scripts(self):
        # Scripts Update Code
        a_time = time.time()
        for script in self.wscripts:
            try:
                script.update()
            except:
                self.wscripts.remove(script)
                raise "ScriptError", script
        b_time = time.time()
        time_diff = b_time - a_time
        if time_diff <= frostlib.maxscriptdelay:
            time.sleep(frostlib.maxscriptdelay - time_diff)
        
    def connect_db(self):
        try:
            import MySQLdb
            mysql_opts = {
                'host': frostlib.MYSQL_WORLD_HOST,
                'user': frostlib.MYSQL_WORLD_USER,
                'pass': frostlib.MYSQL_WORLD_PW,
                'db':   frostlib.MYSQL_WORLD_DB
                }
            self.mysql = MySQLdb.connect(mysql_opts['host'], mysql_opts['user'], mysql_opts['pass'], mysql_opts['db']) 
            self.mysql.apilevel = "2.0"
            self.mysql.threadsafety = 2
            self.mysql.paramstyle = "format"
            self.cursor = self.mysql.cursor()
        except:
            import traceback
            traceback.print_exc(file=frostlib.logfile)
            frostlib.nout("No Connection to MySQL Server")
            frostlib.shutdown()
    def loadscripttexts(self):
        
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
    def loaditems(self):
        resultcount = self.cursor.execute("SELECT * FROM item_template")
        p = frostlib.ProgressBar(int(resultcount), "Loading Items...")
        pold = str(p)
        result = self.cursor.fetchall()
        for entry in range(0,resultcount):
            try:
                currentry =             result[entry]
                item_entry =            int(currentry[0])
                item_class =            int(currentry[1])
                item_subclass =         int(currentry[2])
                item_field4 =           int(currentry[3])
                item_name1 =                currentry[4]
                item_displayid =        int(currentry[5])
                item_quality =          int(currentry[6])
                item_flags =            int(currentry[7])
                item_buyprice =         int(currentry[8])
                item_sellprice =        int(currentry[9])
                item_inventorytype =    int(currentry[10])
                item_allowableclass =   int(currentry[11])
                item_allowablerace =    int(currentry[12])
                item_itemlevel =        int(currentry[13])
                item_requiredlevel =    int(currentry[14])
                item_RequiredSkill =    int(currentry[15])
                item_RequiredSkillRank =int(currentry[16])
                item_RequiredSpell =    int(currentry[17])
                item_RequiredPlayerRank1=int(currentry[18])
                item_RequiredPlayerRank2=int(currentry[19])
                item_RequiredFaction=   int(currentry[20])
                item_RequiredFactionStanding=int(currentry[21])
                item_Unique = int(currentry[22])
                item_maxcount = int(currentry[23])
                item_ContainerSlots = int(currentry[24])
                item_itemstatscount = int(currentry[25])
                item_stat_type1 = int(currentry[26])
                item_stat_value1= int(currentry[27])
                item_stat_type2 = int(currentry[28])
                item_stat_value2= int(currentry[29])
                item_stat_type3 = int(currentry[30])
                item_stat_value3= int(currentry[31])
                item_stat_type4 = int(currentry[32])
                item_stat_value4= int(currentry[33])
                item_stat_type5 = int(currentry[34])
                item_stat_value5= int(currentry[35])
                item_stat_type6 = int(currentry[36])
                item_stat_value6= int(currentry[37])
                item_stat_type7 = int(currentry[38])
                item_stat_value7= int(currentry[39])
                item_stat_type8 = int(currentry[40])
                item_stat_value8= int(currentry[41])
                item_stat_type9 = int(currentry[42])
                item_stat_value9= int(currentry[43])
                item_stat_type10= int(currentry[44])
                item_stat_value10=int(currentry[45])
                item_ScaledStatsDistributionID = int(currentry[46])
                item_ScaledStatsDistributionFlags=int(currentry[47])
                item_dmg_min1 = float(currentry[48])
                item_dmg_max1 = float(currentry[49])
                item_dmg_type1= int(currentry[50])
                item_dmg_min2 = float(currentry[51])
                item_dmg_max2 = float(currentry[52])
                item_dmg_type2= int(currentry[53])
                item_armor = int(currentry[54])
                item_holy_res = int(currentry[55])
                item_fire_res = int(currentry[56])
                item_nature_res = int(currentry[57])
                item_frost_res = int(currentry[58])
                item_shadow_res= int(currentry[59])
                item_arcane_res= int(currentry[60])
                item_delay = int(currentry[61])
                item_ammo_type= int(currentry[62])
                item_range = int(currentry[63])
                item_spellid_1 = int(currentry[64])
                item_spelltrigger_1 = int(currentry[65])
                item_spellcharges_1 = int(currentry[66])
                item_spellcooldown_1= int(currentry[67])
                item_spellcategory_1= int(currentry[68])
                item_spellcategorycooldown_1 = int(currentry[69])
                item_spellid_2 = int(currentry[70])
                item_spelltrigger_2 = int(currentry[71])
                item_spellcharges_2 = int(currentry[72])
                item_spellcooldown_2= int(currentry[73])
                item_spellcategory_2= int(currentry[74])
                item_spellcategorycooldown_2 = int(currentry[75])
                item_spellid_3 = int(currentry[76])
                item_spelltrigger_3 = int(currentry[77])
                item_spellcharges_3 = int(currentry[78])
                item_spellcooldown_3 = int(currentry[79])
                item_spellcategory_3 = int(currentry[80])
                item_spellcategorycooldown_3 = int(currentry[81])
                item_spellid_4 = int(currentry[82])
                item_spelltrigger_4 = int(currentry[83])
                item_spellcharges_4 = int(currentry[84])
                item_spellcooldown_4 = int(currentry[85])
                item_spellcategory_4 = int(currentry[86])
                item_spellcategorycooldown_4 = int(currentry[87])
                item_spellid_5 = int(currentry[88])
                item_spelltrigger_5 = int(currentry[89])
                item_spellcharges_5 = int(currentry[90])
                item_spellcooldown_5 = int(currentry[91])
                item_spellcategory_5 = int(currentry[92])
                item_spellcategorycooldown_5 = int(currentry[93])
                item_bonding = int(currentry[94])
                item_description = str(currentry[95])
                item_page_id = int(currentry[96])
                item_page_language = int(currentry[97])
                item_page_material = int(currentry[98])
                item_quest_id = int(currentry[99])
                item_lock_id = int(currentry[100])
                item_lock_material = int(currentry[101])
                item_sheathID = int(currentry[102])
                item_randomprop = int(currentry[103])
                item_randomsuffix = int(currentry[104])
                item_block = int(currentry[105])
                item_itemset = int(currentry[106])
                item_bagfamily = int(currentry[107])
                item_TotemCategory = int(currentry[108])
                item_socket_color_1 = int(currentry[109])
                item_unk201_3 = int(currentry[110])
                item_socket_color_2 = int(currentry[111])
                item_unk201_5 = int(currentry[112])
                item_socket_color_3 = int(currentry[113])
                item_unk201_7 = int(currentry[114])
                item_socket_bonus = int(currentry[115])
                item_GemProperties = int(currentry[116])
                item_ReqDisenchantSkill = int(currentry[117])
                item_ArmorDamageModifier = int(currentry[118])
                item_ExistingDuration = int(currentry[119])
                item_ItemLimitCategoryId = int(currentry[120])
                item_HolidayId = currentry[121]
                del currentry
            except:
                import traceback
                traceback.print_exc(file=frostlib.logfile)
                frostlib.dout("Fehler beim Item: " + str(entry))
            item = frostlib.classes.item(item_entry,
                                         item_class,
                                         item_subclass,
                                         item_field4,
                                         item_name1,
                                         item_displayid,
                                         item_quality,
                                         item_flags,
                                         item_buyprice,
                                         item_sellprice,
                                         item_inventorytype,
                                         item_allowableclass,
                                         item_allowablerace,
                                         item_itemlevel,
                                         item_requiredlevel,
                                         item_RequiredSkill,
                                         item_RequiredSkillRank,
                                         item_RequiredSpell,
                                         item_RequiredPlayerRank1,
                                         item_RequiredPlayerRank2,
                                         item_RequiredFaction,
                                         item_RequiredFactionStanding,
                                         item_Unique,
                                         item_maxcount,
                                         item_ContainerSlots,
                                         item_itemstatscount,
                                         item_stat_type1,
                                         item_stat_value1,
                                         item_stat_type2,
                                         item_stat_value2,
                                         item_stat_type3,
                                         item_stat_value3,
                                         item_stat_type4,
                                         item_stat_value4,
                                         item_stat_type5,
                                         item_stat_value5,
                                         item_stat_type6,
                                         item_stat_value6,
                                         item_stat_type7,
                                         item_stat_value7,
                                         item_stat_type8,
                                         item_stat_value8,
                                         item_stat_type9,
                                         item_stat_value9,
                                         item_stat_type10,
                                         item_stat_value10,
                                         item_ScaledStatsDistributionID,
                                         item_ScaledStatsDistributionFlags,
                                         item_dmg_min1,
                                         item_dmg_max1,
                                         item_dmg_type1,
                                         item_dmg_min2,
                                         item_dmg_max2,
                                         item_dmg_type2,
                                         item_armor,
                                         item_holy_res,
                                         item_fire_res,
                                         item_nature_res,
                                         item_frost_res,
                                         item_shadow_res,
                                         item_arcane_res,
                                         item_delay,
                                         item_ammo_type,
                                         item_range,
                                         item_spellid_1,
                                         item_spelltrigger_1,
                                         item_spellcharges_1,
                                         item_spellcooldown_1,
                                         item_spellcategory_1,
                                         item_spellcategorycooldown_1,
                                         item_spellid_2,
                                         item_spelltrigger_2,
                                         item_spellcharges_2,
                                         item_spellcooldown_2,
                                         item_spellcategory_2,
                                         item_spellcategorycooldown_2,
                                         item_spellid_3,
                                         item_spelltrigger_3,
                                         item_spellcharges_3,
                                         item_spellcooldown_3,
                                         item_spellcategory_3,
                                         item_spellcategorycooldown_3,
                                         item_spellid_4,
                                         item_spelltrigger_4,
                                         item_spellcharges_4,
                                         item_spellcooldown_4,
                                         item_spellcategory_4,
                                         item_spellcategorycooldown_4,
                                         item_spellid_5,
                                         item_spelltrigger_5,
                                         item_spellcharges_5,
                                         item_spellcooldown_5,
                                         item_spellcategory_5,
                                         item_spellcategorycooldown_5,
                                         item_bonding,
                                         item_description,
                                         item_page_id,
                                         item_page_language,
                                         item_page_material,
                                         item_quest_id,
                                         item_lock_id,
                                         item_lock_material,
                                         item_sheathID,
                                         item_randomprop,
                                         item_randomsuffix,
                                         item_block,
                                         item_itemset,
                                         item_bagfamily,
                                         item_TotemCategory,
                                         item_socket_color_1,
                                         item_unk201_3,
                                         item_socket_color_2,
                                         item_unk201_5,
                                         item_socket_color_3,
                                         item_unk201_7,
                                         item_socket_bonus,
                                         item_GemProperties,
                                         item_ReqDisenchantSkill,
                                         item_ArmorDamageModifier,
                                         item_ExistingDuration,
                                         item_ItemLimitCategoryId,
                                         item_HolidayId)
            self.witems[item_entry] = item
                       
            p.update_time(entry)
            if str(p) != pold:
                frostlib.nout(str(p))
                pold = str(p)
        #print self.witems
    def load_creatures(self):
        resultcount = self.cursor.execute("SELECT * FROM creature_template")
        p = frostlib.ProgressBar(int(resultcount), "Loading Creature Template...")
        pold = str(p)
        result = self.cursor.fetchall()
        for entry in range(0,resultcount):
            currentres = result[entry]
            creature_entry = int(currentres[0])
            creature_name = str(currentres[1])
            creature_subname = str(currentres[2])
            creature_info_str = currentres[3]
            creature_flags1 = int(currentres[4])
            creature_type = int(currentres[5])
            creature_family = int(currentres[6])
            creature_rank = int(currentres[7])
            creature_killcredit1 = int(currentres[8])
            creature_killcredit2 = int(currentres[9])
            creature_male_displayid = int(currentres[10])
            creature_female_displayid = int(currentres[11])
            creature_male_displayid2 = int(currentres[12])
            creature_female_displayid2 = int(currentres[13])
            creature_unknown_float1 = float(currentres[14])
            creature_unknown_float2 = float(currentres[15])
            creature_leader = int(currentres[16])
            creature_questitem1 = int(currentres[17])
            creature_questitem2 = int(currentres[18])
            creature_questitem3 = int(currentres[19])
            creature_questitem4 = int(currentres[20])
            creature_questitem5 = int(currentres[21])
            creature_questitem6 = int(currentres[22])
            creature_pathid = int(currentres[23])
            creature = frostlib.classes.creature(creature_entry,
                                                 creature_name,
                                                 creature_subname,
                                                 creature_info_str,
                                                 creature_flags1,
                                                 creature_type,
                                                 creature_family,
                                                 creature_rank,
                                                 creature_killcredit1,
                                                 creature_killcredit2,
                                                 creature_male_displayid,
                                                 creature_female_displayid,
                                                 creature_male_displayid2,
                                                 creature_female_displayid2,
                                                 creature_unknown_float1,
                                                 creature_unknown_float2,
                                                 creature_leader,
                                                 creature_questitem1,
                                                 creature_questitem2,
                                                 creature_questitem3,
                                                 creature_questitem4,
                                                 creature_questitem5,
                                                 creature_questitem6,
                                                 creature_pathid)

            self.wcreatures[creature_entry] = creature
            
            p.update_time(entry)
            if str(p) != pold:
                frostlib.nout(str(p))
                pold = str(p)
                        
    def loaditems_localized(self):
        resultcount_de = int(self.cursor.execute("SELECT * FROM items_localized_de"))
        result_de = self.cursor.fetchall()
        resultcount_es = int(self.cursor.execute("SELECT * FROM items_localized_es"))
        result_es = self.cursor.fetchall()
        resultcount_fr = int(self.cursor.execute("SELECT * FROM items_localized_fr"))
        result_fr = self.cursor.fetchall()
        resultcount_ru = int(self.cursor.execute("SELECT * FROM items_localized_ru"))
        result_ru = self.cursor.fetchall()
        resultcount = resultcount_de + resultcount_es + resultcount_fr + resultcount_ru
        helpvar = ""
        p = frostlib.ProgressBar(int(resultcount), "Loading Item Localizations...")
        pold = str(p)
        cur = 0
        for entry in range(0,resultcount_de):
            
            currentres = result_de[entry]
            item_entry = int(currentres[0])
            try:
                self.witems[item_entry].set_localized(currentres[1],currentres[2],currentres[3])
            except:
                helpvar += "Got localized name for item " + str(item_entry) + " , but there is no Item with entry " + str(item_entry) + "\n"
            p.update_time(cur)
            cur += 1
            if str(p) != pold:
                frostlib.nout(str(p))
                pold = str(p)

        for entry in range(0,resultcount_es):
            
            currentres = result_es[entry]
            item_entry = int(currentres[0])
            try:
                self.witems[item_entry].set_localized(currentres[1],currentres[2],currentres[3])
            except:
                helpvar += "Got localized name for item " + str(item_entry) + " , but there is no Item with entry " + str(item_entry) + "\n"
            p.update_time(cur)
            cur += 1
            if str(p) != pold:
                frostlib.nout(str(p))
                pold = str(p)

                
        for entry in range(0,resultcount_fr):
            
            currentres = result_fr[entry]
            item_entry = int(currentres[0])
            try:
                self.witems[item_entry].set_localized(currentres[1],currentres[2],currentres[3])
            except:
                helpvar += "Got localized name for item " + str(item_entry) + " , but there is no Item with entry " + str(item_entry) + "\n"
            p.update_time(cur)
            cur += 1
            if str(p) != pold:
                frostlib.nout(str(p))
                pold = str(p)

        for entry in range(0,resultcount_ru):
            
            currentres = result_ru[entry]
            item_entry = int(currentres[0])
            try:
                self.witems[item_entry].set_localized(currentres[1],currentres[2],currentres[3])
            except:
                helpvar += "Got localized name for item " + str(item_entry) + " , but there is no Item with entry " + str(item_entry) + "\n"
            p.update_time(cur)
            cur += 1
            if str(p) != pold:
                frostlib.nout(str(p))
                pold = str(p)
        
        frostlib.eout(helpvar)
        
    
