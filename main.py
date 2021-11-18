
class Point:
    "Класс для представления аттрибутов точек на плоскости"
    color = 'red'
    sphere = 5

    def setCoord():
        print('Вызов метода setCoords')

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

a = Point()
b = Point()