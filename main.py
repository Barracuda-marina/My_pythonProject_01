# Описание стандартных библиотек https://docs.python.org/3/library/index.html

class Point:
    "Класс для представления аттрибутов точек в 3d"
    color = 'red'
    sphere = 5

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __del__(self):
        pass

    def set_coord(self, x , y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_coord(self):
        return (self.x, self.y, self.z)

class Coord:
    "Класс для представления координат точек в 3d"
    x = 1
    y = 1
    z = 1

class Human:
    "Класс для описания параметров человека"
    sex = 'male'
    age = 1.0
    date_of_birth = '01/01/1980'
    live = True
    marriage = 'married'
    height = 170.0
    weight = 70.0

if not getattr(Point, 'f', False):
    print("No data")
else:
    print("Data are present")

pt = Point(1, 1, 1)
pt2 = Point(5, 5, 5)
print(pt.__dict__)
print(pt2.__dict__)
