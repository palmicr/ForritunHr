# is_prime function definition goes here
def is_prime(x):
    for i in range(3, x):
        if x % i == 0:
            return False
    return True
num = int(input("Input an integer greater than 1: "))
if is_prime(num):
    print(num,"is a prime")
else:
    print(num,"is not a prime")
# Call the function here and print out the appropriate message