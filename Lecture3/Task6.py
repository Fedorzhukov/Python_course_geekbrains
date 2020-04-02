def int_func(x):
    return x.title()

text = input('введите строку: ').lower()
text_new = ''
for i in text.split(' '):
    int_func(i)
    text_new += int_func(i) + ' '

print(text_new)