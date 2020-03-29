line = 'Привет! Меня зовут Иван Иванов. Приятно познакомиться!'
new_line = line.split(' ')
n = 0
for i in (new_line):
    if len(i) > 10:
        i = i[:10]
    print(n, i)
    n += 1