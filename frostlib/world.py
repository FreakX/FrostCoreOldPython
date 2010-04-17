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
    def loaditems(self):
        import MySQLdb
        mysql_opts = {
            'host': "localhost",
            'user': "root",
            'pass': "",
            'db':   "fworld"
            }
        mysql = MySQLdb.connect(mysql_opts['host'], mysql_opts['user'], mysql_opts['pass'], mysql_opts['db']) 
        mysql.apilevel = "2.0"
        mysql.threadsafety = 2
        mysql.paramstyle = "format"
        cursor = mysql.cursor()
        resultcount = cursor.execute("SELECT * FROM item_template")
        result = cursor.fetchall()
        for entry in xrange(0,resultcount):
            item_entry = int (result[entry][0])
            item_class = int (result[entry][1])
            item_subclass = int (result[entry][2])
            item_field4 = int(result[entry][3])
            item_name1 = result[entry][4]
            item_displayid = int(result[entry][5])
            item_quality = int(result[entry][6])
            item_flags = int(result[entry][7])
            item_buyprice = int(result[entry][8])
            item_sellprice = int(result[entry][9])
            item_inventorytype = int(result[entry][10])
            item_allowableclass = int(result[entry][11])
            item_allowablerace = int(result[entry][12])
            item_itemlevel = int(result[entry][13])
            item_requiredlevel = int(result[entry][14])
            item_RequiredSkill = int(result[entry][15])
            item_RequiredSkillRank = int(result[entry][16])
            item_RequiredSpell = int(result[entry][17])
            item_RequiredPlayerRank1 = int(result[entry][18])
            item_RequiredPlayerRank2 = int(result[entry][19])
            item_RequiredFaction = int(result[entry][20])
            item_RequiredFactionStanding = int(result[entry][21])
            item_Unique = int(result[entry][22])
            item_maxcount = int(result[entry][23])
            item_ContainerSlots = int(result[entry][24])
            item_itemstatscount = int(result[entry][25])
            item_stat_type1 = int(result[entry][26])
            item_stat_value1= int(result[entry][27])
            item_stat_type2 = int(result[entry][28])
            item_stat_value2= int(result[entry][29])
            item_stat_type3 = int(result[entry][30])
            item_stat_value3= int(result[entry][31])
            item_stat_type4 = int(result[entry][32])
            item_stat_value4= int(result[entry][33])
            item_stat_type5 = int(result[entry][34])
            item_stat_value5= int(result[entry][35])
            item_stat_type6 = int(result[entry][36])
            item_stat_value6= int(result[entry][37])
            item_stat_type7 = int(result[entry][38])
            item_stat_value7= int(result[entry][39])
            item_stat_type8 = int(result[entry][40])
            item_stat_value8= int(result[entry][41])
            item_stat_type9 = int(result[entry][42])
            item_stat_value9= int(result[entry][43])
            item_stat_type10= int(result[entry][44])
            item_stat_value10=int(result[entry][45])
            item_ScaledStatsDistributionID = int(result[entry][46])
            item_ScaledStatsDistributionFlags=int(result[entry][47])
            item_dmg_min1 = float(result[entry][48])
            item_dmg_max1 = float(result[entry][49])
            item_dmg_type1= int(result[entry][50])
            item_dmg_min2 = float(result[entry][51])
            item_dmg_max2 = float(result[entry][52])
            item_dmg_type2= int(result[entry][53])
            item_armor = int(result[entry][54])
            item_holy_res = int(result[entry][55])
            item_fire_res = int(result[entry][56])
            item_nature_res = int(result[entry][57])
            item_frost_res = int(result[entry][58])
            item_shadow_res= int(result[entry][59])
            item_arcane_res= int(result[entry][60])
            item_delay = int(result[entry][61])
            item_ammo_type= int(result[entry][62])
            item_range = int(result[entry][63])
            item_spellid_1 = int(result[entry][64])
            item_spelltrigger_1 = int(result[entry][65])
            item_spellcharges_1 = int(result[entry][66])
            item_spellcooldown_1= int(result[entry][67])
            item_spellcategory_1= int(result[entry][68])
            item_spellcategorycooldown_1 = int(result[entry][69])
            item_spelltrigger_2 = int(result[entry][70])
            item_spellcharges_2 = int(result[entry][71])
            item_spellcooldown_2= int(result[entry][72])
            item_spellcategory_2= int(result[entry][73])
            item_spellcategorycooldown_2 = int(result[entry][74])
            
                                      
        
    
