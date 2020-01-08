import socket 

##
# rc4 decode
##
import binascii
import hashlib,base64

def rc4(text, key='1'):
#    key=hashlib.md5(key).hexdigest()
    result=''
    key_len=len(key)
    sbox=list(range(256))
    j=0
    for i in range(256):
        j=(j+sbox[i]+ord(key[i%key_len]))%256
        sbox[i],sbox[j]=sbox[j],sbox[i]
    
    i=j=0
#    print(type(text))
#    print(text)
    #print(len(text))
    text=text.decode("utf-8", "ignore")
    #text=str(text, encoding = "utf-8")
    
    #text= bytes.decode(text, encoding="ascii")
#    print(text)
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
    host='0.0.0.0'
    port=1775
    key="1"
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        #s.listen(1)
        print('start...')
        while True:
            msg, addr=s.recvfrom(1024)
            #cl=rc4_crypt(msg, key)
            #print("cl:",cl)
            #bh = bytes2hexstr(cl)
            print("len",len(msg))
            #b64=base64.b64decode(msg)
            #print("b64:",b64)
            print(msg)
            print(type(msg))
#            for i in msg:
#                print("%#x"%ord(i))
            bs=bytesToHexString(msg)
            print(bs)
                      
            ss=bytes.decode(msg)
            h=tohex(ss)
            print("to hex:",h)
            bh = rc4(msg)
            print("rc4 decode is", bh)
#            print("src is", msg)
#            msg.decode('utf-8')
#           tcp
#            conn, addr=s.accept()
#            with conn:
#                print('connectec by' , addr)
#                while (True):
#                    data=conn.recv(1024)
#                    if not data:
#                        break
#                    conn.sendall(data)
#            s.close()


if (__name__ == "__main__"):
    main()
print("ok222")