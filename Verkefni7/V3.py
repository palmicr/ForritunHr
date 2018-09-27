# The function definition goes here
MAX_r = 555
MIN_r = 1
def in_range(x):
    if x in range(MIN_r,MAX_r):
        return True
    else:
        return False
num = int(input("Enter a number: "))
if in_range(num):
    print(num,"is in range!")
else:
    print(num,"is outside the range!")
# You call the function here