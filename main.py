class Point:
    "Класс для представления координат точек на плоскости"
    color = 'red'
    circle = 2
    x = 1
    y = 1

class Human:
    "Класс для описания человека"
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
