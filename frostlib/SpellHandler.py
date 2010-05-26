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

class SpellHandler(object):
    def GetSpell(self,spellid):
        for case in frostlib.switch(spellid):
            if case(1):
                frostlib.logger("Spell 1")
                return "spell1"
            if case(2):
                frostlib.logger("Spell 2")
                return "spell2"
            if case(3):
                frostlib.logger("Spell 3")
                return "spell3"
            if case(4):
                frostlib.logger("Spell 4")
                return "spell4"                
            if case(5):
                frostlib.logger("Spell 5")
                return "spell5"
            if case(6):
                frostlib.logger("Spell 6")
                return "spell6"
            if case(7):
                frostlib.logger("Spell 7")
                return "spell7"
            if case(8):
                frostlib.logger("Spell 8")
                return "spell8"
            if case(9):
                frostlib.logger("Spell 9")
                return "spell9"
            
            
