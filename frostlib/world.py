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

class world(object):
    def __init__(self,conf):
        self.__conf = conf
        self.__quests = {}
        
    def load_data(self,path): #Load Data is not work correctly
        for questnum in xrange(1, 30):
            try:
                f = open(str(os.getcwd()) + path + str(questnum) + ".fcd", r)
                self.__quests[questnum] = f.readlines()
                f.close()
            except:
                if frostlib.DEBUG_MODE == True:
                    print "Quest " + str(questnum) + " failed loading"
                pass
    def return_quests(self):
        return self.__quests
