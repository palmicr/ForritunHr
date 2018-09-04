n = int(input("Input a natural number: ")) # Do not change this line

# Fill in the missing code below
c = 2
prime = 1
while c < n:
    if (n % c) == 0:
        prime = 0
    c += 1
# Do not changes the lines below
if prime:
    print("Prime")
else:
    print("!Prime")