# import time as tm
#
# class TrafficLight:
#     def __init__(self, color):
#         self.__color = color
#
#
#     def running(self):
#         i = 0
#         while i < 3:
#             print(f'{self.__color[i]}')
#             i += 1
#             #time.sleep(3)
#
# a = TrafficLight(['красный', 'желтый', 'зеленый'])
# a.running()
# import time as tm
#
# class TrafficLight:
#     def __init__(self, color):
#         self.__color = color
#
#
#     def running(self):
#         a = 0
#         while a < 50:
#             for i in self.__color:
#                 print(f'{self.__color[i == 1]}')
#                 tm.sleep(7)
#                 print(f'{self.__color[i == 1]}')
#                 tm.sleep(2)
#                 print(f'{self.__color[i == 2]}')
#                 tm.sleep(4)
#                 print(f'{self.__color[i == 1]}')
#                 tm.sleep(2)
#             a += 1
#
# a = TrafficLight(['красный', 'желтый', 'зеленый'])
# a.running()

import time as tm

class TrafficLight:
    def __init__(self, color):
        self.__color = color


    def running(self):
        a = 0
        while a < 50:
                print(f'{self.__color}')
                tm.sleep(7)

                self.__color = 'желтый'
                print(f'{self.__color}')
                tm.sleep(2)

                self.__color = 'зеленый'
                print(f'{self.__color}')
                tm.sleep(4)

                self.__color = 'желтый'
                print(f'{self.__color}')
                self.__color = 'красный'
                tm.sleep(2)
        a += 1

b = TrafficLight('красный')
b.running()