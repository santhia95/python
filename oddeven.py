def oddeven(n):
    if(n != 0):
        if n > 0:
           if n % 2 == 0:
               print("Number is even and positive")

           else:
               print("Number is odd and positive")

        else:
            if n % 2 == 0:
               print("Number is even and negative")

            else:
               print("Number is odd and negative")
    else:
        print("Number is Zero")


n = int(input("Enter number:"))
print(oddeven(n))
