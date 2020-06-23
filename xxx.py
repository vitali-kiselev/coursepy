lst = [1, 3, 5, 9, 1, 3, 9]
for x in set(lst):
    if x in set(lst):
        print(set(x))
