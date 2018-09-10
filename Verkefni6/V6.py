name = input("Input a name: ")
first, last = name.split(", ")
print(last[0].upper() + ". " + first[0].upper() + first[1:])