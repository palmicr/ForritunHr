# Your function definition goes here
def count_case(string):
    x = 0
    y = 0
    for char in string: 
        if char.islower():
            x += 1
        elif char.isupper():
            y += 1
    return y,x

user_input = input("Enter a string: ")
# Call the function here
upper, lower = count_case(user_input)
print("Upper case count: ", upper)
print("Lower case count: ", lower)