from tkinter import *
from socket import *
from threading import *


serverIP = "127.0.0.1"

def CallServer() :
    from subprocess import call
    call(["python", "Merged_Server/Merged_Server.py"])

Server_thread = Thread (target= CallServer)

# create root window
root = Tk()
root.title("Network Task Automator")
canvas1 = Canvas(root, width=700, height=100, relief='raised')
canvas1.pack()

Welcome_lbl = Label(root, text = "Welcome", font=('helvetica', 20) )
canvas1.create_window(350, 50, window=Welcome_lbl)
Server_thread.start()

#PORTS
StatPort = 13000
AudioPort = 13001
RenamePort = 13002
EquationsPort = 5050 
ConfigurationPort = 5060
AlarmPort = 12000


# entry2 = Entry(root)
# entry2.pack()

# def entryfunc ():
#     AlarmSocket = socket(AF_INET, SOCK_STREAM)
#     AlarmSocket.connect((serverIP,AlarmPort))

#     print("inside function")
#     print(f"{entry2.get()}")
#     #Socket for NETWORK ALARM client
#     print("Client is ready to send")
#     AlarmSocket.send(bytes(entry2.get(),"utf-8"))
#     AlarmSocket.close()

# submitbtn =  Button(root, text="Get Input", command=lambda:entryfunc())
# submitbtn.pack()

def NetworkAlarm():
    root.iconify()
    Network_window = Toplevel()
    Network_window.title("Convert Image")
    Network_window.geometry("700x600")

    entry = Entry(Network_window)
    entry.pack()

    
    def getPortNumber(PortNumber):
        AlarmSocket = socket(AF_INET, SOCK_STREAM)
        AlarmSocket.connect((serverIP,AlarmPort))
        print("inside function")
        print(f"{PortNumber}")
        #Socket for NETWORK ALARM client
        
        print("Client is ready to send")
        AlarmSocket.send(bytes(PortNumber,"utf-8"))
        AlarmSocket.close()

    submit = Button(Network_window, text="Get Input", command=lambda:getPortNumber(entry.get()))
    submit.pack()

    def BackCommand():
        Network_window.destroy()
        root.deiconify()

    back_button = Button(Network_window, text="Back", command=BackCommand)
    back_button.pack()

def Equations():
    root.iconify()
    Equations_window = Toplevel()
    Equations_window.title("Network Equations")
    Equations_window.geometry("700x600")

    HEADER = 64 #how many bytes we will gonna receive are specified in the header
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE="!DISCONNECT"
    def send(L, R, label):
        print (L,R)

        client = socket(AF_INET, SOCK_STREAM) #creating socket (family,type)
        client.connect((serverIP,EquationsPort))
        
        client.sendall(str.encode("\n".join([str(L), str(R)])))
        # client.send(bytes(L,"utf-8"))
        # client.send(bytes(R, "utf-8"))

        Trans = client.recv(2048).decode(FORMAT)
        print(Trans)
        if Trans != '0' :
            label.config(text= Trans)
        client.close()

    def total(tran,prop,labelT):
        # print(client1_lbl.cget("text"))
        total = float(client1_lbl.cget("text"))+float(client_lbl2.cget("text"))
        if total != '0' :
            labelT.config(text= total)
    
    entryL = Entry(Equations_window)
    entryL.pack()
    # submitL = Button(Equations_window, text="send length of bits", command=lambda:send(entryL.get()))
    # submitL.pack()
    entryR = Entry(Equations_window)
    entryR.pack()
    submitR = Button(Equations_window, text="calculate transmisstion delay", command=lambda:send(entryL.get(),entryR.get(), client1_lbl))
    submitR.pack()
    client1_lbl = Label(Equations_window, text = "", font=('helvetica', 16) )
    client1_lbl.pack()

    entryD = Entry(Equations_window)
    entryD.pack()
    entryS = Entry(Equations_window)
    entryS.pack()
    submitP = Button(Equations_window, text="calculate Prop delay", command=lambda:send(entryD.get(),entryS.get(), client_lbl2))
    submitP.pack()
    client_lbl2 = Label(Equations_window, text = "", font=('helvetica', 16) )
    client_lbl2.pack()

    submitT = Button(Equations_window, text="calculate Total delay", command=lambda:total(client_lbl2,client1_lbl,client_lbl3))
    submitT.pack()
    client_lbl3 = Label(Equations_window, text = "", font=('helvetica', 16) )
    client_lbl3.pack()

    def BackCommand():
        Equations_window.destroy()
        root.deiconify()

    back_button = Button(Equations_window, text="Back", command=BackCommand)
    back_button.pack()

frame1 = Frame(root)
frame1.pack()

ImageConvert_btn = Button(frame1, text = "Convert an Image" , fg = "white", command=NetworkAlarm, width=15, height=5, bg="green", font= ('helvetica', 14))
ImageConvert_btn.pack(side="left")

Rename_btn = Button(frame1, text = "Rename a File" , fg = "white", command=NetworkAlarm, width=15, height=5, bg="pink", font= ('helvetica', 14))
Rename_btn.pack(side="left")

AudioTransfer_btn = Button(frame1, text = "Download Audio" , fg = "white", command=NetworkAlarm, width=15, height=5, bg="purple", font= ('helvetica', 14))
AudioTransfer_btn.pack(side="left")


frame2 = Frame(root)
frame2.pack()
Statistics_btn = Button(frame2, text = "Network Statistics" , fg = "white", command=NetworkAlarm, width=15, height=5, bg="red", font= ('helvetica', 14))
Statistics_btn.pack(side="left")


Alarm_btn = Button(frame2, text = "Network Alarm" , fg = "white", command=NetworkAlarm, width=15, height=5, bg="blue", font= ('helvetica', 14))
Alarm_btn.pack( side="left")


Config_btn = Button(frame2, text = "Configuration" , fg = "white", command=NetworkAlarm, width=15, height=5, bg="black", font= ('helvetica', 14))
Config_btn.pack( side="left")

frame3 = Frame(root)
frame3.pack()

Equation_btn = Button(frame3, text = "Network Equations" , fg = "white", command=Equations, width=15, height=5, bg="black", font= ('helvetica', 14))
Equation_btn.pack( side="left")

# Execute Tkinter
root.mainloop()
