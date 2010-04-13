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

        
        
        
        
    
