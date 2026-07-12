#!/usr/bin/env python3

import pygame
from PIL import Image

print("Python is working")
print(f"Pygame version: {pygame.version.ver}")
print(f"Pillow version: {Image.__version__}")

pygame.init()

screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Pygame Test")

screen.fill((0, 100, 200))
pygame.display.flip()

print("Pygame window created successfully")
print("Close the window to exit")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

print("Finished successfully")