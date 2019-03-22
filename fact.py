# Factorial number
def fact(n):
    num = 1
    while n > 0:
        num = num * n
        n = n - 1
    return num


n = int(input("enter the number:"))

print(fact(n))






