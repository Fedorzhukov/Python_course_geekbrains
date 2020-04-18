class Matrix:
    def __init__(self, user_matrix):
        self.user_matrix = user_matrix

    def __str__(self):
        output = ''
        for row in self.user_matrix:
            for elem in row:
                output += (str(elem) + ' ')
            output += '\n'
        return output

    def __add__(self, other):
        result = ''
        for row in range(len(self.user_matrix)):
            for elem in range(len(self.user_matrix[row])):
                result += str(self.user_matrix[row][elem] + other[row][elem]) + ' '
            result += '\n'
        return result

    def __getitem__(self, index):
        return self.user_matrix[index]


test1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
test2 = Matrix([[100, 100, 100], [100, 100, 100], [100, 100, 100]])

print(test1)
print('+')
print(test2)
print('=')
print(test1 + test2)

