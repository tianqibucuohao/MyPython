import socket
import base64

def rc4(text, key="1"):
#    key=hashlib.md5(key).hexdigest()
    result=''
    key_len=len(key)
    sbox=list(range(256))
    #print(sbox)
    j=0
    for i in range(256):
        j=(j+sbox[i]+ord(key[i%key_len]))%256
        sbox[i],sbox[j]=sbox[j],sbox[i]
    
    i=j=0
    
    #text=str(text, encoding = "utf-8")
    #print(text)
    for element in text:
        i = (i+1)%256
        j = (j+sbox[i])%256
        sbox[i],sbox[j] = sbox[j],sbox[i]
        k = chr(ord(element) ^ sbox[(sbox[i]+sbox[j])%256])
        result += k
    return result

def tohex(s):
    return ' '.join([hex(ord(c)).replace('0x', '') for c in s])
    
def bytesToHexString(bs):
    # hex_str = ''
    # for item in bs:
    #     hex_str += str(hex(item))[2:].zfill(2).upper() + " "
    # return hex_str
    return ''.join(['%02X ' % b for b in bs])

def main():
    host="192.168.52.188"
    port=1775
    #with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msg="LOGIN 1824734721 1.0\nusername: web-10\nip:192.168.0.100\ngroups:\nauthway:1024\nmac:000000000000\nhasflow:0\n\n"
    #msg=msg.encode("utf-8")
    print("src len:",len(msg))
    r=rc4(msg)
    #print("rc4 len:",len(r))
    
    b=str.encode(r)
    h=bytesToHexString(b)
    print("tohex:",h)
    #print("utf8 len:",len(b))
    #b=base64.b64encode(b)
    print("base64 len:", len(b))
    print(b)
    #print("=====")
    #print(tohex(b))
    s.sendto(b,(host, port))
#        s.connect((host, port))
#        #s.sendall(b'Hello, world')
#        
#        data = s.recv(1024)
#        print('Received', repr(data))
#        print(type(data))
#        s.send(b'ishare\r\n')
#        data=''
#        data = s.recv(1024)
#        print('Received', repr(data))
#        s.send(b'123\r\n')
#        data = s.recv(1024)
#        
#        print('Received', repr(data))
#        s.send(b'ver\r\n')
#        data=s.recv(1024)
#        print("ver:",data)
    s.close()


if (__name__=="__main__"):
    main()
print("finished...")