import datetime
import os
import socket

# bool var to check if the command is valid
is_command = False

while True:
    # gets the current date and time 
    dt = datetime.datetime.now()

    # taking the user input
    usinp = input("$ ")

    # check if echo is at the begining of the user input
    if usinp[0:5] == "echo ":
        is_command = True
        print(usinp[5:])

    # check if exit in user input
    if usinp == "exit":
        is_command = True
        break

    if usinp == "date":
        is_command = True
        print(f"{dt.day}-{dt.month}-{dt.year}")

    if usinp == "cls" or usinp == "clear":
        is_command = True
        os.system('cls')

    if usinp == "ls":
        is_command = True
        path = os.getcwd()
        dir_list = os.listdir(path)
        print(f"files and directories in {path}  :  ")
        print(dir_list)

    if usinp == "hostname":
        is_command = True
        print(socket.gethostname())

    


    # if user input does not contain any builtin commands this will be executed
    if not is_command:
        print(usinp + " : command not found")