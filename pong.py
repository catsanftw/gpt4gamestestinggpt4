import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the game window
WIDTH, HEIGHT = 800, 600

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the window title
pygame.display.set_caption('Pong')

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the window with a black color
    window.fill((0, 0, 0))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()