import math


class Vector2:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __truediv__(self, scalar):
        return Vector2(self.x / scalar, self.y / scalar)
    
    def __repr__(self):
        return f"Vector2({self.x:.3f}, {self.y:.3f})"
    
    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def length_squared(self):
        return self.x ** 2 + self.y ** 2

    def normalised(self):
        length = self.length()
        if length == 0:
            return Vector2(0, 0)
        return Vector2(self.x / length, self.y / length)
    
    def dot(self, other):
        return self.x * other.x + self.y + other.y