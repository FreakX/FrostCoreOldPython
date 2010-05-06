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
class account(object):
    
    def __init__(self,guid,name,password,email,expansion):
        self.__guid = guid
        self.__name = name
        self.__password = password
        self.__email = email
        self.__expansion = expansion
        self.__verify = False

    def getguid(self):
        return self.__guid
    def getname(self):
        return self.__name
    def getpassword(self):
        return self.__password
    def getemail(self):
        return self.__email
    def getexpansion(self):
        return self.__expansion
    def getverify(self):
        return self.__verify

    def verify(self,checkpassword):
        if self.__password == checkpassword:
            self.__verify = True
            return True
        else:
            self.__verify = False
            return False

class character(object):
    def __init__(self, guid, account, name, race, classx, hp, power, equipment, bag, posx, posy, posz, orientation):
        self.__guid = guid
        self.__accountid = account
        self.__name = name
        self.__race = race
        self.__classx = classx
        self.__hp = hp
        self.__power = power
        self.__eq = equipment
        self.__pos = [posx, posy, posz]
        self.__orientation = orientation
        self.__bag = bag
        self.__instance = 0
        self.__instancemode = frostlib.INSTANCE_MODE_10_NORMAL

    def opengossip(self):
        #TODO: Open Gossip Menu Code ( Not Implementet )
        pass # Indented Command, so code is runnable
    def gossipadd(self,gossiptext):
        if gossiptext == "$xx$.$":
            #send "Hello " + self.__name    # Hyphotetic Function
            pass # Indented Command, so code is runnable
        else:
            #send gossiptext                # Hyphotetic Function
            pass # Indented Command, so code is runnable
    def setinstance(self, instance):
        self.__instance = instance

    def setinstancemode(self, instancemode):
        self.__instancemode = instancemode
        

class quest(object):
    def __init__(self, questid, (title_en, title_de, title_fr, title_es), (desc_en, desc_de, desc_fr, desc_es), rewardmoney, rewarditem1, rewarditem2, rewarditem3, rewarditem4, rewarditem5,rewarditem6, choiceitem1, choiceitem2,choiceitem3,choiceitem4,choiceitem5,choiceitem6):
        self.id = questid
        self.title = [title_en, title_de, title_fr, title_es]
        self.desc = [desc_en, desc_de, desc_fr, desc_es]
        self.rewardmoney = rewardmoney
        self.rewarditem = [rewarditem1,rewarditem2,rewarditem3,rewarditem4,rewarditem5,rewarditem6]
        self.choiceitem = [choiceitem1,choiceitem2,choiceitem3,choiceitem4,choiceitem5,choiceitem6]

    def getlocalizedtitle(self, local):
        if local == "en":
            return self.title[0]
        elif local == "de":
            return self.title[1]
        elif local == "fr":
            return self.title[2]
        elif local == "es":
            return self.title[3]

    def getlocalizeddesc(self, local):
        if local == "en":
            return self.desc[0]
        elif local == "de":
            return self.desc[1]
        elif local == "fr":
            return self.desc[2]
        elif local == "es":
            return self.desc[3]
    
    
    
class npc(object):
    def __init__(self, npcid, npcguid):
        #TODO: Load NPC Data from another Class (NPC Instance Class) (Not Implementet yet))
        self.guid = npcguid
        
    def gossip(self, character):
        character.opengossip()
        try:
            for gossip_item in self.gossip_items:
                character.gossipadd(gossip_item)
        except:
            character.gossipadd("$xx$.$") # Special Code for "Hello <name>"


class group(object):
    def __init__(self, leader):
        self.leader = leader
        self.member = [leader]
    def newmember(self, member):
        self.member.append(member)
    def getmember(self):
        return self.member

class instancehandler(object):
    def __init__(self):
        self.instances = []
    def createnewinstance(self, instance):
        instancecount = len(self.instances)
        self.instances.append(instance)
        return instancecount + 1
        
        
class instance(object):
    def __init__(self, mode, group, instancemap, instancehandler):
        self.id = instancehandler.createnewinstance(self)
        self.mode = mode
        self.group = group
        self.map = instancemap
        self.member = []
        self.create()
        

    def create(self):
        groupmember = self.group.getmember()
        for member in groupmember:
            self.member.append(member)
        for member in self.member:
            member.setinstance(self.id)
            member.setinstancemode(self.mode)
class item(object):
    def __init__(self,
                 item_entry,
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
                 item_HolidayId):
        
        self.entry =            item_entry
        self.item_class =            item_class
        self.subclass =         item_subclass
        self.field4 =           item_field4
        self.en_name =          item_name1
        self.displayid =        item_displayid
        self.quality =          item_quality
        self.flags =            item_flags
        self.buyprice =         item_buyprice
        self.sellprice =        item_sellprice
        self.inventorytype =    item_inventorytype
        self.allowableclass =   item_allowableclass
        self.allowablerace =    item_allowablerace
        self.itemlevel =        item_itemlevel
        self.requiredlevel =    item_requiredlevel
        self.RequiredSkill =    item_RequiredSkill
        self.RequiredSkillRank =item_RequiredSkillRank
        self.RequiredSpell =    item_RequiredSpell
        self.RequiredPlayerRank1=item_RequiredPlayerRank1
        self.RequiredPlayerRank2=item_RequiredPlayerRank2
        self.RequiredFaction=   item_RequiredFaction
        self.RequiredFactionStanding=item_RequiredFactionStanding
        self.Unique = item_Unique
        self.maxcount = item_maxcount
        self.ContainerSlots = item_ContainerSlots
        self.itemstatscount = item_itemstatscount
        self.stat_type1 = item_stat_type1
        self.stat_value1= item_stat_value1
        self.stat_type2 = item_stat_type2
        self.stat_value2= item_stat_value2
        self.stat_type3 = item_stat_type3
        self.stat_value3= item_stat_value3
        self.stat_type4 = item_stat_type4
        self.stat_value4= item_stat_value4
        self.stat_type5 = item_stat_type5
        self.stat_value5= item_stat_value5
        self.stat_type6 = item_stat_type6
        self.stat_value6= item_stat_value6
        self.stat_type7 = item_stat_type7
        self.stat_value7= item_stat_value7
        self.stat_type8 = item_stat_type8
        self.stat_value8= item_stat_value8
        self.stat_type9 = item_stat_type9
        self.stat_value9= item_stat_value9
        self.stat_type10= item_stat_type10
        self.stat_value10=item_stat_value10
        self.ScaledStatsDistributionID = item_ScaledStatsDistributionID
        self.ScaledStatsDistributionFlags=item_ScaledStatsDistributionFlags
        self.dmg_min1 = item_dmg_min1
        self.dmg_max1 = item_dmg_max1
        self.dmg_type1= item_dmg_type1
        self.dmg_min2 = item_dmg_min2
        self.dmg_max2 = item_dmg_max2
        self.dmg_type2= item_dmg_type2
        self.armor = item_armor
        self.holy_res = item_holy_res
        self.fire_res = item_fire_res
        self.nature_res = item_nature_res
        self.frost_res = item_frost_res
        self.shadow_res= item_shadow_res
        self.arcane_res= item_arcane_res
        self.delay = item_delay
        self.ammo_type= item_ammo_type
        self.range = item_range
        self.spellid_1 = item_spellid_1
        self.spelltrigger_1 = item_spelltrigger_1
        self.spellcharges_1 = item_spellcharges_1
        self.spellcooldown_1= item_spellcooldown_1
        self.spellcategory_1= item_spellcategory_1
        self.spellcategorycooldown_1 = item_spellcategorycooldown_1
        self.spellid_2 = item_spellid_2
        self.spelltrigger_2 = item_spelltrigger_2
        self.spellcharges_2 = item_spellcharges_2
        self.spellcooldown_2= item_spellcooldown_2
        self.spellcategory_2= item_spellcategory_2
        self.spellcategorycooldown_2 = item_spellcategorycooldown_2
        self.spellid_3 = item_spellid_3 
        self.spelltrigger_3 = item_spelltrigger_3
        self.spellcharges_3 = item_spellcharges_3
        self.spellcooldown_3 = item_spellcooldown_3
        self.spellcategory_3 = item_spellcategory_3
        self.spellcategorycooldown_3 = item_spellcategorycooldown_3
        self.spellid_4 = item_spellid_4
        self.spelltrigger_4 = item_spelltrigger_4
        self.spellcharges_4 = item_spellcharges_4
        self.spellcooldown_4 = item_spellcooldown_4
        self.spellcategory_4 = item_spellcategory_4
        self.spellcategorycooldown_4 = item_spellcategorycooldown_4
        self.spellid_5 = item_spellid_5
        self.spelltrigger_5 = item_spelltrigger_5
        self.spellcharges_5 = item_spellcharges_5
        self.spellcooldown_5 = item_spellcooldown_5
        self.spellcategory_5 = item_spellcategory_5
        self.spellcategorycooldown_5 = item_spellcategorycooldown_5
        self.bonding = item_bonding
        self.en_description = item_description
        self.page_id = item_page_id
        self.page_language = item_page_language
        self.page_material = item_page_material
        self.quest_id = item_quest_id
        self.lock_id = item_lock_id
        self.lock_material = item_lock_material
        self.sheathID = item_sheathID
        self.randomprop = item_randomprop
        self.randomsuffix = item_randomsuffix
        self.block = item_block
        self.itemset = item_itemset
        self.bagfamily = item_bagfamily
        self.TotemCategory = item_TotemCategory
        self.socket_color_1 = item_socket_color_1
        self.unk201_3 = item_unk201_3
        self.socket_color_2 = item_socket_color_2
        self.unk201_5 = item_unk201_5
        self.socket_color_3 = item_socket_color_3
        self.unk201_7 = item_unk201_7
        self.socket_bonus = item_socket_bonus
        self.GemProperties = item_GemProperties
        self.ReqDisenchantSkill = item_ReqDisenchantSkill
        self.ArmorDamageModifier = item_ArmorDamageModifier
        self.ExistingDuration = item_ExistingDuration
        self.ItemLimitCategoryId = item_ItemLimitCategoryId
        self.HolidayId = item_HolidayId
        
    def set_localized(self,langcode,langname,langdesc):
        if langcode == "deDE":
            self.de_name = langname
            self.de_description = langdesc
        elif langcode == "esES":
            self.es_name = langname
            self.es_description = langdesc
        elif langcode == "ruRU":
            self.ru_name = langname
            self.ru_description = langdesc
        elif langcode == "frFR":
            self.fr_name = langname
            self.fr_description = langdesc
        else:
            frostlib.dout("Undefined Language Code: " + str(langcode))

    def getlocalizedname(self, lang):
        try:
            if lang == "enUS":
                return self.en_name
            elif lang == "deDE":
                return self.de_name
            elif lang == "esES":
                return self.es_name
            elif lang == "frFR":
                return self.fr_name
            elif lang == "ruRU":
                return self.ru_name
        except NameError:
            return self.en_name

    def getlocalizeddesciption(self, lang):
        try:
            if lang == "enUS":
                return self.en_description
            elif lang == "deDE":
                return self.de_description
            elif lang == "esES":
                return self.es_description
            elif lang == "frFR":
                return self.fr_description
            elif lang == "ruRU":
                return self.ru_description
        except NameError:
            return self.en_description
            
                


class creature(object):
    def __init__(self,
                 creature_entry,
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
                 creature_pathid):

        self.entry = creature_entry
        self.en_name = creature_name
        self.en_subname = creature_subname
        self.info_str = creature_info_str
        self.flags1 = creature_flags1
        self.type = creature_type
        self.family = creature_family
        self.rank = creature_rank
        self.killcredit1 = creature_killcredit1
        self.killcredit2 = creature_killcredit2
        self.male_displayid = creature_male_displayid
        self.female_displayid = creature_female_displayid
        self.male_displayid2 = creature_male_displayid2
        self.female_displayid2 = creature_female_displayid2
        self.unknown_float1 = creature_unknown_float1
        self.unknown_float2 = creature_unknown_float2
        self.leader = creature_leader
        self.questitem1 = creature_questitem1
        self.questitem2 = creature_questitem2
        self.questitem3 = creature_questitem3
        self.questitem4 = creature_questitem4
        self.questitem5 = creature_questitem5
        self.questitem6 = creature_questitem6
        self.pathid = creature_pathid

    def set_localized(self,langcode,langname,langsubname):
        if langcode == "deDE":
            self.de_name = langname
            self.de_subname = langsubname
        elif langcode == "esES":
            self.es_name = langname
            self.es_subname = langsubname
        elif langcode == "ruRU":
            self.ru_name = langname
            self.ru_subname = langsubname
        elif langcode == "frFR":
            self.fr_name = langname
            self.fr_subname = langsubname
        else:
            frostlib.dout("Undefined Language Code: " + str(langcode))

    def getlocalizedname(self, lang):
        try:
            if lang == "enUS":
                return self.en_name
            elif lang == "deDE":
                return self.de_name
            elif lang == "esES":
                return self.es_name
            elif lang == "frFR":
                return self.fr_name
            elif lang == "ruRU":
                return self.ru_name
        except NameError:
            return self.en_name

    def getlocalizedsubname(self, lang):
        try:
            if lang == "enUS":
                return self.en_subname
            elif lang == "deDE":
                return self.de_subname
            elif lang == "esES":
                return self.es_subname
            elif lang == "frFR":
                return self.fr_subname
            elif lang == "ruRU":
                return self.ru_subname
        except NameError:
            return self.en_subname

class creature_instance(object):
    def __init__(self, creatureobject, xpos, ypos, zpos, size):
        self.creatureobject = creatureobject
        self.xpos = xpos
        self.ypos = ypos
        self.zpos = zpos
        self.size = size
    
    def getlocalizedname(self, lang):
        return self.creatureobject.getlocalizedname(lang)
    def getlocalizedsubname(self, lang):
        return self.creatureobject.getlocalizedsubname(lang)

    def setscript(self, scriptname):
        if scriptname == "boss_lichking":
            self.script = frostlib.creaturescripts.icecrown.lichking()
        elif scriptname == "boss_illidan":
            self.script = frostlib.creaturescripts.blacktemple.illidan()
            

class script_text(object):
    def __init__(self, script_id, script_text):
        self.en_text = script_text
        self.script_text_id = script_id

    def set_lang(self, script_lang, script_text):
        if script_lang == "deDE":
            self.de_text = script_text

        elif script_lang == "esES":
            self.es_text = script_text

        elif script_lang == "frFR":
            self.fr_text = script_text

        elif script_lang == "ruRU":
            self.ru_text = script_text

        else:
            frostlib.dout("Undefined Language Code: " + str(script_lang))
        
    def getlocalizedtext(self, lang):
        try:
            if lang == "enUS":
                return self.en_text
            elif lang == "deDE":
                return self.de_text
            elif lang == "esES":
                return self.es_text
            elif lang == "frFR":
                return self.fr_text
            elif lang == "ruRU":
                return self.ru_text
        except NameError:
            return self.en_text

class bag(object):
    def __init__(self):
        self.bag = {}
        maxslots = 0
        for x in xrange(0,500):
            self.bag[x] = False
    def insert(self, slot, item):
        self.bag[slot] = item

    
        
        
        
