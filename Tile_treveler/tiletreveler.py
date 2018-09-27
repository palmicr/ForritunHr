# x,y hnit fyrir staðsetningu.
# Norður og Suður er  + og - á y hniti.
# Austur og Vestur er + og - á x hniti.
# Ef X eða Y er 1 kemst það ekki lengur í -.
# Ef X eða Y er 3 kemst það ekki lengur í +.
# Svo eru "Veggir" sem koma í veg fyrir það 
# að hægt sé að fara í gegnum þá.
r = True
x = 1
y = 1
direction = ""
north = "(N)orth"
south = "(S)outh"
east = "(E)ast"
west = "(W)est"
o = "or"
while r:
    if (x == 3) and (y == 1):
        print("Victory!")
        break
    elif (y == 1):
        print("You can travel: " + north + ".")
        while (y == 1):
            direction = input("Direction: ")
            if direction.lower() == "n":
                if (y+1) > 3:
                    print("Not a valid direction!")
                else:
                    y += 1
            else:
                print("Not a valid direction!")

    elif (y == 2):
        if (x == 1):
            print("You can travel: " + north,o,east,o,south + ".")
            while (x == 1) and (y == 2):
                direction = input("Direction: ")
                if direction.lower() == "n" :
                    if (y+1) < 1:
                        print("Not a valid direction!")
                    else:
                        y += 1
                elif direction.lower() == "s" :
                    if (y-1) < 1:
                        print("Not a valid direction!")
                    else:
                        y -= 1
                elif direction.lower() == "e":
                    if (x+1) > 3:
                        print("Not a valid direction!")
                    else:
                        x += 1
                else:
                    print("Not a valid direction!")
        elif (x == 2):
            print("You can travel: " + south,o,west + ".")
            while (x == 2) and (y == 2):
                direction = input("Direction: ")
                if direction.lower() == "w" :
                    if (x-1) < 1:
                        print("Not a valid direction!")
                    else:
                        x -= 1
                elif direction.lower() == "s" :
                    if (y-1) < 1:
                        print("Not a valid direction!")
                    else:
                        y -= 1
                else:
                    print("Not a valid direction!")
        elif (x == 3):
            print("You can travel: " + north,o,south + ".")
            while (x == 3) and (y == 2):
                direction = input("Direction: ")
                if direction.lower() == "n" :
                    if (y+1) < 1:
                        print("Not a valid direction!")
                    else:
                        y += 1
                elif direction.lower() == "s" :
                    if (y-1) < 1:
                        print("Not a valid direction!")
                    else:
                        y -= 1
                else:
                    print("Not a valid direction!")
    elif (y == 3):
        if (x == 1):
            print("You can travel: " + east,o,south + ".")
            while (x == 1) and (y == 3):
                direction = input("Direction: ")
                if direction.lower() == "s" :
                    if (y-1) < 1:
                        print("Not a valid direction!")
                    else:
                        y -= 1
                elif direction.lower() == "e":
                    if (x+1) > 3:
                        print("Not a valid direction!")
                    else:
                        x += 1
                else:
                    print("Not a valid direction!")
        elif (x == 2):
            print("You can travel: " + east,o,west + ".")
            while (x == 2) and (y == 3):
                direction = input("Direction: ")
                if direction.lower() == "w" :
                    if (x-1) < 1:
                        print("Not a valid direction!")
                    else:
                        x -= 1
                elif direction.lower() == "e" :
                    if (x+1) > 3:
                        print("Not a valid direction!")
                    else:
                        x += 1
                else:
                    print("Not a valid direction!")
        elif (x == 3):
            print("You can travel: " + south,o,west + ".")
            while (x == 3) and (y == 3):
                direction = input("Direction: ")
                if direction.lower() == "w" :
                    if (x-1) < 1:
                        print("Not a valid direction!")
                    else:
                        x -= 1
                elif direction.lower() == "s" :
                    if (y-1) < 1:
                        print("Not a valid direction!")
                    else:
                        y -= 1
                else:
                    print("Not a valid direction!")
    else:
        print("Not a valid direction!")

