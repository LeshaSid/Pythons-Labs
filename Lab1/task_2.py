string = input("Enter string: ")
new_string = ""
sym = ['a', 'e', 'i', 'o', 'u']
for i in string:
    if i not in sym:
        new_string += i
print(new_string)