import pygame, sys

chef_image = pygame.image.load("tom-the-chef-pixilart (1).png")
chef_rect = chef_image.get_rect()
chef_rect.centerx = WIDTH//2
chef_rect.ceentery= HEIGHT//2

pygame.init()
clock = pygame.time.Clock()

WIDTH = 600
HEIGHT = 300
display_surface = pygame.display.set_mode((WIDTH,HEIGHT))

chef = chef(50,50,100,100,(255,255,255))

chef_group= pygame.sprite.Group()
chef_group.add(chef)

if __name__ =="__main__":
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



pygame.display.flip()
chef_group.draw(screen)
clock.tick(60)



pygame.quit()