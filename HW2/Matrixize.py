'''
Напишите программу, принимающую на вход одномерный массив и два числа - размеры выходной матрицы. На выход программа должна подавать матрицу нужного размера, сконструированную из элементов массива.

Пример
[1, 2, 3, 4, 5, 6], 2, 3
#=>
[
    [1, 2, 3],
    [4, 5, 6]
]

Пример 2

[1, 2, 3, 4, 5, 6, 7, 8,], 4, 2 =>
[
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
]

'''


class MyClass():

    def home_work(self, var, a, b):

        if not a > 0 or not b > 0:
            print("false")
        result = []
        while var:
            result.append(var[:b])
            del var[:b]

        return result[:a]  # here we return result


if __name__ == '__main__':
    # Here we can make console input and check how function works
    a = 2
    b = 3

    lst_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


    result = MyClass().home_work(lst_, a, b)

    print(result)
