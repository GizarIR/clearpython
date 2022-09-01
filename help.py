
import datetime

# набираем в терминале puthon или через print
dir(datetime)
# ['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__',
#   '__doc__', '__file__', '__loader__', '__name__',
#   '__package__', '__spec__', '_divide_and_round',
#   'date', 'datetime', 'datetime_CAPI', 'time',
#   'timedelta', 'timezone', 'tzinfo']

print(dir(datetime.date))
# ['__add__', '__class__', ..., 'day', 'fromordinal',
#   'isocalendar', 'isoformat', 'isoweekday', 'max',
#   'min', 'month', 'replace', 'resolution', 'strftime',
#   'timetuple', 'today', 'toordinal', 'weekday', 'year']

print([_ for _ in dir(datetime) if 'date' in _.lower()])
# ['date', 'datetime', 'datetime_CAPI']

print(help(datetime))

# разберем функцию до винтиков
def greet(name):
    return 'Привет, ' + name + '!'

print(greet('Гвидо'))
# 'Привет, Гвидо!'

# Вместо того чтобы непосредственно исполнить человекочитаемый исход- ный код, в Python используются компактные
# цифровые коды, константы и ссылки, которые представляют результат лексического и семантическо- го анализа,
# выполняемого компилятором.
# Это экономит время и оперативную память для повторных исполнений программ или частей программ. Например, байткод,
# который получается в результате этого шага компиляции, кэшируется на диске в файлах .pyc и .pyo
# его можно посмотреть
print(greet.__code__.co_code)
# b'dx01|x00x17x00dx02x17x00Sx00'
print(greet.__code__.co_consts)
# (None, 'Привет, ', '!')
print(greet.__code__.co_varnames)
# ('name',)

# БОлее читабельно
# Дизассемблер байткода Python располагается в модуле dis, который яв- ляется составной
# частью стандартной библиотеки. Поэтому мы можем его просто импортировать и вызвать dis.dis() с
# функцией greet в каче- стве аргумента, чтобы получить более удобочитаемое представление о ее байткоде:

import dis
print(dis.dis(greet))
#  25           0 LOAD_CONST               1 ('Привет, ')
#               2 LOAD_FAST                0 (name)
#               4 BINARY_ADD
#               6 LOAD_CONST               2 ('!')
#               8 BINARY_ADD
#              10 RETURN_VALUE
# None