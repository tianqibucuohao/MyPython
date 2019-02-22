import socket 


def main():
    host=''
    port=8080
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        #s.listen(1)
        conn, addr=s.accept()
        with conn:
            print('connectec by' , addr)
            while (True):
                data=conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
        s.close()


if (__name__ == "__main__"):
    main()
print("ok222")