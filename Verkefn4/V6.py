top_num = int(input("Upper number for the range: ")) # Do not change this line
for x in range(2,(top_num+1)):
    summa = 0
    for n in range(1,x):
        if(x % n) == 0:
            summa += n
    if summa == x:
        print(summa)