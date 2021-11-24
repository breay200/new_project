from os import error
import socket
import tkinter as tk
from threading import Thread, stack_size
global HEADER_LENGTH
HEADER_LENGTH = 1024

status = {"sending": True}
thread_list = []

def receive(sock):
    no_data = True
    while no_data:
        try:
            data_header = sock.recv(HEADER_LENGTH)
            data_length = int(float(data_header.decode('utf-8').strip()))
            data = sock.recv(data_length).decode('utf-8')
            
            if data == 'user 1 received':
                #status["sending"] = False
                pass
            elif 'user2' in data:
                print("received data from user 2", data)
                with open("received_data.txt", "a") as file1:
                    file1.write(data + "\n")
                    #no_data = False
            elif 'user1' in data:
                #print("this is my sent data")
                pass

        except Exception as e:
            print(e)


def send(data, sock):
    #sending = status.get("sending")
    try:
        data_header = f"{len(data):<{HEADER_LENGTH}}".encode('utf-8')
        assert sock.send(data_header+data.encode('utf-8'))
    except Exception as e:
        print(f"line 39: {e}")
    #sending = status.get("sending")
        

def rock_paper_scissors():
    def widget_send(data):
        if not receiving.is_alive():
            
            print("started recieving")
            receiving.start()
        send(data, sock)

    for widget in main_frame.winfo_children():
        widget.destroy()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 65432)
    
    sock.connect(server_address)
    print('connecting to %s port %s' % server_address)
    receiving = Thread(target = receive, args=(sock,))
    thread_list.append(receiving)
    receiving.start()

    send("connection test from user1", sock)
    rock_btn = tk.Button(main_frame, text="rock", command=lambda: widget_send("user1 rock"))
    rock_btn.grid(column=1,row=1)

    paper_btn = tk.Button(main_frame, text="paper", command=lambda: widget_send("user1 paper"))
    paper_btn.grid(column=2, row=1)

    scissor_btn = tk.Button(main_frame, text="scissors", command=lambda: widget_send("user1 scissors"))
    scissor_btn.grid(column=3, row=1)



print("Client Test")
master = tk.Tk()
master.geometry('400x200')
master.title("Client Test")

main_frame = tk.Frame(master)

send_btn = tk.Button(main_frame, text="Start", command=lambda: rock_paper_scissors(), width=25)
send_btn.grid(column=1, row=1)

quit_btn = tk.Button(main_frame, text="Quit", command=lambda: quit(), width=25)
quit_btn.grid(column=2, row=1)

main_frame.columnconfigure(1, weight=1)
main_frame.rowconfigure(1, weight=1)
main_frame.grid(column=0, row=0)

master.mainloop()