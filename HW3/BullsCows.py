'''
В классическом варианте игра рассчитана на двух игроков. Каждый из игроков задумывает и записывает тайное 4-значное
число с неповторяющимися цифрами. Игрок, который начинает игру по жребию, делает первую попытку отгадать число.
 Попытка — это 4-значное число с неповторяющимися цифрами, сообщаемое противнику.
 Противник сообщает в ответ, сколько цифр угадано без совпадения с их позициями в тайном числе (то есть количество коров)
  и сколько угадано вплоть до позиции в тайном числе (то есть количество быков).

При игре против компьютера игрок вводит комбинации одну за другой, пока не отгадает всю последовательность.

Ваша задача реализовать программу, против которой можно сыграть в "Быки и коровы"

Пример
Загадано число 3219

 #>>> 2310
Две коровы, один бык
 #>>> 3219
Вы выиграли!
'''

class MyClass():

    def myfunc(self):

        while True:
            var = input('Input VAR: ')
            if sec_num == var:
                print('Вы победили')
                break

            cows = len(set(list(sec_num)).intersection(list(var)))
            bulls = len([x for x in zip(list(sec_num), list(var)) if x[0] == x[1]])
            print(f"{cows} коровы {bulls} быков")

        result = None

        return result # here we retrun result

if __name__ == '__main__':
    import random

    num1 = random.choice(range(1, 10))
    num2 = random.choice([x for x in range(0, 10) if x not in [num1]])
    num3 = random.choice([x for x in range(0, 10) if x not in [num1, num2]])
    num4 = random.choice([x for x in range(0, 10) if x not in [num1, num2, num3]])

    var = input('Input VAR: ')
    sec_num = f"{num1}{num2}{num3}{num4}"
    cows, bulls = 0, 0

    result = MyClass().myfunc()

    print(result)

