def test_simbol_():
    car = ('красный', '1988', 'легковой автомобиль', '13500')
    color, _, _, price = car
    print(color, price)


def print_methods():
    from string import Template

    name = 'Bob'
    errno = 50159747054
    print('--------------------------')
    print("Вариант 1 - классический")
    print('Привет, %s' % name) #выводим оычную строку
    print('%x' % errno) # вывод переменной в 16ричном формате
    print('Эй, %s! Вот ошибка 0x%x' % (name, errno)) #Несколько переменных объединяем в кортеж
    print('Эй, %(name)s! Вот ошибка 0x%(errno)x' % {
        'name': name,
        'errno': errno,
    }) #ну или можно использовать словарь для поименования переменных в строке
    print('--------------------------')
    print("Вариант 2 - с использвоанием format")
    print('Привет, {}!'.format(name))
    print('Эй, {name}! Вот ошибка 0x{errno:x}'.format(name=name, errno=errno))
    print('--------------------------')
    print('Вариант 3 . f-строки, Интерполяция литеральных строк (Python 3 .6+)')
    print(f'Привет, {name}!')
    print(f'Эй, {name}! Вот ошибка {errno:#x}!')
    print('--------------------------')
    print('Вариант 4 - Шаблонные строки')
    t = Template('Эй, $name !')
    print(t.safe_substitute(name=name))
    templ_string = Template('Эй, $name ! Вот ошибка $error !')
    print(templ_string.substitute(name=name, error=hex(errno)))

def yell(text):
    return text.upper() + '!'

def greet(func):
    greeting = func('Привет! Из функции у которой входной парамтер функция')
    return greeting

def whisper(text):
    return text.lower() + "..."

def get_speak_func(value):
    def yell(text):
        return text.upper() + '!'
    def whisper(text):
        return text.lower() + "..."
    if value > 0.5:
        return yell
    else:
        return whisper

def get_speak_func2(text, value):
    def yell():
        return text.upper() + '!'
    def whisper():
        return text.lower() + "..."
    if value > 0.5:
        return yell
    else:
        return whisper

def make_adder(n):
    def adder(x):
        return x + n
    return adder



if __name__ == '__main__':
    # test_simbol_()
    # print_methods()
    # import this # пасхалка
    print(yell('Привет'))
    bark = yell
    print(bark('Привет от bark'))
    # del yell
    # try:
    #     print(yell('Привет'))
    # except:
    #     raise ValueError('Не правильное название функции')
    # finally:
    #     print(bark('Привет от bark2'))
    #     print(bark.__name__)

    funcs = [bark, str.lower, str.capitalize]
    print(funcs)
    for f in funcs:
        print(f('Привет из списка'))

    print(funcs[0]('Приветище'))

    print(greet(bark))
    print(greet(whisper))
    # линии поведения функций
    speak_func = get_speak_func(0.3)
    print(speak_func)
    speak_func = get_speak_func(0.7)
    print(speak_func)
    print(speak_func(f'Привет от внутренней функции {speak_func.__name__}'))
    # линии поведения функции с лекисческим замыканием (когда функции явно не переадется параметр из родительской
    # но она его помнит
    print(get_speak_func2('Привет мир с замыканиями', 0.3)())
    plus_3 = make_adder(3)
    plus_5 = make_adder(5)
    print(plus_3(4))
    print(plus_5(4))
    # Функции - объекты, но обратное не верно. Можно сделать объект класса вызываемым, но не будет callable
    class Adder:
        def __init__(self, n):
            self.n = n

        def __call__(self, x):
            return self.n + x
    plus_3 = Adder(3)
    print(plus_3(4)) # Но   за кадром вызывается не функция, а метод класса __call__
    print(callable(plus_3))

    # лямбда функции
    print((lambda x, y: x + y)(3, 5))
    # сортировка по ключу с использованием лямбды
    tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
    print(sorted(tuples, key=lambda x: x[1]))
    tuples2 = [(1, 5), (2, 4), (4, 7), (3, 100)]
    print(sorted(tuples2, key=lambda x: x[0] * x[1]))

    # Декораторы
    # пример самого простого декоратора
    def null_decorator(func):
        return func

    def greet():
        return 'Привет!'

    print(null_decorator(greet()))
    # вариант с использованием определения декоратора
    def null_decorator2(func):
        return func

    @null_decorator
    def greet():
        return 'Привет из декоратора!'

    print(greet())
    # более сложный декоратор
    def uppercase(func):
        def wrapper():
            original_result = func()
            modify_result = original_result.upper()
            return modify_result
        return wrapper

    @uppercase
    def greet():
        return 'Привет из более сложного декоратора!'

    print(greet())

    # порядок выполнения множественных декораторов
    def strong(func):
        def wrapper():
            return f"<strong>{func()}</strong>"
        return wrapper

    def emphasis(func):
        def wrapper():
            return f"<em>{func()}</em>"
        return wrapper

    @strong
    @emphasis
    def greet():
        return 'Привет из под множественных декораторов'

    print(greet())

    # proxy декоратор - декоратор обрабатывающий аргументы принимаемой функции
    def proxy(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    # пример proxy декоратора
    import functools
    def trace(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f'ТРАССИРОВКА: вызвана {func.__name__}()'
                  f'с аргументами: {args}, {kwargs}'
                  )
            original_result = func(*args, **kwargs)
            print(f'ТРАССИРОВКА: функция {func.__name__}()'
                  f'вернула результат: {original_result}'
                  )
            return original_result
        return wrapper

    @trace
    def say(name, line):
        """Описание функции которое может быть не видно для коллег если не использовать встроекнный
        декоратор @functools.wraps(func)"""
        return f'{name}, {line}'

    print(say('Gizar', 'hello!'))

    # Что такое args и kwargs
    def foo(required, *args, **kwargs):
        print(required)
        if args:
            print(args)
        if kwargs:
            print(kwargs)

    # print(func())
    foo('Привет')
    foo('Привет', 1, 2, 3,)
    foo('Привет', 1, 2, 3, key1='значение', key2='23424dfg')
    # Привет
    # Привет
    # (1, 2, 3)
    # Привет
    # (1, 2, 3)
    # {'key1': 'значение', 'key2': '23424dfg'}

    # Переменные функций можно расширять и передавтаь в другие функции
    def bar(x, *args, **kwargs):
        print(f'Функция бар получила {x}')
        if args:
            print(f'Функция бар получила  аргс {args}')
        if kwargs:
            print(f'Функция бар получила  кваргс {kwargs}')


    def foo_2(x, *args, **kwargs):
        print(x)
        if args:
            print(args)
        if kwargs:
            print(kwargs)
        kwargs['имя'] = "Алиса"
        new_args = args + ('дополнительный', )
        bar(x, *new_args, **kwargs)


    foo_2('Привет', 1, 2, 3, key1='значение', key2='23424dfg')

    # пример использования args kwargs в классах
    class Car:
        def __init__(self, color, mileage):
            self.color = color
            self.mileage = mileage


    class AlwaysBlueCar(Car):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.color = 'синий'

    print(AlwaysBlueCar('зеленый', 12334).color)

    # пример использования args b kwargs при написании декораторов
    def trace(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            print(f, args, kwargs)
            result = f(*args, **kwargs)
            print(result)

        return wrapper


    @trace
    def greet(greeting, name):
        return '{}, {}!'.format(greeting, name)

    print(greet('Привет', 'Боб'))

    # Распаковка значений для аргументов функций при помощи * и **
    def print_vector(x, y, z):
        print(f'<{x},{y},{z}>')

    print_vector(0, 1, 0)


    #    распакуем кортеж / список при помощи *
    list_vector = [1, 2, 3]
    tuple_vec = (1, 2, 3)
    # не делать так
    print_vector(tuple_vec[0], tuple_vec[1], tuple_vec[2])
    # лучше так
    print_vector(*list_vector)

    # распакуем словарь при помощи ** (ключи подобраны под названия аргументов

    dict_vector = {'y': 4, 'z': 8, 'x': 12}

    print_vector(**dict_vector)

