# Your functions should appear here
def populate_list(i):
    x = True
    while x:
        s = input("Enter value to be added to list: ")
        if s.lower() == "exit":
            x = False
        else:
            i.append(s) 

def triple_list(i):
    t = i * 3
    return t

# Main program starts here - DO NOT change it.
initial_list = []
populate_list(initial_list)
new_list = triple_list(initial_list)

for items in new_list:
    print(items)
