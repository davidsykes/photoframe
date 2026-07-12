import pygame
from PIL import Image

pygame.init()
screen = pygame.display.set_mode((800, 480))

img = Image.new("RGB", (800, 480), "red")
img.save("test.jpg")

surface = pygame.image.load("test.jpg")
screen.blit(surface, (0, 0))
pygame.display.flip()

input("Press Enter to quit...")