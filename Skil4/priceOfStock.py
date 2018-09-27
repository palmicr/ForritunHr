def main_continue():
    halda_afram = True
    while halda_afram:
        h_a = input("Continue: ")
        if h_a == "n":
            halda_afram = False
            return 0
        elif h_a == "y":
            halda_afram = False
            return 1
        else:
            print("y or n!")

def ask_shares():
    shares = True
    while shares:
        try: 
            hlutabref_f = int(input("Enter number of shares: "))
        except ValueError:
            print("Invalid number!")
            continue
        else:
            break
    return hlutabref_f

def ask_price():
    price = True
    while price:
        price = input("Enter price (dollars, numerator, denominator): ")
        price = price.split()
        try: 
            dol = int(price[0])
            num = int(price[1])
            den = int(price[2])
        except Exception:
            print("Invalid price!")
            continue
        else:
            break
    return dol,num,den

def calculate_price():
    x = shares * price[0]
    y = shares * (price[1] / price[2])
    r = x + y
    return r

main = True
while main:
    shares = ask_shares()
    price = ask_price()
    value = calculate_price()
    print("{0} shares with market price {1} {2}/{3} have value ${4:.2f}".format(shares, price[0],price[1],price[2],value))
    main = main_continue()