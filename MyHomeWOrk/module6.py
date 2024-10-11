import math


class Figure:
    def __init__(self, color, *sides, sides_count=0):
        self.sides_count = sides_count
        if isinstance(self, Cube) and len(sides)==1:
            self.__sides = list(sides)*sides_count
        elif len(sides) == sides_count:
            self.__sides = list(sides)
        else:
            self.__sides = [1] * sides_count
        self.__color = color
        self.filed = bool()

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        return False

    def set_color(self, *rgb):
        if self.__is_valid_color(*rgb):
            self.__color = tuple(rgb)


    def __is_valid_sides(self, *sides):
        pos_sides = [isinstance(i, int) and i > 0 for i in sides]
        if len(sides) == self.sides_count and all(pos_sides):
            return True
        return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = new_sides

class Circle(Figure):
    def __init__(self, color, *sides, sides_count=1):
        super().__init__(color, *sides, sides_count=sides_count)
        self.__radius = self.__len__() / (2 * math.pi) # 2 pi r = P

    def get_square(self):
        return math.pi * self.__radius**2

class Triangle(Figure):
    def __init__(self, color, *sides, sides_count=3):
        super().__init__(color, *sides, sides_count=sides_count)

    def get_square(self):
        half_per = self.__len__() / 2
        square = math.sqrt(half_per*(half_per-self.get_sides()[0])*(half_per-self.get_sides()[1])*(half_per-self.get_sides()[2]))

class Cube(Figure):
    def __init__(self, color, *sides, sides_count=12):
        super().__init__(color, *sides, sides_count=sides_count)

    def get_volume(self):
        return self.get_sides()[0]**3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

print(len(circle1))

print(cube1.get_volume())
