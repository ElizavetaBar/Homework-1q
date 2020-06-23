from itertools import count

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = []

for el in my_list:
    if my_list.count(el) < 2:
        new_list.append(el)
    else:
        continue

print(f"Новый список: {new_list}")
