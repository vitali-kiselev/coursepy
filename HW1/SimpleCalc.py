print('Выберете операцию:')
print('1. Сложение')
print('2. Вычитание')
print('3. Умножение')
print('4. Деление')

x = int(input('Введите номер пункта: '))
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

if x == 1:
    print(a + b)
if x == 2:
    print(a - b) 
if x == 3:
    print(a * b)
if x == 4:
    print(a / b)




