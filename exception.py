def div_num(n, num):
    l = []
    for i in num:
        try:
            l.append(n/i)
        except ZeroDivisionError as z:

            print(z)
            l.append(0)
    return l


def make_list(n):
    l = []
    for i in range(-n, n+1):
        l.append(i)
    return l


n = int(input("enter a value:"))
num = int(input("enter a number in a list"))
print(div_num(n, make_list(num)))


