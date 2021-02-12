# Задание 2
# Написать функцию которая будет простое число возводить в квардрат
# Необходимо возвести в квадрат все простые числа в списке используя функцию map

spisok = [1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20]
spisok2 =[]
def func_prostoe_chislo(num):
    if num == 1:
        return False
    my_list = []
    sqrt_num= round(num**0.5)
    for delitel in range(2, sqrt_num + 1):
        if num % delitel == 0:
            my_list.append(delitel)
    if len(my_list) == 0:
        num **=2
        spisok2.append(num)
    else:
        return False

b= list(map(func_prostoe_chislo, spisok))
print(spisok2)




