# if (num_int is > max_int) = max_int
num_int = int(input("Input a number: "))    # Do not change this line
max_int = 0
while num_int >= 0:
    if max_int < num_int:
        max_int = num_int
    num_int = int(input("Input a number: "))
print("The maximum is", max_int)    # Do not change this line
