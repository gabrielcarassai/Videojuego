import os
import sys
import pygame

def main(args=None):
    if args is None:
        args = sys.argv[1:]
        
    
    hero_image_filename = ["shmup", "assets", "images", "hero.png"]
    pygame.init() # constructor

    # Set up the drawing window
    screen = pygame.display.set_mode([800, 500], 0, 32)
    pygame.display.set_caption("Caza Jet - La última misión")

    # Load hero image
    hero_image = pygame.image.load(os.path.abspath(os.path.join(*hero_image_filename))).convert_alpha()

    # Run until the user asks to quit
    running = True
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #get user mouse position en juegos el 0,0 está arriba a la izquierda 
        x, y = pygame.mouse.get_pos()
        x -= hero_image.get_width() / 2
        y -= hero_image.get_height() / 2
        screen.fill((0, 60, 90))

        screen.blit(hero_image, (x, y))
        
        # Flip the display
        pygame.display.update()

    pygame.quit() # destructor libera memoria

if __name__ == "__main__":
    sys.exit(main())