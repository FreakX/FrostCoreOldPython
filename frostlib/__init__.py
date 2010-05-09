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
    import world
    sworld = world.world()
    import classes
    import config
    import opcodes
    import handler
    import wowmath
    import scripts
    import hash
    import time
    import frostlib
LOG_LEVEL = 3                # 0 = Normal | 1 = Debug | 2 = Erweitertes Debug | 3 = Alles
DEBUG_MODE = True            # Debug Mode True|False
RELEASE_TYPE = "PRE-ALPHA"   # Current Realease Type Alpha|Beta|Release
REVISION = 4                 # FrostCore Revision
CONNECTION_INFO = True       # Define if Connection Info Is shown
CONNECTION_INFO_DELAY = 30   # Seconds between Connection Info
CLIENT_AUTH_INFO = True      # Show Client Info on Connect True|False
AUTHBUILD_ACCEPT = 11723
HASH = ""

maxscriptdelay = 0.1
MYSQL_WORLD_HOST = ""
MYSQL_WORLD_USER = ""
MYSQL_WORLD_PW = ""
MYSQL_WORLD_DB = ""
TIME_SECOND = 1
TIME_MINUTE = TIME_SECOND * 60
TIME_HOUR = TIME_MINUTE * 60
TIME_DAY = TIME_HOUR * 24
TIME_MONTH = TIME_DAY * 30
TIME_YEAR = TIME_MONTH * 12


def shutdown():
    nout("Schutdown in 10")
    time.sleep(1)
    nout("Schutdown in 9")
    time.sleep(1)
    nout("Schutdown in 8")
    time.sleep(1)
    nout("Schutdown in 7")
    time.sleep(1)
    nout("Schutdown in 6")
    time.sleep(1)
    nout("Schutdown in 5")
    time.sleep(1)
    nout("Schutdown in 4")
    time.sleep(1)
    nout("Schutdown in 3")
    time.sleep(1)
    nout("Schutdown in 2")
    time.sleep(1)
    nout("Schutdown in 1")
    time.sleep(1)
    logfile.close()
    exit()
logfile = open("log.txt", "w")
def nout(out):
    print out
    logfile.write(out + "\n")

def dout(out):
    if LOG_LEVEL >= 1:
        print out
        logfile.write(out + "\n")
        
def edout(out):
    if LOG_LEVEL >= 2:
        print out
        logfile.write(out + "\n")
        
def eout(out):
    if LOG_LEVEL >= 3:
        print out
        logfile.write(out + "\n")


class ProgressBar:
    def __init__(self, duration, text):
        self.duration = duration
        self.prog_bar = '[]'
        self.text = text
        self.fill_char = '='
        self.width = 40
        self.__update_amount(0)
   
    def __update_amount(self, new_amount):
        percent_done = int(round((new_amount / 100.0) * 100.0))
        all_full = self.width - 2
        num_hashes = int(round((percent_done / 100.0) * all_full))
        self.prog_bar = '[' + self.fill_char * num_hashes + ' ' * (all_full - num_hashes) + ']'
        pct_place = (len(self.prog_bar) / 2) - len(str(percent_done))
        pct_string = '%i%%' % percent_done
        self.prog_bar = self.prog_bar[0:pct_place] + \
            (pct_string + self.prog_bar[pct_place + len(pct_string):])
       
    def update_time(self, elapsed_secs):
        self.__update_amount((elapsed_secs / float(self.duration)) * 100.0)
        self.prog_bar += "  " + str(self.text)

    def __str__(self):
        return str(self.prog_bar)
       


