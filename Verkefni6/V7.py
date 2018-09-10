my_int = int(input('Give me an int >= 0: '))
# Fill in the missing code
x = my_int
bstr = ""
if x == 0:
    bstr += str(x)
else:    
    while x > 0:
        binni = x % 2
        x = x // 2
        binni = str(binni)
        bstr += binni 
print("The binary of", my_int, "is", bstr[::-1])