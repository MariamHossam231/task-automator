from tkinter import *
from socket import *
from threading import *
import subprocess
import os

TK_SILENCE_DEPRECATION=1

serverIP = "127.0.0.1"

def CallServer():
    file_path = os.path.join("..", "Merged_Server_GUI.py")
    subprocess.call(["python", file_path])

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



def RenameFile():
      root.iconify()
      Rename_window = Toplevel()
      Rename_window.title("Renaming File")
      Rename_window.geometry("700x600")

      Oldfileinput = Entry(Rename_window)
      Oldfileinput.pack()

      Newfileinput = Entry(Rename_window)
      Newfileinput.pack()

    
      def FileRenamed(old_filename, new_filename):
          RenameSocket = socket(AF_INET, SOCK_STREAM) 

          RenameSocket.connect((serverIP,RenamePort))
          #old_filename = input("Enter old file name: ")
          #new_filename = input("Enter new file name: ")
          command = f'RENAME {old_filename} {new_filename}'
          RenameSocket.sendall(command.encode())

          #print(clientSocket.recv(1024).decode())

          RenameSocket.close() 
    

      submitbtn = Button(Rename_window, text= "Rename", command=lambda:FileRenamed(Oldfileinput.get(),Newfileinput.get()))
      submitbtn.pack()


      def BackCommand():
        Rename_window.destroy()
        root.deiconify()

      back_button = Button(Rename_window, text="Back", command=BackCommand)
      back_button.pack()


def AudioVidTransfer():
      root.iconify()
      Transfer_window = Toplevel()
      Transfer_window.title("Audio/Video Download")
      Transfer_window.geometry("700x600")

      Input = Entry(Transfer_window)
      Input.pack()

      def Transfer(audio_file):
        TransferSocket = socket(AF_INET, SOCK_STREAM) 

        TransferSocket.connect((serverIP,AudioPort))

        #audio_file = input("Which audio file do you want?\n")

        TransferSocket.sendall(audio_file.encode())   
        print(f"audio file = {audio_file}")

        audio_data= TransferSocket.recv(200000)
        
        with open(audio_file,'wb') as file:
           file.write(audio_data)

        #print('File received: ',audio_file)

        TransferSocket.close() 


      transfersubmit = Button(Transfer_window, text= "Download", command=lambda:Transfer(Input.get()))
      transfersubmit.pack()


frame1 = Frame(root)
frame1.pack()


ImageConvert_btn = Button(frame1, text = "Convert an Image" , fg = "white", command=RenameFile, width=15, height=5, bg="green", font= ('helvetica', 14))
ImageConvert_btn.pack(side="left")

Rename_btn = Button(frame1, text = "Rename a File" , fg = "white", command=RenameFile, width=15, height=5, bg="pink", font= ('helvetica', 14))
Rename_btn.pack(side="left")

AudioTransfer_btn = Button(frame1, text = "Download Audio" , fg = "white", command=AudioVidTransfer, width=15, height=5, bg="purple", font= ('helvetica', 14))
AudioTransfer_btn.pack(side="left")


frame2 = Frame(root)
frame2.pack()
Statistics_btn = Button(frame2, text = "Network Statistics" , fg = "white", command=RenameFile, width=15, height=5, bg="red", font= ('helvetica', 14))
Statistics_btn.pack(side="left")


Alarm_btn = Button(frame2, text = "Network Alarm" , fg = "white", command=RenameFile, width=15, height=5, bg="blue", font= ('helvetica', 14))
Alarm_btn.pack( side="left")


Config_btn = Button(frame2, text = "Configuration" , fg = "white", command=RenameFile, width=15, height=5, bg="black", font= ('helvetica', 14))
Config_btn.pack( side="left")

# Execute Tkinter
root.mainloop()




# root= tk.Tk()

# root.title("Network Task Automator")
# canvas1 = tk.Canvas(root, width=700, height=600, relief='raised')
# canvas1.pack()

# label1 = tk.Label(root, text='Welcome!')
# label1.config(font=('helvetica', 18))
# canvas1.create_window(320, 25, window=label1)

# # label2 = tk.Label(root, text='Type 1 for SIC or 2 for SICXE:')
# # label2.config(font=('helvetica', 10))
# # canvas1.create_window(200, 100, window=label2)

# # entry1 = tk.Entry(root) 
# # canvas1.create_window(200, 140, window=entry1)

# def clicked():
    
#     lbl = tk.Label(root, text='Welcome!')
#     lbl.config(font=('helvetica', 12))
#     lbl.config(300, 
#         text = "I just got clicked")
 
# # button widget with red color text
# # inside
# btn = tk.Button(root, text = "Click me" ,fg = "red", command=clicked)
# # set Button grid
# btn.config(column=1, row=0)


# root.mainloop()