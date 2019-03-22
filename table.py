def table(a, b):
    if a and b != 0:
        return a * b
    else:
        return 0


n = int(input("Enter the number for multiplying:"))

for i in range(1, 11):
    print("{} multiplied by {} is {}".format(n, i, table(i, n)))

