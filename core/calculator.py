from decorators import cache_decorator
@cache_decorator
def calculator(a, b, operation):
    # Здесь нужно реализовать функцию,
    # которая реализует основные арифметические операции между числами: +, -, /, *, **.
    # Так же следует сделать проверку, что поступивший оператор корректен (присутствует в этом списке +, -, /, *, **)
    result ={
        '+': a+b,
        '-': a-b,
        '/': a/b,
        '*': a*b,
        '**': a**b
    }
    return result.get(operation, 'Неизвестная операция')


if __name__ == '__main__':
    while True:
        try:
            a = int(input('Введите число: ')) # Тут было бы неплохо обрабатывать ошибку в случае передачи некорректных символов
            b = int(input('Введите число: '))
            operation = input('Введите операцию: ')

            print('Результат: ', calculator(a, b, operation))
        except ValueError:
            print('Введенные символы не являются числом')
        except ZeroDivisionError:
            print('Деление на 0 в обычной алгебре запрещено')
            