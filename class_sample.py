
class Rectangle:  # 長方形

    def __init__(self, width, height):  # 建構子
        self.width = width
        self.height = height


    def get_area(self):  # method 求面積
        return self.width * self.height

    # setter
    def set_a(self, value):
        self.a = value

    # getter
    def get_a(self):
        return self.a

class Square(Rectangle):  # 正方形

    def __init__(self, length):  # 建構子
        self.width = length
        self.height = length
        self.a = None

def test():  # X method,  O function
    pass

r1 = Rectangle(5,10)
r2 = Rectangle(10,20)
s1 = Square(5)

print('')

