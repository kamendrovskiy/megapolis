import csv

with open('scientist.txt', encoding = 'utf8') as file:
    f = list(csv.reader(file, delimiter = '#', quotechar = '"'))
    f = f[1:]
    c = {}
    names = []
    dates = []
    for s in f:
        date_list = s[2].split(sep = '-')
        date = int(date_list[0])*365 + int(date_list[1])*12 + int(date_list[2])
        date_old = c.get(s[1], 0)
        if date_old == 0 or date < date_old:
            c[s[1]] = date
        if 'Аллопуринол'in s[1]:
            names.append(s[0])
            dates.append(s[2])
    for s in f:
        date_list = s[2].split(sep = '-')
        date = int(date_list[0])*365 + int(date_list[1])*12 + int(date_list[2])
        date_ideal = c.get(s[1], 0)
        if date > date_ideal:
            f.remove(s)

with open('scientist_origin.txt', 'w', encoding = 'utf8', newline = '') as file:
    w = csv.writer(file, delimiter = '#', quotechar = '"')
    w.writerow(['ScientistName', 'preparation', 'date', 'components'])
    w.writerows(f)
print('Разработчиками Аллопуринола были такие люди:')
for i in range(len(names)):
    print(names[i], ' - ', dates[i])
for i in range(len(names)):
    date = dates[i]
    date_list = date.split(sep = '-')
    date = int(date_list[0])*365 + int(date_list[1])*12 + int(date_list[2])
    if date == c['Аллопуринол']:
        print('Оригинальный рецепт принадлежит: ', names[i])
    