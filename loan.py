# Pálmi C Rúnarsson
# Skilaverkefni 1 - Lán
loan_amount = float(input("Input the cost of the item in $: "))
payment_left = float(loan_amount)
payment = float(50)
month_count = 0
intrest = float(0)
total_intrest = float(0)
vextir = float(0)

while round(payment_left, 2):
    if loan_amount <= 1000:
        vextir = 0.015
    else:
        vextir = 0.02
    intrest = (payment_left * vextir)
    if payment_left < payment:
        payment = payment_left + intrest
    total_intrest += intrest
    payment_left = intrest + (payment_left - payment)
    month_count += 1
    print("Month:", month_count, "Payment:", round(payment,2), "Interest paid:", round(intrest,2), "Remaining debt:", round(payment_left,2))
print(" ")
print("Number of months:", month_count)
print("Total interest paid:", round(total_intrest,2))