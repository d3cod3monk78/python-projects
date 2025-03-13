from rectangle import Rectangle


class Point:
    """
        Describe about a point in a geometrical view
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show_xy(self):
        print(f"x: {self.x} and y: {self.y}")

    def falls_in_rectangle(self, rectangle):
        if rectangle.low_left.x < self.x < rectangle.up_right.x and rectangle.low_left.y < self.y < rectangle.up_right.y:
            return True
        else:
            return False

    def distance_from_point(self, other_point):
        distance = (self.x - other_point.x)**2 + (self.y - other_point.y)**2
        return distance**0.5
