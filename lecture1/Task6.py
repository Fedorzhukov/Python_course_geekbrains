init_dist = int(input('В первый день пробегает км: '))
target_dist = int(input('Сколько хотим чтобы пробегал км: '))

day = 1
current_dist = init_dist
while target_dist >= current_dist:
    day += 1
    current_dist = current_dist + current_dist * 0.1

print('На ' + str(day) + ' день он пробежит ' + str(current_dist) + ' км')

