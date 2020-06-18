lst = [165, 163, 160, 160, 157, 157, 155, 154]

x = int(input())

rank = 0

while rank < len(lst) and lst[rank] >= x:
    rank += 1
print(rank+1)










