from vector2 import Vector2


class World:
    GRAVITY = Vector2(0, 500)
    SOLVER_ITERATIONS = 4
    CELL_SIZE = 60

    def __init__(self, floor_y, ceiling_y, left_wall_x, right_wall_x):
        self.bodies = []
        self.floor_y = floor_y
        self.left_wall_x = left_wall_x
        self.right_wall_x = right_wall_x
        self.ceiling_y = ceiling_y

    def build_grid(self):
        grid = {}

        for body in self.bodies:
            cell_x = int(body.position.x // self.CELL_SIZE)
            cell_y = int(body.position.y // self.CELL_SIZE)
            cell = (cell_x, cell_y)

            if cell not in grid:
                grid[cell] = []
            
            grid[cell].append(body)

        return grid

    def resolve_ball_collisions_grid(self):
        grid = self.build_grid()

        # debug print
        # for cell, bodies_in_cell in grid.items():
        #     if len(bodies_in_cell) > 1:
        #         print(f"Cell {cell} has {len(bodies_in_cell)} balls")

        checked_pairs = set()

        for body in self.bodies:
            cell_x = int(body.position.x // self.CELL_SIZE)
            cell_y = int(body.position.y // self.CELL_SIZE)

            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    neighbour_cell = (cell_x + dx, cell_y + dy)

                    if neighbour_cell not in grid:
                        continue

                    for other in grid[neighbour_cell]:
                        if other is body:
                            continue
                        
                        pair = (id(body), id(other))
                        pair_sorted = tuple(sorted(pair))

                        if pair_sorted in checked_pairs:
                            continue
                        
                        checked_pairs.add(pair_sorted)

                        self.resolve_ball_collision(body, other)

    def add_body(self, body):
        self.bodies.append(body)

    def step(self, dt):
        for body in self.bodies:
            gravity_force = self.GRAVITY * body.mass
            body.apply_force(gravity_force)

            body.update(dt)

            self.resolve_floor_collision(body)
            self.resolve_ceiling_collision(body)
            self.resolve_left_wall_collision(body)
            self.resolve_right_wall_collision(body)

        for i in range(self.SOLVER_ITERATIONS):
            self.resolve_ball_collisions_grid()


    def resolve_floor_collision(self, body):
        bottom_of_ball = body.position.y + body.radius

        if bottom_of_ball >= self.floor_y:
            body.position.y = self.floor_y - body.radius

            body.velocity.y = -body.velocity.y * 0.7

    def resolve_left_wall_collision(self, body):
        left_of_ball = body.position.x - body.radius

        if left_of_ball <= self.left_wall_x:
            body.position.x = self.left_wall_x + body.radius

            body.velocity.x = -body.velocity.x * 0.7
    
    def resolve_right_wall_collision(self, body):
        right_of_ball = body.position.x + body.radius

        if right_of_ball >= self.right_wall_x:
            body.position.x = self.right_wall_x - body.radius

            body.velocity.x = -body.velocity.x * 0.7

    def resolve_ceiling_collision(self, body):
        top_of_ball = body.position.y - body.radius

        if top_of_ball <= self.ceiling_y:
            body.position.y = self.ceiling_y + body.radius

            body.velocity.y = -body.velocity.y * 0.7

    def resolve_ball_collision(self, a, b):
        direction = b.position - a.position
        distance_squared = direction.length_squared()
        radius_sum = a.radius + b.radius

        if distance_squared < radius_sum ** 2:
            distance = direction.length()

            if distance == 0:
                normal = Vector2(1, 0)
            else:
                normal = direction.normalised()

            overlap = radius_sum - distance
            a.position = a.position - normal * (overlap / 2)
            b.position = b.position + normal * (overlap / 2)

            relative_velocity = b.velocity - a.velocity
            velocity_along_normal = relative_velocity.dot(normal)

            if velocity_along_normal > 0:
                return

            restitution = 0.7

            impulse_magnitude = -(1 + restitution) * velocity_along_normal
            impulse_magnitude /= (1 / a.mass) + (1 / b.mass)

            impulse = normal * impulse_magnitude

            a.velocity = a.velocity - impulse / a.mass
            b.velocity = b.velocity + impulse / b.mass
