import csv

with open('scientist.txt', encoding = 'utf8') as file:

    '''Эта часть кода получает данные из файла scientist.txt'''

    f = list(csv.reader(file, delimiter = '#', quotechar = '"'))
    f = f[1:]
    flag = 0
    date = input().split(sep='.')
    date_n = int(date[2])*365 + int(date[1])*12 + int(date[0])
    for s in f:
        date_list = s[2].split(sep = '-')
        date_a = int(date_list[0])*365 + int(date_list[1])*12 + int(date_list[2])
        if date_n == date_a:
            name_list = s[0].split()
            name = name_list[0] + ' ' + name_list[1][:1] + '. ' + name_list[2][:1] + '.'
            print('Ученый ', name, ' 24.02.1создал препарат: ', s[1], ' - ', s[2])
            flag = 1
    if flag == 0:
        print('В этот день ученые отдыхали')
