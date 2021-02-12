#Предлагаем ввести число
number = int(input('Введите любое от 1 до 9999 число:'))

#Создаем переменные с подчетом
b= number % 10
c= (number // 10) % 10
x= (number // 100) % 10
y= number // 1000
#переводим переменную number в строку
number = str(number)
#высчитываем количество символов в строке
kol_vo = len(number)
# Делаем проверку количество символов в строке
if kol_vo == 1:
    print("1 *", b)
elif kol_vo == 2:
    print("10 * ",c, "+","1 *", b)
elif kol_vo == 3:
    print("100 *", x, "+","10 * ",c, "+","1 *", b)
elif kol_vo == 4:
    print("1000 *", y, "100 *", x, "+","10 * ",c, "+","1 *", b)
else:
    print("Erorr")