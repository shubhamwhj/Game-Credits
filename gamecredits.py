import pygame, sys

pygame.init()
clock=pygame.time.Clock()

screen = pygame.display.set_mode((400,600))


font1=pygame.font.Font('freesansbold.ttf', 26)
font2=pygame.font.Font('freesansbold.ttf', 18)

y=500
change=1

while True:    
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
      
    
    
    name=font1.render("SPACE INVADERS", False, (255,255,255))
    text=font2.render("Created By: Creator 9",False,(255,255,255))
    
    y=y-change
    screen.blit(name,[95,y]) 
    screen.blit(text,[110,y+50]) 
    if(y<100):
        change=0
    
   
    
    pygame.display.update()
    clock.tick(30)
