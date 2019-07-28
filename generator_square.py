def nextsquare():
    i = 1
    while True:
        yield i * i
        i += 1

for num in nextsquare():
    if num > 100:
        break
    print(num)