init_rating = [7, 5, 3, 3, 2]
init_rating.sort(reverse=True)

while True:
    new = int(input('введите новое значение: '))
    if new in init_rating:
        ind = init_rating.index(new)
        init_rating.insert(ind + 1, new)
    else:
        init_rating.append(new)
        init_rating.sort(reverse=True)
    print(init_rating)

