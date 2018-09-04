num = 10
while num < 99:
    c = num * num
    d = (c // 100) * 100
    if c > 1000:
        break
    ab = c - d
    if num == ab:
        print(num)
    num += 1    