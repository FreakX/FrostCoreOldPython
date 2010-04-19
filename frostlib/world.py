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

class world(object):
    def __init__(self):
        self.witems = {}
    def connect_mysql(self):
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
            
    def loaditems_localized(self):
        resultcount = self.cursor.execute("SELECT * FROM items_localized")
        p = frostlib.ProgressBar(int(resultcount), "Loading Item Localizations...")
        pold = str(p)
        result = self.cursor.fetchall()
        #print result
        helpvar = ""
        for entry in range(0,resultcount):
            
            currentres = result[entry]
            item_entry = int(currentres[0])
            try:
                self.witems[item_entry].set_localized(currentres[1],currentres[2],currentres[3])
            except:
                helpvar += "Got localized name for item " + str(item_entry) + " , but there is no Item with entry " + str(item_entry) + "\n"
            p.update_time(entry)
            if str(p) != pold:
                frostlib.nout(str(p))
                pold = str(p)
        frostlib.dout(helpvar)
        
    
