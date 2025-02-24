import pygame
import random

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 400, 600
BIRD_X, BIRD_Y = 50, 300
GRAVITY = 0.5
JUMP_STRENGTH = -8
PIPE_WIDTH = 70
PIPE_GAP = 200
PIPE_SPEED = 3

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load assets
bird = pygame.Rect(BIRD_X, BIRD_Y, 30, 30)
clock = pygame.time.Clock()

# Pipe list
pipes = []
def create_pipe():
    y_pos = random.randint(150, HEIGHT - 150)
    pipes.append(pygame.Rect(WIDTH, y_pos, PIPE_WIDTH, HEIGHT))  # Bottom pipe
    pipes.append(pygame.Rect(WIDTH, y_pos - PIPE_GAP - HEIGHT, PIPE_WIDTH, HEIGHT))  # Top pipe

def move_pipes():
    for pipe in pipes:
        pipe.x -= PIPE_SPEED
    if pipes and pipes[0].x < -PIPE_WIDTH:
        pipes.pop(0)
        pipes.pop(0)

def check_collision():
    if bird.y > HEIGHT or bird.y < 0:
        return True
    for pipe in pipes:
        if bird.colliderect(pipe):
            return True
    return False

def draw():
    screen.fill(BLUE)
    pygame.draw.rect(screen, WHITE, bird)
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe)
    pygame.display.update()

def main():
    global bird, velocity, pipes
    velocity = 0
    pipes = []
    running = True
    
    while running:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                velocity = JUMP_STRENGTH

        # Bird mechanics
        velocity += GRAVITY
        bird.y += velocity

        # Pipe mechanics
        if len(pipes) == 0 or pipes[-1].x < WIDTH - 150:
            create_pipe()
        move_pipes()

        # Collision check
        if check_collision():
            running = False

        # Drawing elements
        draw()
    
    pygame.quit()

if __name__ == "__main__":
    main()
