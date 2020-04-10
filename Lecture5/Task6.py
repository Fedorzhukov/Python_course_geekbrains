my_dict = {}
with open('Test_file5.txt') as fl:
    lines = fl.readlines()
    for i in lines:
        line_content = i.split(' ')
        subj = line_content[0]
        lst = []
        for j in line_content[1:]:
            try:
                lst.append(int(((j.split('('))[0])))
            except ValueError:
                pass
        my_dict[subj] = sum(lst)
print(my_dict)