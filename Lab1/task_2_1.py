string = input("Enter string: ")
new_string = ""
for i in string:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        new_string += i
print(new_string)