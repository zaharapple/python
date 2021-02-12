# Написать fizzbuzz для 20 троек чисел, которые записаны в файл.
# Читаете из файла первую строку, берете из нее числа, считаете для них fizzbuzz, выводите.

# открываем фаил с числами
file=open('yslovie.txt', 'r')
#создаем переменные с нужным названием
fizz_name='F'
buzz_name='B'
#1. создаем функцию с ранее сделаной fizz buzz
def func():
    s0 = lines[nomer]
    spisok = [int(x) for x in s0.split()]
    fizz = spisok[0]
    buzz = spisok[1]
    number = spisok[2]
    a = list(range(1, number + 1))
    # #Делаем цикл проверки кратности
    for i in a:
        if i  %  fizz == 0 and not i % buzz ==0:
            print(fizz_name, end=" ")
        elif i % buzz == 0 and not i % fizz ==0:
            print(buzz_name, end=" ")
        elif i % buzz == 0  and i %  fizz == 0:
            print(fizz_name + buzz_name, end=" ")
        else:
            print(i  , end=" " )# Тут функция прекращает свою работу

#создаем переменную которая прочитала наши числа
lines = file.readlines()
nomer = 0
for i in lines:
    # если переменная номер меньше 20 то выполняется наша функция
    if nomer <= 20:
        func()
        #добавляем к переменной единицу для того чтоб перейти на следущюю строчку
        nomer +=1
        #если же наша переменная дошла до 21го то мы прекращаем и выводим финиш
    else:
      file.close()