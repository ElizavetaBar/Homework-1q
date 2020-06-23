from random import randint

my_list = []


def generator():
    a = 1
    while a < 12:
        b = randint(1, 1000)
        my_list.append(b)
        a += 1


generator()

new_list = []
for i in range(1, len(my_list)):

    if my_list[i] > my_list[i - 1]:
        new_list.append(my_list[i])
    else:
        continue

print(my_list)
print(new_list)
