import re

text = open('mod8test.txt', mode='r').read()
text = text.split('\n')

regex1 = '\d{2}:\d{2}:\d{2}'
regex2 = '\d{3}'
regex3 = '\w* [А-Я]{1}\w*'

for x in text:
    if (re.findall(regex3, x)):
        t = (re.search(regex1, x)) # + " - Поезд No "+  + " " + str(re.findall(regex3, x))
        n = (re.search(regex2, x))
        c = (re.search(regex3, x))
        print(t.group(0) + " - Поезд No "+ n.group(0) + " " + c.group(0))


'''
Рейс 365 прибыл из Сасово в 12:56:30
сообщение получено в 12:57:20
Сохранено в базу данных
Рейс 452 отправился в Сочи в 13:04:22
сообщение получено в 13:11:32
Ошибка записи в базу данных

[12:56:30] - Поезд No 365 из Сасово
[13:04:22] - Поезд No 452 в Сочи
'''












'''
regex = '\w{4} \d{3} .*'
text = open('mod8test.txt', mode='r').read()
rows = (re.search(regex, text))


xx = (re.search('\d{2}:\d{2}:\d{2}', text, re.I))
print(xx.group(0))



for x in rows:
    print(re.search('\d{2}:\d{2}:\d{2}' x))
'''
