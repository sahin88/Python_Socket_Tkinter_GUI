import socket
import threading
import time 
PORT=5060
FORMAT='utf-8'
SERVER_NAME=socket.gethostname()
IP_ADRESS=socket.gethostbyname(SERVER_NAME)
ADRESS_DEF=(IP_ADRESS,PORT)
DISCONNECT_MESSAGE='!DISCONECT'
CLIENT_LIST=set()


server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(ADRESS_DEF)

def message_reciv_send(cilentSocket,clientAddress):
    while True:
   
        message=cilentSocket.recv(1024).decode(FORMAT)
        if message:
            
            if message==DISCONNECT_MESSAGE:
                print('{} has left the channel'.format(clientAddress))
                CLIENT_LIST.remove(cilentSocket)

            for cl in CLIENT_LIST:
                #if cl is not cilentSocket:
                cl.send((clientAddress[0] + ":" + str(clientAddress[1]) +" says: "+ message).encode("utf-8"))


def get_start():
    server.listen(2)
    while True: 
        print(' A new User has attented, waits for the client')
        cilentSocket,clientAddress= server.accept()
        #if cilentSocket not in CLIENT_LIST:
        CLIENT_LIST.add(cilentSocket)
        t1= threading.Thread(target= message_reciv_send, args=(cilentSocket,clientAddress))
        t1.start()

get_start()
