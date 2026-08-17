from vector2 import Vector2


class RigidBody:
    def __init__(self, position, mass=1.0, radius=20.0):
        self.position = position
        self.velocity = Vector2(0, 0)
        self.mass = mass
        self.radius = radius

        self.force_accumulator = Vector2(0, 0)

    def apply_force(self, force):
        self.force_accumulator = self.force_accumulator + force

    def update(self, dt):
        acceleration = self.force_accumulator / self.mass

        self.velocity = self.velocity + acceleration * dt
        self.position = self.position + self.velocity * dt

        self.force_accumulator = Vector2(0, 0)