viruchka = input('Выручка = ')
izderzhki = input('Издержки = ')

viruchka = int(viruchka)
izderzhki = int(izderzhki)


if viruchka > izderzhki:
    print('Вы прибыльное предприятие')
    pribil = viruchka - izderzhki
    rentabelnost = pribil/viruchka
    print('Ваша рентабельность: ' + str(rentabelnost))
    empl_num = input('Сколько человек работает: ')
    print('Ваша прибыль на одно сотрудника: ' + str(pribil/int(empl_num)))
else:
    print('Вы убыточное предприятие')



