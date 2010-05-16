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
INI_FILE_WORLD = "world.cfg"
INI_FILE_LOGON = "logon.cfg"
import ConfigParser


def loadlogonconf():
    config = ConfigParser.ConfigParser()
    config.read(INI_FILE_LOGON)
    
    ## MAIN cfg ##
    frostlib.FROSTLIB_HASH =            config.get("MAIN", "FROSTLIB_HASH")
    frostlib.LOG_LEVEL =                config.get("MAIN", "LOG_LEVEL")
    frostlib.DEBUG_MODE =               config.get("MAIN", "DEBUG_MODE")
    frostlib.CONNECTION_INFO =          config.get("MAIN", "CONNECTION_INFO")
    frostlib.CONNECTION_INFO_DELAY =    config.get("MAIN", "CONNECTION_INFO_DELAY")
    frostlib.CLIENT_AUTH_INFO =         config.get("MAIN", "CLIENT_AUTH_INFO")
    frostlib.AUTHBUILD_ACCEPT =         config.get("MAIN", "AUTHBUILD_ACCEPT")

    ## LOGON DB cfg ##
    frostlib.LOGON_HOST =            config.get("LOGON_DB", "DB_HOST")
    frostlib.LOGON_USER =            config.get("LOGON_DB", "DB_USER")
    frostlib.LOGON_PASS =            config.get("LOGON_DB", "DB_PASS")
    frostlib.LOGON_DB =              config.get("LOGON_DB", "DB_DB")
    
def loadworldconf():
    config = ConfigParser.ConfigParser()
    config.read(INI_FILE_WORLD)

    ## MAIN cfg ##
    frostlib.FROSTLIB_HASH =            config.get("MAIN", "FROSTLIB_HASH")
    frostlib.LOG_LEVEL =                config.get("MAIN", "LOG_LEVEL")
    frostlib.DEBUG_MODE =               config.get("MAIN", "DEBUG_MODE")
    frostlib.CONNECTION_INFO =          config.get("MAIN", "CONNECTION_INFO")
    frostlib.CONNECTION_INFO_DELAY =    config.get("MAIN", "CONNECTION_INFO_DELAY")
    frostlib.CLIENT_AUTH_INFO =         config.get("MAIN", "CLIENT_AUTH_INFO")
    frostlib.AUTHBUILD_ACCEPT =         config.get("MAIN", "AUTHBUILD_ACCEPT")

    ## LOGON DB cfg ##
    frostlib.LOGON_HOST =            config.get("LOGON_DB", "DB_HOST")
    frostlib.LOGON_USER =            config.get("LOGON_DB", "DB_USER")
    frostlib.LOGON_PASS =            config.get("LOGON_DB", "DB_PASS")
    frostlib.LOGON_DB =              config.get("LOGON_DB", "DB_DB")

    ## WORLD DB cfg ##

    frostlib.WORLD_HOST =            config.get("WORLD_DB", "DB_HOST")
    frostlib.WORLD_USER =            config.get("WORLD_DB", "DB_USER")
    frostlib.WORLD_PASS =            config.get("WORLD_DB", "DB_PASS")
    frostlib.WORLD_DB =              config.get("WORLD_DB", "DB_DB")
    
