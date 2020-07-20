'''
На вход ваше программы дан массив целых чисел.

Напишите программу, сортирующую этот массив по возрастанию.

Использовать функции .sort() и sorted() нельзя.

sort([5, 90, 3, 2, -7, 0]) => [-7, 0, 2, 3, 5, 90]

'''


class MyClass():

    def sort(self, lst):
        result = []
        for i in range(len(lst)):
            result.append(min(lst))
            lst.remove(min(lst))




        return result  # here we return result


if __name__ == '__main__':
    # Here we can make console input and check how function works

    lst = [5, 90, 3, 2, -7, 0]

    result = MyClass().sort(lst)

    print(result)
