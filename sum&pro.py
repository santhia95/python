def sum(a):
   return a


def pro(d):
    return d


n = int(input("Enter a number:"))
a = 0
while n > 0:
    b = n % 10
    a = a + b
    n = n // 10

print("Sum of digits of a number is:")
print(sum(a))

m = int(input("Enter a number:"))
d = 1
while m > 0:
    e = m % 10
    d = d * e
    m = m // 10


print("Product of digits of a number is")
print(pro(d))


