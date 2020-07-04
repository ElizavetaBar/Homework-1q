class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __add__(self, other):
        m_l = [[self.my_list[i][j] + other.my_list[i][j] for j in range(len(self.my_list[0]))]
               for i in range(len(self.my_list))]
        return m_l

    def __str__(self):
        return 'Матрица:\n' + '\n'.join('\t'.join(map(str, line)) for line in self.my_list)


my_obj = Matrix([[3, 5, 1], [2, 4, -6], [-1, 64, -8]])

my_obj2 = Matrix([[4, 6, 2], [5, 6, -7], [2, 5, -1]])
print(my_obj)
print(my_obj2)
print(Matrix((my_obj + my_obj2)))
