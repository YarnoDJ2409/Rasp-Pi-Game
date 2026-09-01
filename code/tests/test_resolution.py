import pygame
import sys

pygame.init()

# Change these to test different resolutions
WIDTH, HEIGHT = 800, 480
flags = pygame.FULLSCREEN #Fullscreen display

screen = pygame.display.set_mode((WIDTH, HEIGHT), flags)
pygame.display.set_caption("Resolution Test")

clock = pygame.time.Clock()

# Colors for the four corners
RED    = (255, 0, 0)
GREEN  = (0, 255, 0)
BLUE   = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK  = (0, 0, 0)

CORNER_SIZE = 10   # size of the colored squares

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill(BLACK)

    # Top-left
    pygame.draw.rect(screen, RED,    (0, 0, CORNER_SIZE, CORNER_SIZE))
    # Top-right
    pygame.draw.rect(screen, GREEN,  (WIDTH - CORNER_SIZE, 0, CORNER_SIZE, CORNER_SIZE))
    # Bottom-left
    pygame.draw.rect(screen, BLUE,   (0, HEIGHT - CORNER_SIZE, CORNER_SIZE, CORNER_SIZE))
    # Bottom-right
    pygame.draw.rect(screen, YELLOW, (WIDTH - CORNER_SIZE, HEIGHT - CORNER_SIZE, CORNER_SIZE, CORNER_SIZE))

    # Show the current resolution in the center
    font = pygame.font.SysFont(None, 48)
    text = font.render(f"{WIDTH} x {HEIGHT}", True, (255, 255, 255))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()