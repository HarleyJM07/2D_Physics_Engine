import pygame
from vector2 import Vector2
from rigid_body import RigidBody
from world import World

WIDTH, HEIGHT = 800, 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

world = World(floor_y=HEIGHT, ceiling_y=0, left_wall_x=0, right_wall_x=WIDTH)

ball1 = RigidBody(position=Vector2(WIDTH / 2 - 20, 100), mass=1.0, radius=25)
ball2 = RigidBody(position=Vector2(WIDTH / 2 + 20, 300), mass=1.0, radius=25)

world.add_body(ball1)
world.add_body(ball2)

running = True
while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    world.step(dt)

    screen.fill((30, 30, 30))

    pygame.draw.circle(
        screen, (100, 200, 255),
        (int(ball1.position.x), int(ball1.position.y)),
        int(ball1.radius)
    )
    pygame.draw.circle(
        screen, (255, 150, 100),
        (int(ball2.position.x), int(ball2.position.y)),
        int(ball2.radius)
    )

    pygame.display.flip()

pygame.quit()