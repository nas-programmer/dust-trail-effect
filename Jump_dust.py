"""Jump Dust"""
import pygame, sys, random

WIDTH, HEIGHT = 500, 350

pygame.init()

win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Particle:
    def __init__(self, pos):
        self.x, self.y = pos[0], pos[1]
        self.vx, self.vy = random.randint(-2, 2), random.randint(-10, 0)*.1
        self.rad = 5

    def draw(self, win):
        pygame.draw.circle(win, (255, 255, 255), (self.x, self.y), self.rad)
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        if random.randint(0, 100) < 40:
            self.rad -= 1

class Dust:
    def __init__(self, pos):
        self.pos = pos
        self.particles = []
        for i in range(100):
            self.particles.append(Particle(self.pos))

    def update(self):
        for i in self.particles:
            i.update()
            self.particles = [particle for particle in self.particles if particle.rad > 0]

    def draw(self, win):
        for i in self.particles:
            i.draw(win)
        

def move(rect, x, y):
    rect.x += x
    rect.y += y
    if rect.x >= WIDTH:
        rect.x = 0
    if rect.x < -rect.w:
        rect.x = WIDTH
    if x != 0 and rect.y+ rect.h == HEIGHT:
        dust.append(Dust(rect.midbottom))

#Add gravity
def grav(rect, g_force= 6):
    rect.y += g_force
    if rect.y + rect.h >= HEIGHT:
        rect.y = HEIGHT - rect.h
        dust.append(Dust(rect.midbottom))

    

player = pygame.Rect(30, 30, 32, 32)
player_speed = 5
dust = []
x, y = 0,0
while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if pygame.mouse.get_pressed()[0]:
        #         d = Dust(pygame.mouse.get_pos())
        #         dust.append(d)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = -player_speed
            if event.key == pygame.K_RIGHT:
                x = player_speed
            if event.key == pygame.K_UP:
                y = -20
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x = 0
            if event.key == pygame.K_RIGHT:
                x = 0
            if event.key == pygame.K_UP:
                y = 0
            
        
    win.fill((0, 0, 20))
    pygame.draw.rect(win, (255, 154, 110), player)
    
    
    move(player, x= x, y=y)
    
    if player.y + player.h < HEIGHT:
        grav(player)
        
    for i in range(len(dust)):
        if len(dust[i].particles) > 0:
            dust[i].draw(win)
            dust[i].update()
    
    pygame.display.flip()
