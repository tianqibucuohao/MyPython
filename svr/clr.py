import socket


def main():
    host="192.168.52.149"
    port=23
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        #s.sendall(b'Hello, world')
        
        data = s.recv(1024)
        print('Received', repr(data))
        print(type(data))
        s.send(b'ishare\r\n')
        data=''
        data = s.recv(1024)
        print('Received', repr(data))
        s.send(b'123\r\n')
        data = s.recv(1024)
        
        print('Received', repr(data))
        s.send(b'ver\r\n')
        data=s.recv(1024)
        print("ver:",data)
    s.close()


if (__name__=="__main__"):
    main()
print("finished...")