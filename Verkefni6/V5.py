s = input("Input a string: ")
output = ""
for char in s:
    if char.isdigit():
        output += char
    else:
        continue
print(output)