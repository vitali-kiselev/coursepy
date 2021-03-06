'''
Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю.Помогите ему это сделать.

Программа получает на вход невозрастающую последовательность натуральных чисел,означающих рост каждого человека в строю. После этого вводится число X – рост Пети.Все числа во входных данных натуральные и не превышают 200.

Выведите номер, под которым Петя должен встать в строй. Если в строю есть люди с одинаковым ростом,таким же, как у Пети, то он должен встать после них.


Пример:

rank([165, 163, 160, 160, 157, 157, 155, 154], 162)
#=> 3

'''


class MyClass():

    def rank(self, lst, rank):
        x = int(input())

        while rank < len(lst) and lst[rank] >= x:
            rank += 1


        result = rank + 1

        return result  # here we return result


if __name__ == '__main__':
    # Here we can make console input and check how function works

    lst = [165, 163, 160, 160, 157, 157, 155, 154]
    rank = 0

    result = MyClass().rank(lst, rank)

    print(result)
