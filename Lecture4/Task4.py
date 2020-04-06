lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6]
ind = [index for index, value in enumerate(lst) if value not in lst.remove(value)]
# Это задание никак не далось: проблема в последней части: if value not in lst.remove(value) - метод remove не подходит
# Я не смог найти  метод, который бы удалял значеие, которое повторяется несколько раз и возвращает обновлённый лист.
# Такое вообще существует?))

# Собрал вариант без генератора списка
lst2 = lst.copy()
new = []
for i in lst:
    count = 0
    while i in lst2:
        count += 1
        lst2.remove(i)
    if count == 1:
        new.append(i)
print(new)
