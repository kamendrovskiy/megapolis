'''Данная программа определяет настоящих создателей препаратов и создаёт новый файл scientist_origin.txt на основе файла scientist.txt. 
Также программа выводит отчёт полиции, сообщающий о подельниках препарата Аллопуринол и создателе оригинального препарата

Описание аргументов:
f - список списков, каждый из которых содержит информацию об открытии препарата
c - словарь, индексами которого являются препараты, а значениями - даты их открытия
names - список, содержащий имена для отчёта полиции (изобретатели Аллопуринола)
dates - список, содержащий даты открытия Аллопуринола (для индекса n дата dates[n] соответствует изобретателю names[n])

'''

import csv

with open('scientist.txt', encoding = 'utf8') as file:

    '''Эта часть кода получает данные из файла scientist.txt'''

    f = list(csv.reader(file, delimiter = '#', quotechar = '"'))
    f = f[1:]
    c = {}
    names = []
    dates = []
    for s in f:

        '''Эта часть кода находит самые ранние даты открытия препаратов, а также ищет изобретателей Аннопуринола и записывает данные о них в names и dates
        
        Описание аргументов:
        s - список, содержащий информацию об открытии. Цикл выполняется для каждого списка в f
        date_list - список, содержащий год, месяц и число даты, указанной в s
        date - дата из s, переведённая в целое число дней, используется для сравнения дат
        date_old - самая ранняя дата для данного препарата на данный момент, сравнивается с date, чтобы обновить значение самой ранней даты

        '''
        date_list = s[2].split(sep = '-')
        date = int(date_list[0])*365 + int(date_list[1])*12 + int(date_list[2])
        date_old = c.get(s[1], 0)
        if date_old == 0 or date < date_old:
            c[s[1]] = date
        if 'Аллопуринол'in s[1]:
            names.append(s[0])
            dates.append(s[2])

    for s in f:

        '''Эта часть кода выявляет и удаляет фейковые записи путём сравнения даты открытия с самой ранней из словаря c
        
        Описание аргументов:
        date_list, date - аналогичны одноимённым аргументам в предыдущем цикле
        date_ideal - самая ранняя дата, с которой сравнивается текущая для определения фейка/оригинального открытия

        '''
        date_list = s[2].split(sep = '-')
        date = int(date_list[0])*365 + int(date_list[1])*12 + int(date_list[2])
        date_ideal = c.get(s[1], 0)
        if date > date_ideal:
            f.remove(s)

with open('scientist_origin.txt', 'w', encoding = 'utf8', newline = '') as file:

    '''Эта часть кода записывает полученные данные в новый файл scientist_origin.txt'''

    w = csv.writer(file, delimiter = '#', quotechar = '"')
    w.writerow(['ScientistName', 'preparation', 'date', 'components'])
    w.writerows(f)

'''Эта часть кода выводит сообщение для полиции'''
print('Разработчиками Аллопуринола были такие люди:')
for i in range(len(names)):
    print(names[i], ' - ', dates[i])
for i in range(len(names)):
    date = dates[i]
    date_list = date.split(sep = '-')
    date = int(date_list[0])*365 + int(date_list[1])*12 + int(date_list[2])
    if date == c['Аллопуринол']:
        print('Оригинальный рецепт принадлежит: ', names[i])
    