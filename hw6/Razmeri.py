# Написать функцию перевода размеров женского белья из международного во все остальные.
# Внутри функции нужно просто обращаться к правильно составленному словарю.

XXS = {'Rus': 42, 'Germany': 36, 'USA': 8, 'France': 38, 'Great Britain': 24}
my_comand = {'XS': 2, 'S': 4, 'M': 6, 'L': 8, 'XL': 10, 'XXL': 12, 'XXXL': 14}
razmeri_chisla = list(XXS.values())
otvet = []
razmeri_keys = list(XXS.keys())

input_comand = my_comand[input("Введите размер: ").upper()]
input_comand = int(input_comand)


def func(razmer):
    for nums in razmeri_chisla:
        number = nums + razmer
        otvet.append(number)


func(input_comand)

otvet = zip(razmeri_keys, otvet)
otvet = dict(otvet)
print(otvet)
