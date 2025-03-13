from point import Point
from rectangle import Rectangle

if __name__ == '__main__':
    point_one = Point(10, 20)
    point_two = Point(30, 40)
    rect_one = Rectangle(low_left=(12, 16), up_right=(17, 19))
    point_one.show_xy()
    print(point_one.falls_in_rectangle(rect_one))
    print(point_one.distance_from_point(point_two))

