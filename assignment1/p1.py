# To add all natural numbers upto n without using the n(n+1)/2, where n is the user input.
n = int(input("Enter a number\n"))
sum = 0
for i in range(n+1):
    sum += i

print("The sum is", sum)
