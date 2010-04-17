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
if __name__ != '__main__':
    import classes
    import config
    import opcodes
    import world
    import handler
    import wowmath
    import hash
    import time
LOG_LEVEL = 1                # 0 = Normal | 1 = Debug | 2 = Erweitertes Debug | 3 = Alles
DEBUG_MODE = True            # Debug Mode True|False
RELEASE_TYPE = "PRE-ALPHA"   # Current Realease Type Alpha|Beta|Release
REVISION = 4                 # FrostCore Revision
CONNECTION_INFO = True       # Define if Connection Info Is shown
CONNECTION_INFO_DELAY = 30   # Seconds between Connection Info
CLIENT_AUTH_INFO = True      # Show Client Info on Connect True|False
AUTHBUILD_ACCEPT = 11723
HASH = ""
TIME_SECOND = 1
TIME_MINUTE = TIME_SECOND * 60
TIME_HOUR = TIME_MINUTE * 60
TIME_DAY = TIME_HOUR * 24
TIME_MONTH = TIME_DAY * 30
TIME_YEAR = TIME_MONTH * 12
def shutdown():
    print "Schutdown in 5"
    time.sleep(1)
    print "Schutdown in 4"
    time.sleep(1)
    print "Schutdown in 3"
    time.sleep(1)
    print "Schutdown in 2"
    time.sleep(1)
    print "Schutdown in 1"
    time.sleep(1)
    exit()

def nout(out):
    print out

def dout(out):
    if LOG_LEVEL >= 1:
        print out
        
def edout(out):
    if LOG_LEVEL >= 2:
        print out
def eout(out):
    if LOG_LEVEL >= 3:
        print out
