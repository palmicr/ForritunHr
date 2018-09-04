m = int(input("Input the first integer: ")) # Do not change this line
n = int(input("Input the second integer: ")) # Do not change this line

if m > n:
    for i in range(1, n):
        if((m % i == 0) and (n % i == 0)):
            t = i
else:
    for i in range(1, m):
        if((m % i == 0) and (n % i == 0)):
            t = i
print(t)        




    