my_items = ['a', 'b', 'c', 'd']

for item in my_items:
    print(item)


for i in range(0, 3, 2):
    print(my_items[i])

for i, item in enumerate(my_items):
    print(f'{i}: {item}')


emails = {
    'Боб': 'bob@example.com',
    'Алиса': 'alice@example.com',
}
for name, email in emails.items():
    print(f'{name} -> {email}')

# ------------ВКЛЮЧЕНИЯ В СПИСКИ СЛОВАРИ И МНОЖЕЕСТВА-------------------
# или по другому  - генераторы списков
squares = [x * x for x in range(10)]
print(squares)


squares = [x * x for x in range(10) if x % 2 == 0]
print(squares)

# генераторы множеств
print({x * x for x in range(-9, 10)})

# генератор словарей
print({x: x * x for x in range(10)})

# ---------СРЕЗЫ----------------
lst = [1, 2, 3, 4, 5]

# lst[начало:конец:шаг]
print(lst[1:3:1])

# включает каждый второй элемент оригинала:
print(lst[::2])

# [::-1], то вы получите копию оригинального списка, только в обратном порядке:
print(lst[::-1]) #reverse - метод

# удаления всех элементов из списка, не разрушая сам объект-список
del lst[:] #lst.clear()
print(lst)

# наполнение
original_lst = lst
lst[:] = [7, 8, 9]
print(lst)
# [7, 8, 9]
print(original_lst)
# [7, 8, 9]
print(original_lst is lst)
# True

# создание (мелких) копий существующих списков:
copied_lst = lst[:]
print(copied_lst)
# [7, 8, 9]
print(copied_lst is lst)
# False

# -----------------Дандер-методы __iter__ и __next__-----
# Создадим собственный работающий итератор
class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return RepeaterIterator(self)


class RepeaterIterator:
    def __init__(self, source):
        self.source = source

    def __next__(self):
        return self.source.value

# создаем итерируемый объект
# repeater = Repeater('Привет!')

# for item in repeater:
#     print(item)

#вот что под капотом for
# repeater = Repeater('Привет')
# iterator = repeater.__iter__()
# while True:
#      item = iterator.__next__()
#      print(item)

# если пошагово то вот так
# repeater = Repeater('Привет')
# iterator = iter(repeater)
# print(next(iterator))
# # 'Привет'
# print(next(iterator))
# # 'Привет'
# print(next(iterator))
# # 'Привет'
# # ...

# Оптимизируем код итератора и объединим классы
class NewRepeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value


repeater = NewRepeater('Привет!')

# и он тоже раотает
# for item in repeater:
#     print(item)

# класс итератора, который назовем ограни- ченным повторителем BoundedRepeater

class BoundedRepeater():
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        else:
            self.count += 1
            return self.value

repeater = BoundedRepeater('Привет', 3)
for item in repeater:
    print(item)

# или под капотом
repeater = BoundedRepeater('Привет', 3)
iterator = iter(repeater)
while True:
    try:
        item = next(iterator)
    except StopIteration:
        break
    print(item)

# для совместимости и работы во обих версиях питона 2.0 и 3.0
# можно модернизировать класс
class InfiniteRepeater(object):
    def __init__(self, value):
        self.value = value
    def __iter__(self):
        return self
    def __next__(self):
        return self.value
    # Совместимость с Python 2:
    def next(self):
        return self.__next__()


# --------------БЕСКОНЕЧНЫЕ ГЕНЕРАТОРА YiELD---------------
# перепишем предыдущий класс
def repeater(value):
    while True:
        yield value

# бесконечность
# for i in repeater('Привет'):
#     print(i)

iterator = repeater('Привет1')
print(next(iterator))
# 'Привет'
print(next(iterator))
# 'Привет'
print(next(iterator))

# Генераторы, которые прекращают генерацию
def repeat_three_times(value):
    yield value
    yield value
    yield value

for x in repeat_three_times('Всем привет1'):
    print(x)

iterator = repeat_three_times('Всем привет')
print(next(iterator))
# 'Всем привет'
print(next(iterator))
# 'Всем привет'
print(next(iterator))
# 'Всем привет'
# print(next(iterator))
# # StopIteration
# print(next(iterator))
# # StopIteration
# print(next(iterator))
# # StopIteration


def bounded_repeater(value, max_repeats):
    count = 0
    while True:
        if count >= max_repeats:
            return
        count += 1
        yield value

for x in bounded_repeater('Привет4', 4):
    print(x)


def bounded_repeater(value, max_repeats):
    for i in range(max_repeats):
        yield value
    # return None

# -----------ВЫРАЖЕНИЯ ГЕНЕРАТОРЫ-----------
iterator = ('Привет' for i in range(3))
for x in iterator:
    print(x)
# 'Привет'
# 'Привет'
# 'Привет'

# Отличие от ВКЛЮЧЕНИЙ В СПИСОК:
# в отличие от включений в список выражения-генераторы не конструируют объекты-списки. 
# Вместо этого они генерируют значения «точно в срок»
listcomp = ['Привет' for i in range(3)] # <-скобки квадратные
genexpr = ('Привет' for i in range(3)) # <- скобки круглые

print(listcomp)
# ['Привет', 'Привет', 'Привет']
print(genexpr)
# <generator object <genexpr> at 0x1036c3200>
# Прочитать выражение генератор можно следующими способами
# вар 1
print(next(genexpr))
# 'Привет'
print(next(genexpr))
# 'Привет'
# print(next(genexpr))
# StopIteration

# вар2
genexpr = ('Привет' for i in range(3))
print(list(genexpr))
# ['Привет', 'Привет', 'Привет']

# фильтры занчений
even_squares = (x * x for x in range(10) if x % 2 == 0)

# Встраиваемые выражения-генераторы

for x in ('Buongiorno' for i in range(3)):
    print(x)

# Круглые скобки, окружающие выражение-генератор, могут быть опущены, если выражение-генератор
# используется в качестве единственного аргумента функции:
sum((x * 2 for x in range(10)))
# 90
# Сравните с:
sum(x * 2 for x in range(10))
# 90

# ------------------Цепочки итераторов--------------
def integers():
    for i in range(1, 9):
        yield i

print(list(integers()))

# Вы можете взять «поток» значений, выходящих из генератора integers(), и направить их в еще один генератор
def squared(seq):
    for x in seq:
        yield x * x

print(list(squared(integers())))

# и еще раз

def negated(seq):
     for i in seq:
        yield -i

chain = negated(squared(integers()))
print(list(chain))

# теперь можно перевести в генераторы выражений и получим тоже самое но короче:
integers = range(1, 9)
squared = ( x * x for x in integers)
negated = (-i for i in squared)

print(list(negated))


