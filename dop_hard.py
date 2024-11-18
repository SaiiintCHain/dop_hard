import math

class Figure:
    sides_count = 0
    def __init__(self,__color, __sides, filled = bool):
        self.__sides = __sides
        self.__color = list(__color)
        self.filled = filled


    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g ,b):
        if r in range(0,256) and b in range(0,256) and g in range(0,256):
            return True
        else:
            return False

    def set_color(self, r, g ,b):
        if self.__is_valid_color(r, g ,b) == True:
            self.__color = [r, g ,b]
        else:
            pass

    def __is_valid_sides(self, *sides):
        if len(sides) == self.sides_count and all(isinstance(x, int) and x > 0 for x  in sides ) :
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides) == True:
            self.__sides = list(new_sides)
        else:
            pass

    def __len__(self):
        return sum(self.__sides)



class Circle(Figure):
    sides_count = 1

    def __init__(self,__color,length):
        super().__init__(__color, length)
        self.__radius = length / (2 * 3.14)

    def get_square(self):
        return 3.14 * (self.__radius ** 2)

class Triangle(Figure):
    sides_count = 3
    def __init__(self,__color,__sides):
        super().__init__(__color, __sides)

    def get_square(self):
        p = sum(self.get_sides()) / 2
        return (p * ((p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2]))) ** 0.5

class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, edge):
        sides = [edge] * self.sides_count
        super().__init__(__color, sides)


    def get_volume(self):
        edge = self.get_sides()[0]
        return edge ** 3

circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)


circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

print(len(circle1))

print(cube1.get_volume())
