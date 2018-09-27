def to_list(s):
    s = s.replace(","," ")
    new_list = s.split()
    return new_list
# The main program starts here - DO NOT change it
the_string = input("Enter the string: ")
the_list = to_list(the_string)
print(the_list)