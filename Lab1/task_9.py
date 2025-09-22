IP = input("Enter IP: ")
IP_ls = IP.split(sep=".")
if len(IP_ls) == 4:
    for i in IP_ls:
        if 0 <= int(i) <= 255:
            print("Correct!")
        break
else:
    print("Incorrect :(")