# find_min function definition goes here
def find_min(x,y):
    if x >= y:
        return y
    elif x <= y:
        return x
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

# Call the function here
minimum = find_min(first,second)
print("Minimum: ", minimum)