x = [1, 5, 2, 4, 3, 6]
result = list()

for i in range(len(x)):
    if x[i] > x[i-1]:
        result.append(x[i])

print(result)
