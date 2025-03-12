
while True:
    # taking the user input
    usinp = input("$ ")
    # check if echo is at the begining of the user input
    if usinp[0:5] == "echo ":
        print(usinp[5:])