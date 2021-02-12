number = int(input('Введите любое число:'))
a = lambda x : [n for n in range(1, x+1) if x % n ==0]

print(a(number))