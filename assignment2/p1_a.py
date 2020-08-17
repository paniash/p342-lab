# To find the average distance between 2 points on a straight line made of discrete N (=6) points
add = 0
for i in range(6):
    for j in range(6):
        add += abs(j-i)

avg = add/36
print("Average distance:", avg)
