import random
sec_num = [random.randint(0, 9) for i in range(4)] #программа генерирует случайный численный список  от 0 до 9
var = list(map(int, input('Input VAR: ').split()))
dict = {}
buls = 0
cows = 0





#def myfunc(sec_num, var):
num1 = [i for i in sec_num]
num2 = [j for j in var]
if num1 == num2:
    print('You Win')

for i in sec_num:
    for j in var:
        if i in sec_num:































