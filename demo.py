import random
import pygame
from vector2 import Vector2
from rigid_body import RigidBody
from world import World

balls = []

WIDTH, HEIGHT = 1500, 800

pygame.init()
font = pygame.font.SysFont(None, 24)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

world = World(floor_y=HEIGHT, ceiling_y=0, left_wall_x=0, right_wall_x=WIDTH)

for i in range(20):
    ball = RigidBody(position=Vector2(random.randint(25, WIDTH - 25), random.randint(100, 300)), mass=1.0, radius=25)
    balls.append(ball)
    world.add_body(ball)

running = True
while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    world.step(dt)

    screen.fill((30, 30, 30))

    for ball in balls:
        pygame.draw.circle(
            screen, (100, 200, 255),
            (int(ball.position.x), int(ball.position.y)),
            int(ball.radius)
        )

    fps = int(clock.get_fps())
    fps_text = font.render(f"FPS: {fps}", True, (255, 255, 255))
    screen.blit(fps_text, (10, 10))

    pygame.display.flip()

pygame.quit()