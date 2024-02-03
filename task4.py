'''Данная программа добавляет логин и пароль к каждой записи в scientist.txt и записывает обновлённые данные в scientist_password.csv'''

import csv
import random

def pass_gen():
    '''Эта функция генерирует 10-значный пароль'''

    a = 'abcdefghijklmnopqrstuvwxyz'
    b = a.upper()
    c = '0123456789'
    a = a + b + c
    password = str()
    for i in range(10):
        password  = password + a[random.randint(0, 61)]
    return password


with open('scientist.txt', encoding = 'utf8') as file:

    f = list(csv.reader(file, delimiter = '#', quotechar = '"'))
    f = f[1:]
    for s in f:
        '''Эта часть кода добавляет логин и пароль в каждую запись об открытии
        
        Описание аргументов:
        name_list - список из имени, фамилии и отчества ученого из s
        name - преобразованный в строку ФИО name_list в формате Фамилия_ИО (логин)
        password - сгенерированный pass_gen() пароль

        '''
        name_list = s[0].split()
        name = name_list[0] + '_' + name_list[1][:1] + name_list[2][:1]
        s.append(name)
        password = pass_gen()
        s.append(password)

with open('scientist_password.csv', 'w', encoding = 'utf8', newline = '') as file:

    '''Эта часть кода записывает полученные данные в новый файл scientist_password.csv'''

    w = csv.writer(file, delimiter = '#', quotechar = '"')
    w.writerow(['ScientistName', 'preparation', 'date', 'components', 'login', 'password'])
    w.writerows(f)
