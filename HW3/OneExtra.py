'''
Вам передан массив чисел. Известно, что каждое число в этом масиве имеет пару, кроме одного:

[1, 5, 2, 9, 2, 9, 1] => 5

Напишите программу, которая бы максимально быстро находила это число.
'''

class MyClass():

    def myfunc(self, ):
        lst = [1, 3, 5, 9, 1, 3, 9]
        dict = {}
        for i in lst:
            if i in lst:
                dict.setdefault(i, 0)
                dict[i] += 1
        for k, v in dict.items():
            if dict[k] == 1:
                print(k)
                break
        result = None

        return result # here we retrun result

if __name__ == '__main__':
   # Here we can make console input and check how function works

   # var = input('Input VAR: ')

   result = MyClass().myfunc()

   print(result)
