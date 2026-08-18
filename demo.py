import random
import pygame
from vector2 import Vector2
from rigid_body import RigidBody
from world import World

dragged_ball = None

balls = []

WIDTH, HEIGHT = 1500, 800

pygame.init()
font = pygame.font.SysFont(None, 24)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

world = World(floor_y=HEIGHT, ceiling_y=0, left_wall_x=0, right_wall_x=WIDTH)

for i in range(3):
    ball = RigidBody(position=Vector2(random.randint(25, WIDTH - 25), random.randint(100, 300)), mass=1.0, radius=25)
    balls.append(ball)
    world.add_body(ball)

running = True
while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            click_position = Vector2(mouse_x, mouse_y)

            for ball in balls:
                direction = click_position - ball.position
                distance_squared = direction.length_squared()

                if distance_squared < ball.radius ** 2:
                    dragged_ball = ball
    
        if event.type == pygame.MOUSEBUTTONUP:
            dragged_ball = None

    world.step(dt)

    if dragged_ball is not None:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dragged_ball.position = Vector2(mouse_x, mouse_y)

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