x = 1
y = 0
for i in range(1,11):
    for i in range(1,11):
        y = y + x
        print("{:>5d}".format(y),end='')
    print("")
    y = 0
    x += 1
