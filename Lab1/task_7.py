sec = int(input("Enter time in seconds: "))
minutes = sec // 60
new_sec = sec - 60*minutes
print(str(sec) + " - " + str(minutes) + " minutes " + str(new_sec) + " seconds")