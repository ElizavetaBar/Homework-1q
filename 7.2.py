from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, w, h):
        self.w = w
        self.h = h

    @abstractmethod
    def sq_full(self, w, h):
        return f'Площадь ткани \n {(self.w / 6.5 + 0.5) + (self.h * 2.0 + 0.3)}'


class Coat(Clothes):
    def __init__(self, w, h):
        super().__init__(w, h)
        self.square_c = self.w / 6.5 + 0.5

    def __str__(self):
        return f'Площадь на пальто {self.square_c}'

    def square_c(self):
        return self.w / 6.5 + 0.5

    def sq_full(self, w, h):
        return f'Площадь ткани \n {(self.w / 6.5 + 0.5) + (self.h * 2.0 + 0.3)}'


class Suit(Clothes):
    def __init__(self, w, h):
        super().__init__(w, h)
        self.square_s = 2 * self.h + 0.3

    @property
    def square_s(self):
        return self.h * 2 + 0.3

    @square_s.setter
    def square_s(self, h):
        if h < 1:
            self.h = 1
        elif h > 3:
            self.h = 3
        else:
            self.h = h

    def __str__(self):
        return f'Площадь на костюм {self.square_s}'

    def sq_full(self, w, h):
        return f'Площадь ткани \n {(self.w / 6.5 + 0.5) + (self.h * 2.0 + 0.3)}'


coat = Coat(2, 1)
suit = Suit(1, 2)

print(coat)
print(suit)

print(suit.sq_full(2, 1))
