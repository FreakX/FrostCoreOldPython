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
# World Class
import frostlib
import time
import ItemHandler
import CreatureHandler
import ScriptHandler
import PlayerHandler
import BagHandler
import TerrainHandler

class world(ItemHandler.ItemHandler,
            CreatureHandler.CreatureHandler,
            ScriptHandler.ScriptHandler,
            PlayerHandler.PlayerHandler,
            BagHandler.BagHandler,
            TerrainHandler.TerrainHandler):
    """ World Object, Steuert alle Vorgänge """
    def __init__(self):
        self.witems = {}
        self.wcreatures = {}
        self.wscripts = []
        self.wscript_texts = {}
        self.numscripts = 1
    
        
    def update_player(self):
        """ Update Player """
        # Player Update Code
        pass
    def update_scripts(self):
        """ Update Scripts """
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
        """
        Stellt eine Datenbankverbindung her
        """
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

        
    
