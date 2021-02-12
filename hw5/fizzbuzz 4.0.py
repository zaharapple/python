file = open('yslovie.txt', 'r')
file2 = open('newfile1.txt', 'w')
a = [list(map(int, line.split())) for line in file]
fizz_name = 'F'
buzz_name = 'B'


def funcBuz(n):
    b = list(range(1, n[2] + 1))

    def funcBuz2(b):
        if b % n[0] == 0 and not b % n[1] == 0:
            print(fizz_name, end=" ")
            file2.write(str(fizz_name))
        elif b % n[1] == 0 and not b % n[0] == 0:
            print(buzz_name, end=" ")
            file2.write(str(buzz_name))
        elif b % n[1] == 0 and b % n[0] == 0:
            print(fizz_name + buzz_name, end=" ")
            file2.write(str(fizz_name + buzz_name))
        else:
            print(b, end=" ")
            file2.write(str(b))

    d = list(map(funcBuz2, b))
    file2.write('\n')


c = list(map(funcBuz, a))

file2.write('\n')
file.close()
file2.close()
