x = int(input('Что надо возвести в степень: '))
y = 0
while y >= 0:
    y = int(input('В какую степень надо возвести {}^'.format(x)))

# 1
def my_func_one(x, y):
    return x ** (y)
# 2
def my_func_two(x, y):
    for i in range(abs(y)-1):
        x += x
    return 1/x


print(x, '^', y, '=', my_func_one(x, y))
print(x, '^', y, '=', my_func_two(x, y))