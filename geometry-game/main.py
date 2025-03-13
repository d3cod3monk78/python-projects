from random import randint
from point import Point
from rectangle import Rectangle

if __name__ == '__main__':
    rectangle = Rectangle(Point(randint(0, 9), randint(0, 9)), Point(randint(10, 19), randint(10, 19)))
    print(f"Rectangle low_left Coordinates-> rectangle low_left_x: {rectangle.low_left.x}, low_left_y: {rectangle.low_left.y}")
    print(f"Rectangle up_right Coordinates-> rectangle up_right_x: {rectangle.up_right.x}, up_right_y: {rectangle.up_right.y}")

    user_point = Point(float(input("Guess X in point: ")), float(input("Guess Y in point: ")))
    print(user_point.falls_in_rectangle(rectangle))


