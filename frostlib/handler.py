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
AuthCmd = {
"AUTH_LOGON_CHALLENGE" : 0x00,
"AUTH_LOGON_PROOF" : 0x01,
"AUTH_RECONNECT_CHALLENGE" : 0x02,
"AUTH_RECONNECT_PROOF" : 0x03,
"REALM_LIST" : 0x10,
"XFER_INITIATE" : 0x30,
"XFER_DATA" : 0x31,
"XFER_ACCEPT" : 0x32,
"XFER_RESUME" : 0x33,
"XFER_CANCEL" : 0x34
}

import Constants
import frostlib
def getdata(data,fromblock,toblock, reverse=True):
    result = []
    for x in range(fromblock,toblock+1):
        block = data[(x-1)*2:x*2]
        result.append(block)
    if reverse == True:
        result.reverse()
    return result

def logonhandler(data):
    
    opcode = int("".join(getdata(data.encode("hex"),1,1)),16) # Finding Opcode

    if opcode == AuthCmd["AUTH_LOGON_CHALLENGE"]: #AUTHENTICATION_LOGON_CHALLENGE

        data = data.encode("hex")
        client_error = int("".join(getdata(data,2,2)),16)
        client_packet_size = int("".join(getdata(data,3,4)), 16)
        client_gamename = "".join(getdata(data,5,8)).decode("hex")
        client_version_1 = int("".join(getdata(data,9,9)), 16)
        client_version_2 = int("".join(getdata(data,10,10)), 16)
        client_version_3 = int("".join(getdata(data,11,11)), 16)
        client_build = int("".join(getdata(data,12,13)), 16)
        client_bit = "".join(getdata(data,14,17)).decode("hex")
        client_os = "".join(getdata(data,18,21)).decode("hex")
        client_country = "".join(getdata(data,22,25)).decode("hex")
        client_timezone = int("".join(getdata(data,26,29)), 16)
        client_name_size = int("".join(getdata(data,34,34)), 16)
        client_name = "".join(getdata(data,35,34 + client_name_size, reverse = False)).decode("hex")
        if frostlib.CLIENT_AUTH_INFO == True:
            print "Error:   " + str(client_error)
            print "Size:    " + str(client_packet_size)
            print "Game:    " + str(client_gamename)
            print "Version: " + str(client_version_1) + "." + str(client_version_2) + "." + str(client_version_3)
            print "Build:   " + str(client_build)
            print "Platform:" + str(client_bit)
            print "OS:      " + str(client_os)
            print "Country: " + str(client_country)
            print "Timezone:" + str(client_timezone)
            print "Account: " + str(client_name)
        elif frostlib.CLIENT_AUTH_INFO == False:
            print "[AUTH] with Clientbuild " + str(client_build)
        if str(client_build) == str(frostlib.AUTHBUILD_ACCEPT):
            packet = []
            packet.append("00")
            packet.append("00")
            packet.append("02")
            #packet.append(str(Constants.AuthResult["WOW_FAIL_BANNED"]))
            
            
            result = []
            for x in packet:
                result.append(str(x))
                
            return "".join(result)
        else:
            print "False Client Version"
            return "error"


    elif opcode == 1: #AUTHENTICATION PROOF
        print "Auth Proof"


        
    else:
        return "error"


