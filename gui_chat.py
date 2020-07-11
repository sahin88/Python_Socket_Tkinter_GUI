from tkinter import *
import socket
import time
import threading



class Gui(Tk):
    def __init__(self):
        super().__init__()
        
        self.server_name=socket.gethostname()
        self.ip_address=socket.gethostbyname(socket.gethostname())
        self.port=5060
        self.format='utf-8'
        self.connection_detail=(self.ip_address, self.port)
        self.clientSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.clientSocket.connect(self.connection_detail)
        self.title("Connected To Hostname :{} IP_Number :{}".format(self.server_name,self.ip_address))
        self.geometry('425x500') 
        self.chat_screen = Text(self, width=40,fg='red',bg='#40E0D0', font=('Arial',12,'bold'))
        self.chat_screen.grid(row=0, column=0, padx=10, pady=10)
        self.msg_entry = Entry(self, width=30,fg='blue', font=('Halvetica',12,'bold'))
        self.msg_entry.insert(0,"Please Enter your message")
        self.msg_entry.grid(row=1, column=0, padx=10, pady=10)
        self.msg_send_btn = Button(self, text="Send", width=20, command= lambda:self.msg_send_func())
        self.msg_send_btn.grid(row=2, column=0, padx=10, pady=10)
        self.thrd_1 = threading.Thread(target= self.msg_recv_func)
        self.thrd_1.daemon = True
        self.thrd_1.start()
    


    def msg_send_func(self):
        sending_msg = self.msg_entry.get()
        self.clientSocket.send(sending_msg.encode("utf-8"))

       

    def msg_recv_func(self):
        while True:
            coming_msg = self.clientSocket.recv(1024).decode("utf-8")
            self.chat_screen.insert(END, "\n"+coming_msg)
    


hel=Gui()
hel.mainloop()