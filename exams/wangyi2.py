def rev(num):
    s = str(num)
    s = s[::-1]
    return int(s)

num1 = 100
num2 = 123
print(rev(rev(100)+rev(num2)))

def buyApple(n):
    x = 0
    minBags = n/6.0
    if n < 6:
        return 0
    for y in range(0,int(n/8)):
        x = (n - 8 * y)/6.0
        if float(x).is_integer():
            if (x + y) <= minBags:
                minBags = int(x+y)
    if float(minBags).is_integer():
        return minBags
    else:
        return 0

n = 34
print(buyApple(n))
