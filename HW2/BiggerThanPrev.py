'''
Больше предыдущего
Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.

Пример
[1, 5, 2, 4, 3]
#=> [5, 4]
[1, 2, 3, 4, 5]
#=> [2, 3, 4, 5]
'''


class MyClass():

    def lesson_work(self, var):
        result = list()

        for i in range(len(var)):
            if var[i] > var[i-1]:
                result.append(var[i])

        return result  # here we return result


if __name__ == '__main__':
    # Here we can make console input and check how function works

    var = [1, 5, 2, 4, 3]

    result = MyClass().lesson_work(var)

    print(result)
