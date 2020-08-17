# To find the average distance between 2 points in a 6x6 two-dimensional grid

add = 0
for i in range(6):
    for j in range(6):
        for k in range(6):
            for l in range(6):
                add += abs(i-k) + abs(j-l)

avg = add/(36*36)
print("Average distance:", avg)

# Output
# Average distance: 3.8888889
