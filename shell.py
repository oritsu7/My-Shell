import datetime
import os
import socket


while True:
    # bool var to check if the command is valid
    is_command = False

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

    if usinp == "time":
        is_command = True
        print(f"{dt.hour}::{dt.minute}::{dt.second}")

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

    if usinp[0:6] == "touch ":
        is_command = True
        filename = usinp[6:]
        f = open(filename, "a")
        f.close()

    if usinp[0:3] == "rm ":
        is_command = True
        filename = usinp[3:]
        if os.path.exists(filename):
            os.remove(filename)
        else:
            print("The file does not exist")
    

    if not is_command:
        try:
            if all(c.isdigit() or c in "+-*/%()" for c in usinp.replace(" ", "")):
                print(eval(usinp))
                is_command = True
        except ZeroDivisionError:
            print("Zero division error!")
            is_command = True
        except:
            pass
    


    # if user input does not contain any builtin commands this will be executed
    if not is_command:
        print(usinp + " : command not found")