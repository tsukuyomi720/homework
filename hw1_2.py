import math

'''Сложение, вычитание, умножение, деление, возведение в степень, логарифм,
округление до N знака после запятой.'''


def obj_x():
    while True:
        x = input('first element:')
        try:
            return float(x)
            break
        except:
            print('Ошибка! Ожидалось вещественное число.')


def obj_y():
    while True:
        y = input('second element:')
        try:
            return float(y)
            break
        except:
            print('Ошибка! Ожидалось вещественное число.')


while True:
    q = input('Выберите действие(+,-,*,/,^,log,roundUP,roundDOWN):')
    if q == '+':
        c = obj_x() + obj_y()
        print('result:', c)

    elif q == '-':
        c = obj_x() - obj_y()
        print('result:', c)

    elif q == '*':
        c = obj_x() * obj_y()
        print('result:', c)

    elif q == '/':
        x = obj_x()
        while True:
            y = input('second element:')
            try:
                y = float(y)
                if y == 0:
                    print('Ошибка! Измените элемент для выполнения выбранного действия.')
                else:
                    break
            except:
                print('Ошибка! Ожидалось вещественное число.')
        c = x / y
        print('result:', c)

    elif q == '^':
        c = math.pow(obj_x(), obj_y())
        print('result:', c)

    elif q == 'log':
            while True:
                x = input('first element:')
                try:
                    x = float(x)
                    if x <= 0:
                        print('Ошибка! Измените элемент для выполнения выбранного действия.')
                    else:
                        break
                except:
                    print('Ошибка! Ожидалось вещественное число.')
            while True:
                y = input('second element:')
                try:
                    y = float(y)
                    if y<=0 or y == 1:
                        print('Ошибка! Измените элемент для выполнения выбранного действия.')
                    else:
                        break
                except:
                    print('Ошибка! Ожидалось вещественное число.')
            c = math.log(x, y)
            print('result:', c)

    elif q == 'roundUP':

        x = obj_x()

        while True:

            y = input('Сколько чисел после запятой должно стоять:')

            try:

                y = int(y)

                if y < 0:

                    print('Ошибка! Измените элемент для выполнения выбранного действия.')

                else:

                    break

            except:

                print('Ошибка! Ожидалось вещественное число.')

        c = x * (10 ** y)

        print(math.ceil(c) / (10 ** y))  # по правилам округления

        # print("result: ={:.{:d}f}". format(x, y))

        # print('result:', c)

    elif q == 'roundDOWN':

        x = obj_x()

        while True:

            y = input('Сколько чисел после запятой должно стоять:')

            try:

                y = int(y)

                if y < 0:

                    print('Ошибка! Измените элемент для выполнения выбранного действия.')

                else:

                    break

            except:

                print('Ошибка! Ожидалось вещественное число.')

        c = x * (10 ** y)

        print(math.floor(c) / (10 ** y))

    else:
        print('Ошибка! Выберите одно из предложенных действий.')