# palindrome function definition goes here
def is_palindrome(string):
    old_string = ""
    new_string = ""
    for i in string:
        if i.isalpha():
            old_string += i
        else:
            continue
    new_string = old_string[::-1]
    if old_string.lower() == new_string.lower():
        return True
    else:
        return False

in_str = input("Enter a string: ")
if is_palindrome(in_str):
    print('"' + in_str + '" is a palindrome.')
else:
    print('"' + in_str+ '" is not a palindrome.')

# call the function and print out the appropriate message