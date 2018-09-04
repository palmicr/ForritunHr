stars = int(input("Max number of stars: ")) # Do not change this line
for x in range (0,stars):
    for j in range (x):
        print("*")
    print()

for x in range (stars,0,-1):
    for j in range (x):
        print("*")
    print()