num_products = int(input('Сколько товаров будет в магазине? '))
main_list = []
list_names = []
list_price = []
list_amount = []
list_meas = []

for i in range(num_products):
    prod_name = input('Введите название {}-го товара: '.format(i + 1))
    prod_price = float(input('Введите цену {}-го товара: '.format(i + 1)))
    prod_amount = int(input('Введите количество {}-го товара: '.format(i + 1)))
    meas_amount = input('Введите единицы измерения {}-го товара: '.format(i + 1))
    main_list.append((i + 1, {'Название': prod_name, 'цена': prod_price, 'количество': prod_amount, 'eд': meas_amount}))

for i in range(len(main_list)):
    temp_list_one = main_list[i]
    temp_list_two = temp_list_one[1]
    list_names.append(temp_list_two['Название'])
    list_price.append(temp_list_two['цена'])
    list_amount.append(temp_list_two['количество'])
    list_meas.append(temp_list_two['eд'])
analysis = {'Название': list_names, 'цена': list_price, 'количество': list_amount, 'eд': list_meas}
print(analysis)


# Вопросы:
# 1) всегда ли надо создавать пустые листы, как я это сделал в начале, чтобы внутри цикла к ним доабвлять что-то?
#    или есть более эффективный способ?
# 2) Хотел сделать доп цикл с while, который бы бесконечно гонял пользователя, если, например, в поле цены пользователь
# вводит не число, а текст, но не получилось. Как лучше это реализовать?
# 3) В целом длина кода оптимальна? или можно было бы короче и компактнее?