Cityes = ['Kharkov', 'Lviv', 'Kiev', 'Odessa', 'Dnepr', 'San Francisco']
t = [-14, -10, -13, -7, -10, +17]
nasilenie = [
'1,419 миллиона (2017 г.)', '721 301 (2017 г.)', '2,884 миллиона (2017 г.)', '993 120 (2017 г.)', '966 400 (2017 г.)',
'883 305 (2018 г.)']
zip1=[]

def myzip(*args):
    result = (args)
    zip1.append(result)

def my_arg(*args):
    cnt=0
    kolvo_args = len(args)
    kolvo_args_vspiske= len(args[0])
    counter1 = 0
    counter2 = 0
    vremenniy=[]
    while cnt< kolvo_args* kolvo_args_vspiske:
        cxx=args[counter2][counter1]
        vremenniy.append(cxx)
        # print(asd)
        counter2 +=1
        cnt += 1
        if counter2 == kolvo_args:
            result = (vremenniy)
            myzip(result)
            del vremenniy
            vremenniy=[]
            counter2 = 0
            counter1 +=1


my_arg(Cityes, t, nasilenie)

print(zip1)
