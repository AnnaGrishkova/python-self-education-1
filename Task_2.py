print('Привет,я Юлька')
print('1 уровень')
print('1) Введите число a и число b. Возведите число a в степень b')
a = int(input ("Введите число: "))
b = int (input ( "Введите число: "))
print(a ** b)

print('2) Пользователь вводит 2 числа. Покажите большее из них')
aa = int(input ("Введите число: "))
bb = int (input ( "Введите число: "))
print(max(aa,bb))

print('3) Пользователь вводит сумму в грн и курс доллара. Нужно пересчитать сумму в долларах')
aaa = int(input ("Введите число: "))
bbb = int (input ( "Введите число: "))
print(aaa/bbb)

print('4) Пользователь вводит цифру от 1 до 7. Нужно показать соответствующий день недели')
q = int(input('Введите день: '))
if q == 1:
    print('Понедельник')
elif q == 2:
    print('Вторник')
elif q == 3:
    print('Среда')
elif q == 4:
    print('Четверг')
elif q == 5:
    print('Пятница')
elif q == 6:
    print('Суббота')
else:
    print('Воскресенье')


print('2 уровень')
print('1) Введите число,если оно четное,отобразить "четное", если нечетное,отобразить "нечетное"')
q = int(input ("Введите число: "))
if q % 2 == 0:
    print('четное')
else:
     print('нечетное')



print('2) Пользователь вводит 3 числа. Покажите наименьшее из них')
aa = int(input ("Введите число: "))
bb = int (input ( "Введите число: "))
cc = int (input ( "Введите число: "))
print(min(aa,bb,cc))

print('3) Из Убудского чата Аня узнала, что рекомендуется спать хотя бы А часов в сутки, \n'
      'но пересыпать тоже вредно и не стоит спать более В часов. Сейчас Аня спит Н часов в сутки.\n'
      ' Если режим сна Ани удовлетворяет рекомендациям Сергея, выведите "Это нормально".\n'
      ' Если Аня спит менее А часов, выведите "Недосып", если же более В часов, то выведите "Пересып"')
aaa = int(input ("Введите число A(минимум сна): "))
bbb = int (input ( "Введите число В(максимум сна): "))
ccc = int (input ( "Введите число С(сколько спит Аня): "))

if ccc < aaa:
      print('недосіп')
elif ccc > bbb:
      print('пересіп')
else:
      print('норма')


