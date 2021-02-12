# Создать словарь оценок предполагаемых студентов (Ключ - ФИ студента, значение - список оценок студентов).
# Найти самого успешного и самого отстающего по среднему баллу.
students = {'Ivanov Sergey': [3, 5, 5], 'Sidorov Evgeniy': [5, 5, 2], 'Kravchenko Denis': [4, 4, 3],
            'Denisov Egor': [3, 2, 3], 'Kylakov Sergey': [3, 4, 3]}
stud_reting = list(students.values())
sredniy_bal = []
stud_name = list(students.keys())

# функция которая считает средний бал
def listsum(numList):
    global my_result
    theSum = 0
    for i in numList:
        theSum = theSum + int(i)
        my_result = theSum / len(numList)
    return my_result

# Создаем цикл который помещает наших студентов в нашу функцию
# ипереносит средний бал в новый список
cnt = 0
while cnt < len(stud_reting):
    sred = listsum(stud_reting[cnt])
    sred = round(sred, 1)
    sredniy_bal.append(sred)
    cnt += 1
# с помощью zip обьеденяем список с учениками
# и их средним балом и переводим все в словарь
my_reshenie = zip(stud_name, sredniy_bal)
my_reshenie = dict(my_reshenie)

# создаем цикл for для поиска максимального и минимального бала
mn = 999
mx = 0
for key, value in my_reshenie.items():
    # print(key, value)
    if value > mx:
        key_mx = key
        mx = value
    if mn > value:
        key_mn = key
        mn = value

print('Минимальный бал:', key_mn, mn)
print('Максимальный бал:', key_mx, mx)
