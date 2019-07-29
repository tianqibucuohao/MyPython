"""

"""

import uuid
import os
import re

def GetMac(adp):
    #mac1=uuid.UUID(int = uuid.getnode()).hex[-12:].upper()
    #print(mac1)
    #return "".join([mac[e:e+2] for e in range(0,11,2)])
    #return "000C298E72CB"
    if (adp == ""):
    	adp = "eth0"
    #print adp
    cmd=os.popen("ifconfig")
    data=cmd.read()
    cmd.close()
    #print data

    mat=adp+"\s*Link encap:\S*\s*HWaddr\s*\S*"
    ret=re.findall(mat,data)
    if (ret):
        mac=ret[0].split(' ')[-1].upper()
        #print("re:",mac)
        return "".join([mac[e:e+2] for e in range(0,18,3)])
    else:
        return ""
    
if (__name__ == "__main__"):
	adp=""
	mac=GetMac(adp)
	print( mac)
	