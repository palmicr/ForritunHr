iv = int(input("Initial value: "))
steps = int(input("Step: "))
suma = iv
output = 0
while output <= 100:
    print(suma,end=' ')
    output += suma
    suma = suma + steps
    

print("\nSum of series: " + str(output))



