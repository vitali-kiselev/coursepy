x = [5, 90, 3, 2, -7, 0]
lst = []

for i in range(len(x)):
    lst.append(min(x))
    x.remove(min(x))
print(lst)










