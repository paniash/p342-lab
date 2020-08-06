# To calculate the factorial of a number n and to give an error when the input is a negative number.
n = int(input("Enter a number.\n"))
if n<0:
    print("Factorial for negative numbers is undefined!!!\n")
    exit()
elif n==0:
    prod = 1
    print("The factorial of", n, "is", prod)
else:
    prod = 1
    for i in range(1,n+1):
        prod *= i
    print("The factorial of", n, "is", prod)
