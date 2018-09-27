MAX_X = 10
MIN_X = 1
cont = 1

def move_x(y,x):
    if y == "r":
        if (x+1) > MAX_X:
            x = x
        else:
            x += 1
    elif y == "l": 
        if (x-1) < MIN_X:
            x = x
        else:
            x -= 1
    return x

x_posision = int(input("Input a position between 1 and 10: "))
while cont:
    print("l - for moving left\nr - for moving right\nAny other letter for quitting")
    move_input = input("Input your choice: ")
    if move_input == "r" or move_input == "l":
        x_posision = move_x(move_input,x_posision)
        print("New position is: " + str(x_posision))
    else:
        break
print("New position is: " + str(x_posision))
