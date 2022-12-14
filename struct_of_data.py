from collections import OrderedDict, defaultdict, ChainMap
from types import MappingProxyType

# ---------------СЛОВАРИ---------------

# OrderedDict - сохранит порядок следования ключей

d = OrderedDict(one=1, two=2, three=3)
d['четыре'] = 4
print(d)
# OrderedDict([('one', 1), ('two', 2), ('three', 3), ('четыре', 4)])

# collections .defaultdict — возвращает значения, заданные по умолчанию для отсутствующих ключей
dd = defaultdict(list)
# Попытка доступа к отсутствующему ключу его создает и
# инициализирует, используя принятую по умолчанию фабрику, # то есть в данном примере list():
dd['собаки'].append('Руфус')
dd['собаки'].append('Кэтрин')
dd['собаки'].append('Сниф')
print(dd['собаки'])
# ['Руфус', 'Кэтрин', 'Сниф']

# collections .ChainMap — производит поиск в многочисленных словарях как в одной таблице соответствия
dict1 = {'один': 1, 'два': 2}
dict2 = {'три': 3, 'четыре': 4}
chain = ChainMap(dict1, dict2)
print(chain)
# ChainMap({'один': 1, 'два': 2}, {'три': 3, 'четыре': 4})
print(chain['три'])
# 3
print(chain['один'])
# 1

# types .MappingProxyType — обертка для создания словарей только для чтения
writable = {'один': 1, 'два': 2}  # доступный для обновления
read_only = MappingProxyType(writable) # Этот представитель/прокси с доступом только для чтения:
print(read_only['один'])
# 1
# read_only['один'] = 23
# TypeError: "'mappingproxy' object does not support item assignment"
# Обновления в оригинале отражаются в прокси:
writable['один'] = 42
print(read_only)
# mappingproxy({'один': 42, 'один': 2})

# -----------МАССИВЫ--------------
# lis - динамически массив, структура следит за выделяемым объемео резервирования памяти при операция
# удаления, добавления и вставки
list_ = [1, 2, 3]

# кортежи не изменные тип данных
my_tuple = 1, 2, 3
print(my_tuple[0])
# my_tuple[0] = 23
# TypeError: 'tuple' object does not support item assignment

# массивы - «типизированными массивами», ограниченными единственным типом данных. чтоявляется более пространственно
# эффективным и позволяет хранить данные более плотно чем
import array
arr = array.array('f', (1.0, 0.5, 1.5, 2.0))
print(arr[1])
print(arr)
# могут меняться
arr[1] = 3
print(arr)
arr.append(43)
print(arr)
# # Массивы — это "типизированные" структуры данных:
# arr[1] = 'привет'
# TypeError: "must be real number, not str"

# Строки - неизменяемы
arr = 'abcd'
# arr[1] = 'e'
# TypeError:
# "'str' object does not support item assignment"

print(list(arr))
print(''.join(list(arr)))


# bytes — неизменяемые массивы одиночных байтов
# целых чисел в диапазоне 0 ≤ x ≤ 255
arr = bytes((0, 1, 2, 3))
print(arr[1])
# 1
# Байтовые литералы имеют свой собственный синтаксис:
print(arr)
b'x00x01x02x03'
arr = b'x00x01x02x03'

# # Байты неизменяемы:
# >>> arr[1] = 23
# TypeError:
# "'bytes' object does not support item assignment"
# >>> del arr[1]
# TypeError:
# "'bytes' object doesn't support item deletion"

# bytearray — изменяемые массивы одиночных байтов
# последовательность целых чисел в диапазоне 0 ≤ x ≤ 255

arr = bytearray((0, 1, 2, 3))
print(arr[1])
# 1
# Метод repr для bytearray:
print()
# bytearray(b'x00x01x02x03')
# Байтовые массивы bytearray изменяемы:
arr[1] = 23
print(arr)
# bytearray(b'x00x17x02x03')
print(arr[1])
# 23
# Байтовые массивы bytearray могут расти и сжиматься в размере:
del arr[1]
arr.append(42)
print(arr)
bytearray(b'x00x02x03*')
# Байтовые массивы bytearray могут содержать только "байты"
# # (целые числа в диапазоне 0 <= x <= 255)
# >>> arr[1] = 'привет'
# TypeError: "an integer is required"
# >>> arr[1] = 300
# ValueError: "byte must be in range(0, 256)"
# # Bytearrays может быть преобразован в байтовые объекты: # (Это скопирует данные)
# >>> bytes(arr)
# b'x00x02x03*'

# ----------------Записи и структуры----------------------
# Рекомендации по структурам данных для органиазции записей:
#
# У вас есть всего несколько (2–3) полей: использование обыкновенного объекта-кортежа может подойти, если порядок
# следования полей легко запоминается или имена полей излишни. Например, представьте точку (x, y, z) в трехмерном
# пространстве.
#
# Вам нужны неизменяемые поля: в данном случае обыкновенные кортежи, collections.namedtuple и typing.NamedTuple,
# дадут неплохие возмож ности для реализации этого типа объекта данных.
#
# Вам нужно устранить имена полей, чтобы избежать опечаток: вашими друзьями здесь будут collections.namedtuple и
# typing.NamedTuple.
#
# Вы не хотите усложнять: обыкновенный объект-словарь может быть хорошим вариантом из-за удобного синтаксиса,
# который сильно напоминает JSON. Или types .SimpleNamespace — причудливый атрибутивный доступ
#
# Вам нужен полный контроль над вашей структурой данных: самое время написать собственный класс с
# методами-модификаторами (сеттерами) и методами-получателями (геттерами) @property.
#
# Вам нужно добавить в объект поведение (методы): вам следует на- писать собственный класс с нуля либо путем
# расширения collections. namedtuple или typing.NamedTuple.
#
# Вам нужно плотно упаковать данные, чтобы сериализовать их для записи на жесткий диск или отправить их по Сети:
# самое время навести справки по поводу struct.Struct, потому что этот объект представляет собой превосходный
# вариант использования.

# ----------МНОЖЕСТВА-------------
# set
vowels = {'а', 'о', 'э', 'и', 'у', 'ы', 'е', 'е', 'ю', 'я'}
print('э' in vowels)

# frozenset — неизменяемые множества
vowels = frozenset({'а', 'о', 'э', 'и', 'у', 'ы', 'е', 'е', 'ю','я'})
# vowels.add('р')
# AttributeError "'frozenset' object has no attribute 'add'"

# Множества frozenset хешируемы и могут
# использоваться в качестве ключей словаря:
d = { frozenset({1, 2, 3}): 'привет' }
print(d[frozenset({1, 2, 3})])
# 'привет'

# collections .Counter — мультимножества
from collections import Counter
inventory = Counter()
loot = {'клинок': 1, 'хлеб': 3}
inventory.update(loot)
print(inventory)
# Counter({'клинок': 1, 'хлеб': 3})
more_loot = {'клинок': 1, 'яблоко': 1}
inventory.update(more_loot)
print(inventory)
Counter({'клинок': 2, 'хлеб': 3, 'яблоко': 1})

print(len(inventory))
# 3 # Количество уникальных элементов
print(sum(inventory.values()))
# 6 # Общее количество элементов

#-----------СТЭКИ LIFO------------
# простые встроенные через list
list_ = []
list_.append(1)
list_.append(2)
list_.pop()
list_.pop()

# collections .deque — быстрые и надежные стеки
# Класс deque реализует очередь с двусторонним доступом, которая под- держивает добавление и удаление
# элементов с любого конца за O(1) (неамортизируемое) время.

from collections import deque
s = deque()
s.append('есть')
s.append('спать')
s.append('программировать')
print(s)
# deque(['есть', 'спать', 'программировать'])
print(s.pop())
# 'программировать'
s.pop()
# 'спать'

# deque .LifoQueue — семантика блокирования для параллельных вычислений

from queue import LifoQueue
s = LifoQueue()
s.put('есть')
s.put('спать')
s.put('программировать')
print(s)
# <queue.LifoQueue object at 0x108298dd8>
print(s.get())
# 'программировать'
print(s.get())
# 'спать'
print(s.get())
# 'есть'
# print(s.get_nowait())
# raise queue.Empty
# s.get()
# Блокирует / ожидает бесконечно...


# лучше всего использовать список list (append и pop) или
# двустороннюю очередь deque.

# --------------ОЧЕРЕДИ FIFO-----------------
#  list - ужастно мееееедленная очередь
q = []
q.append('есть')
q.append('спать')
q.append('программировать')
print(q)
# ['есть', 'спать', 'программировать']
# Осторожно: это очень медленная операция! О(n) - нужно сдвинуть все эелементы очереди
q.pop(0)
# 'есть'


# Но есть решение - collections .deque — быстрые и надежные очереди
#
# Класс deque реализует очередь с двусторонним доступом, которая под- держивает добавление и удаление элементов
# с любого конца за O(1) (неамортизируемое) время. Поскольку двусторонние очереди одинаково хорошо поддерживают
# добавление и удаление элементов с любого конца, они могут служить в качестве очередей и в качестве стеков1.

from collections import deque
q = deque()
q.append('есть')
q.append('спать')
q.append('программировать')
print(q)
deque(['есть', 'спать', 'программировать'])
q.popleft()
# 'есть'
q.popleft()
# 'спать'
q.popleft()
# 'программировать'
# q.popleft()
# IndexError: "pop from an empty deque"

# queue .Queue — семантика блокирования для параллельных вычислений
from queue import Queue
q = Queue()
q.put('есть')
q.put('спать')
q.put('программировать')
print(q)
# <queue.Queue object at 0x1070f5b38>
q.get()
# 'есть'
q.get()
# 'спать'
q.get()
# 'программировать'
# q.get_nowait()
# queue.Empty
# q.get()
# Блокирует / ожидает бесконечно...

# multiprocessing .Queue — очереди совместных заданий
# Такая реализация очереди совместных заданий позволяет выполнять па- раллельную обработку находящихся
# в очереди элементов многочисленны- ми параллельными рабочими процессами

from multiprocessing import Queue
q = Queue()
q.put('есть')
q.put('спать')
q.put('программировать')
print(q)
# <multiprocessing.queues.Queue object at 0x1081c12b0>
q.get()
# 'есть'
q.get()
# 'спать'
q.get()
# 'программировать'
# q.get()
# Блокирует / ожидает бесконечно...

# Вывод: Если вы не ищете поддержку параллельной обработки, то реализация, предлагаемая очередью collections.deque,
# является превосходным вариантом по умолчанию для реализации в Python

# -----------------Очереди с приоритетом--------
# Если list , тогда — поддержание сортируемой очереди вручную

q = []
q.append((2, 'программировать'))
q.append((1, 'есть'))
q.append((3, 'спать'))
# ПРИМЕЧАНИЕ: Не забудьте выполнить пересортировку всякий раз,
#             когда добавляется новый элемент, либо используйте
# bisect.insort(). q.sort(reverse=True)
while q:
    next_item = q.pop()
    print(next_item)
# Результат:
# (1, 'есть')
# (2, 'программировать')
# (3, 'спать')

# heapq — двоичные кучи на основе списка

import heapq
q = []
heapq.heappush(q, (2, 'программировать'))
heapq.heappush(q, (1, 'есть'))
heapq.heappush(q, (3, 'спать'))
while q:
    next_item = heapq.heappop(q)
    print(next_item)
# Результат:
# (1, 'есть')
#   (2, 'программировать')
#   (3, 'спать')

# queue .PriorityQueue — красивые очереди с приоритетом (на базе heapq)
from queue import PriorityQueue
q = PriorityQueue()
q.put((2, 'программировать'))
q.put((1, 'есть'))
q.put((3, 'спать'))
while not q.empty():
    next_item = q.get()
    print(next_item)
# Результат:
# (1, 'есть')
#   (2, 'программировать')
#   (3, 'спать')

# Вывод: Реализация queue.PriorityQueue выбивается из общего ряда. Такая реализация должна быть предпочтительным
# вариантом. Если требуется избежать издержек, связанных с блокировкой очере- ди queue.PriorityQueue,
# то непосредственное использование модуля heapq


