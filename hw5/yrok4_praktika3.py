# Вспоминаем работу с файлом. Есть файл, в котором много англоязычных
# текстовых строк. Считаем частоту встретившихся слов в файле,
# но через функции и map, без единого цикла
my_text = open('anglslova.txt', 'r')
text_string = my_text.read()
from collections import Counter

print(Counter(
    [''.join(filter(str.isalpha, x.lower())) for x in text_string.split() if ''.join(filter(str.isalpha, x.lower()))]))
