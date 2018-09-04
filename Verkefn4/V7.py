top_num = int(input("Input a number between 0 and 999: "))
for x in range(0, top_num):
    suma, a, b, c = 0, 0, 0, 0
    if 10 > x:
        print(x)
    elif x > 9 and 100 > x:
        a = (x // 10)
        b = x - (a*10)
        suma = ((a**2)+(b**2))
        if suma == x:
            print(x)
    elif x > 99 and 1000 > x:
        a = (x // 100)
        b = (x//10)-(a*10)
        c = x - ((a*100)+(b*10))
        suma = ((a**3)+(b**3)+(c**3))
        if suma == x:
            print(x)