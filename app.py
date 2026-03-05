import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLUE = (135, 206, 235)

# Bird
bird_x = 80
bird_y = 300
bird_radius = 15
bird_velocity = 0
gravity = 0.5
jump_strength = -8

# Pipes
pipe_width = 60
pipe_gap = 150
pipe_speed = 3
pipes = []

def create_pipe():
    height = random.randint(100, 400)
    pipes.append({"x": WIDTH, "height": height})

def draw_pipes():
    for pipe in pipes:
        # top pipe
        pygame.draw.rect(screen, GREEN, (pipe["x"], 0, pipe_width, pipe["height"]))
        # bottom pipe
        pygame.draw.rect(
            screen,
            GREEN,
            (pipe["x"], pipe["height"] + pipe_gap, pipe_width, HEIGHT),
        )

def move_pipes():
    for pipe in pipes:
        pipe["x"] -= pipe_speed

def check_collision():
    global bird_y

    if bird_y > HEIGHT or bird_y < 0:
        return True

    for pipe in pipes:
        if bird_x + bird_radius > pipe["x"] and bird_x - bird_radius < pipe["x"] + pipe_width:
            if bird_y - bird_radius < pipe["height"] or bird_y + bird_radius > pipe["height"] + pipe_gap:
                return True

    return False


pipe_timer = 0

# Game loop
while True:
    screen.fill(BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = jump_strength

    # Bird physics
    bird_velocity += gravity
    bird_y += bird_velocity

    # Pipe logic
    pipe_timer += 1
    if pipe_timer > 90:
        create_pipe()
        pipe_timer = 0

    move_pipes()

    # Draw bird
    pygame.draw.circle(screen, WHITE, (bird_x, int(bird_y)), bird_radius)

    # Draw pipes
    draw_pipes()

    # Collision
    if check_collision():
        print("Game Over")
        pygame.quit()
        sys.exit()

    pygame.display.update()
    clock.tick(60)
