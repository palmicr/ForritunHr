age = int(input("Input age: ")) # Do not change this line

# Fill in the missing code below
ticket_price = float(30)

if age >= 65:
    ticket_price = ticket_price * 0.5
    print(ticket_price)
elif age <= 5:
    ticket_price = 0.0
    print(ticket_price)
else:
    print(ticket_price)


