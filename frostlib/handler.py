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
import binascii
import frostlib

def datareturn(data):
    return binascii.unhexlify(data)
def getdata(data,fromblock,toblock, reverse=True):
    result = []
    for x in range(fromblock,toblock+1):
        block = data[(x-1)*2:x*2]
        result.append(block)
    if reverse == True:
        result.reverse()
    return result

def logonhandler(data):
    try:
        opcode = int("".join(getdata(data.encode("hex"),1,1)),16) # Finding Opcode

        if opcode == 0: #AUTHENTICATION_LOGON_CHALLENGE

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
            #if frostlib.CLIENT_AUTH_INFO == True:
            if True:
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
                #return datareturn("00000013db7112721b91e37fffb0525f8869dff46b8168d564e2595ff2fa11a141a42e010720b79b3e2a87823cab8f5ebfbf8eb10108535006298b5badbd5b53e1895e644b89cd3010ede00281e26c03cd5a8cfb7c5d36c6f9cc36d2e176532bdaa4f304cbd3e9cbbc9d4234009a98ebdb40db99f39500")
                return datareturn("000002")
            else:
                print "False Client Version"
                return "error"


        elif opcode == 1: #AUTHENTICATION PROOF
            return datareturn("01007adff8d407916f53529440a778eea9d6b64db91000008000000000000000")


            
        else:
            return "error"












    except:
        traceback.print_exc(file=frostlib.logfile)
        return "error"


