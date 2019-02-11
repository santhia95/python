def leap_year(year):
    if(year % 4 == 0):
        if(year % 100 == 0):
            if(year % 400 == 0):
                return("leap")
            else:
                return("not leap")
        else:
            return("leap")
    else:
        return("not leap")

l=[]
n = int(input("enter the number of years you want to test:"))
for i in range(n):
    l.append(int(input("enter year{} :".format(i+1))))
    print(l[i], l)

for i in range(len(l)):
    n = input("y/n")
    if n == "y":
        print(l[i], leap_year(l[i]))
    else:
        break
print(l[i], leap_year(l[i]))