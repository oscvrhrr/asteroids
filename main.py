import pygame
from constants import *

def main():
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  pygame.init()
  
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  while screen:
    for event in pygame.event.get():
      screen.fill(color="black")
    if event.type == pygame.QUIT:
        return
    

  pygame.display.flip()

if __name__ == "__main__":
  main()