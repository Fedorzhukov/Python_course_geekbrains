list_one = list(input('введите элементы листа: '))
if len(list_one) % 2 == 0:
    for num, i in enumerate(list_one):
        if num % 2 == 0:
            print(num)
            list_one[num], list_one[num + 1] = list_one[num + 1], list_one[num]
else:
    for num, i in enumerate(list_one[:len(list_one)-1]):
        if num % 2 == 0:
            print(num)
            list_one[num], list_one[num + 1] = list_one[num + 1], list_one[num]
print(list_one)



