# Sum over 1+1/2+1/3+... till the sum does not change by more than 0.001
for n in range(1, 10000):
    temp = 0
    total = 0
    for i in range(1, n+1):
        temp+=1/i
    for j in range(1, n+2):
        total+=1/j
    if (total-temp) <= 0.001:
        print("SUM:", total)
        exit()
