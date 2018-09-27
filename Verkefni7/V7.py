# Your function definition goes here
def fibo(x):
    num1 = 1
    num2 = 1
    num3 = 0
    if x == 1:
        print(num1)
    elif x == 2:
        print(num1,num2)
    else:
        print(num1,num1,end=' ')
        for i in range(x-2):
            num3 = num2 + num1
            num1 = num2
            num2 = num3
            print(num3,end=' ')

    return 0
n = int(input("Input the length of Fibonacci sequence (n>=1): "))
fibo(n)
# Call your function here        

