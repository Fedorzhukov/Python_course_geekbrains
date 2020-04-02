def my_func(x, y, z):
    init_vars = [x, y, z]
    max_one = max(init_vars)
    init_vars.remove(max_one)
    max_two = max(init_vars)
    return max_one + max_two

result = my_func(10, 9, 1)
print(result)