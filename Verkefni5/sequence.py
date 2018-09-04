# suma = x1 + x2 + x3
# x1 = x2
# x2 = x3
# x3 = suma
n = int(input("Enter the length of the sequence: ")) # Do not change this line
x1 = 0
x2 = 1
x3 = 2
if n >= 3:
    print(x2)
    print(x3)
    for s in range(n-2):
        suma = x1 + x2 + x3
        x1 = x2
        x2 = x3
        x3 = suma
        print(suma)
elif n == 1:
    print(x2)
elif n == 2:
    print(x2)
    print(x3)

