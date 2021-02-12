#Есть три числа которые пользователь должен ввести
print('''Привет , тебя приветствует программ fizz-buzz
введите 3 числа
''')
fizz = int(input('Введите число №1 :'))
buzz = int(input('Введите число №2 :'))
number = int(input('Введите число №3 :'))

print(fizz ,buzz, number )
#Делаем список от 1го до задоного числа
a=list(range(1, number + 1))
#создаем переменные с нужным названием
fizz_name='F'
buzz_name='B'
#Делаем цикл проверки кратности
for i in a:
    if i  %  fizz == 0 and not i % buzz ==0:
        print(fizz_name, end=" ")
    elif i % buzz == 0 and not i % fizz ==0:
        print(buzz_name, end=" ")
    elif i % buzz == 0  and i %  fizz == 0:
        print(fizz_name + buzz_name, end=" ")
    else:
        print(i, end=" ")
