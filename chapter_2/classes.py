import math

class Point:
    pass

class Point2:
    def reset(self):
        self.x = 0
        self.y = 0

class Point3:
    def move(self,x,y):
        self.x = x
        self.y = y

    def reset(self):
        self.x = 0
        self.y = 0

    def calculate_distance(self, other_point):
        return math.sqrt(
            (self.x - other_point.x)**2 +
            (self.y - other_point.y) ** 2
        )
