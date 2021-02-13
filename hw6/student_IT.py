# Создать структуру данных для студентов из имен и фамилий, можно случайных.
# Придумать структуру данных, чтобы указывать, в какой группе учится студент
# (Группы Python, FrontEnd, FullStack, Java). Студент может учиться в нескольких группах. Затем вывести:
# 1. студентов, которые учатся в двух и более группах
# 2. студентов, которые не учатся на фронтенде
# 3. студентов, которые изучают Python или Java

group_Python = {'Smith', 'Johnson', 'Miller', 'Taylor'}
group_FrontEnd = {'Williams', 'Miller', 'Thomas', 'Harris'}
group_FullStack = {'Smith', 'Wilson', 'Hernandez', 'Harris'}
group_Java = {'Johnson', 'Wilson', 'Martin', 'Lee'}

peresechenie = group_Java & group_Python and group_FullStack & group_FrontEnd
print(str(peresechenie))

what = int(input('''\n1. Если хотите узнать количество студентов, которые учатся в двух и более группах введите : "1"
2. Если хотите узнать количество студентов, которые не учатся на фронтенде введите :        "2"
3. Если хотите узнать количество студентов, которые изучают Python или Java введите :       "3" 
                                             Введите команду : '''))

if what == 1:
    peresechenie = (group_Java & group_FrontEnd) | (group_Java & group_FullStack) | (group_Java & group_Python) | (
            group_FullStack & group_FrontEnd) | (group_FullStack & group_Python) | (group_FrontEnd & group_Python)
    print(str(peresechenie))
elif what == 2:
    peresechenie = (group_Python | group_FullStack | group_Java) - group_FrontEnd
    print(peresechenie)
elif what == 3:
    peresechenie = group_Python | group_Java
    print(peresechenie)
else:
    print('Неверная команда')

