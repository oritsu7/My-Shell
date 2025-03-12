is_command = False

while True:
    # taking the user input
    usinp = input("$ ")
    # check if echo is at the begining of the user input
    if usinp[0:5] == "echo ":
        is_command = True
        print(usinp[5:])

    if usinp[0:4] == "exit":
        is_command = True
        break

    if not is_command:
        print(usinp + " : command not found")