import pygame
import random
from pygame.locals import *
pygame.init()

WIDTH = 864
HEIGHT = 936

clock = pygame.time.Clock()
fps = 60
# title_font = pygame.font.SysFont("helvicta", 14)
ground_x = 0
scroll_speed = 4
running = True
game_over = False
flying = True

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird") 

bg = pygame.image.load("./images/bg.png")
ground = pygame.image.load("./images/ground.png")

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        
        for i in range(1,4):
            bird = pygame.image.load(f"./images/bird{i}.png")
            self.images.append(bird)
        
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.velocity = 0    
        self.clicked = False
        
    def update(self):
        if flying == True:
            # Gravity
            self.velocity += 0.5
            if self.velocity > 8:
                self.velocity = 8
            
            if self.rect.bottom < 768:
                self.rect.y += int(self.velocity)
            
        if game_over == False:
            # Clicking effect
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.velocity = -10
            
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        self.counter += 1
        flap_cooldown = 2
        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        
        self.image = self.images[self.index]
        
        

   
bird_group = pygame.sprite.Group()
bird1 = Bird(int(WIDTH/4), int(HEIGHT/2))     
bird_group.add(bird1)
        
while running:
    clock.tick(fps)

    screen.blit(bg, (0,0))
    
    bird_group.draw(screen)
    bird_group.update()
    
    # drawing and scrolling the ground
    screen.blit(ground, (ground_x, 768))
    ground_x -= scroll_speed
    if abs(ground_x) > 35:
        ground_x = 0
        
    
        
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()