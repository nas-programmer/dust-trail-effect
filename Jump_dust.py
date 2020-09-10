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
            if i.rad <= 0:
                self.particles.remove(i)

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


























































































































































# import pygame, sys

# # Global constants

# # Colors
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
# BLUE = (0, 0, 255)

# # Screen dimensions
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600

# class Player(pygame.sprite.Sprite):
#     """ This class represents the bar at the bottom that the player
#         controls. """
 
#     # -- Methods
#     def __init__(self):
#         """ Constructor function """
 
#         # Call the parent's constructor
#         super().__init__()
 
#         # Create an image of the block, and fill it with a color.
#         # This could also be an image loaded from the disk.
#         width = 40
#         height = 60
#         self.image = pygame.Surface([width, height])
#         self.image.fill(RED)
 
#         # Set a referance to the image rect.
#         self.rect = self.image.get_rect()
 
#         # Set speed vector of player
#         self.change_x = 0
#         self.change_y = 0
 
#         # List of sprites we can bump against
#         self.level = None
 
#     def update(self):
#         """ Move the player. """
#         # Gravity
#         self.calc_grav()
 
#         # Move left/right
#         self.rect.x += self.change_x
 
#         # See if we hit anything
#         block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
#         for block in block_hit_list:
#             # If we are moving right,
#             # set our right side to the left side of the item we hit
#             if self.change_x > 0:
#                 self.rect.right = block.rect.left
#             elif self.change_x < 0:
#                 # Otherwise if we are moving left, do the opposite.
#                 self.rect.left = block.rect.right
 
#         # Move up/down
#         self.rect.y += self.change_y
 
#         # Check and see if we hit anything
#         block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
#         for block in block_hit_list:
 
#             # Reset our position based on the top/bottom of the object.
#             if self.change_y > 0:
#                 self.rect.bottom = block.rect.top
#             elif self.change_y < 0:
#                 self.rect.top = block.rect.bottom
 
#             # Stop our vertical movement
#             self.change_y = 0
 
#     def calc_grav(self):
#         """ Calculate effect of gravity. """
#         if self.change_y == 0:
#             self.change_y = 2
#         else:
#             self.change_y += .25
 
#         # See if we are on the ground.
#         if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
#             self.change_y = 0
#             self.rect.y = SCREEN_HEIGHT - self.rect.height
 
#     def jump(self):
#         """ Called when user hits 'jump' button. """
 
#         # move down a bit and see if there is a platform below us.
#         # Move down 2 pixels because it doesn't work well if we only move down
#         # 1 when working with a platform moving down.
#         self.rect.y += 2
#         platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
#         self.rect.y -= 2
 
#         # If it is ok to jump, set our speed upwards
#         if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
#             self.change_y = -10
 
#     # Player-controlled movement:
#     def go_left(self):
#         """ Called when the user hits the left arrow. """
#         self.change_x = -6
 
#     def go_right(self):
#         """ Called when the user hits the right arrow. """
#         self.change_x = 6
 
#     def stop(self):
#         """ Called when the user lets off the keyboard. """
#         self.change_x = 0
 
# class Platform(pygame.sprite.Sprite):
#     """ Platform the user can jump on """
 
#     def __init__(self, width, height):
#         """ Platform constructor. Assumes constructed with user passing in
#             an array of 5 numbers like what's defined at the top of this
#             code. """
#         super().__init__()
 
#         self.image = pygame.Surface([width, height])
#         self.image.fill(GREEN)
 
#         self.rect = self.image.get_rect()
 
# class Level(object):
#     """ This is a generic super-class used to define a level.
#         Create a child class for each level with level-specific
#         info. """
 
#     def __init__(self, player):
#         """ Constructor. Pass in a handle to player. Needed for when moving platforms
#             collide with the player. """
#         self.platform_list = pygame.sprite.Group()
#         self.enemy_list = pygame.sprite.Group()
#         self.player = player
         
#         # Background image
#         self.background = None
 
#     # Update everythign on this level
#     def update(self):
#         """ Update everything in this level."""
#         self.platform_list.update()
#         self.enemy_list.update()
 
#     def draw(self, screen):
#         """ Draw everything on this level. """
 
#         # Draw the background
#         screen.fill(BLUE)
 
#         # Draw all the sprite lists that we have
#         self.platform_list.draw(screen)
#         self.enemy_list.draw(screen)
 
# # Create platforms for the level
# class Level_01(Level):
#     """ Definition for level 1. """
 
#     def __init__(self, player):
#         """ Create level 1. """
 
#         # Call the parent constructor
#         Level.__init__(self, player)
 
#         # Array with width, height, x, and y of platform
#         level = [[210, 70, 500, 500],
#                  [210, 70, 200, 400],
#                  [210, 70, 600, 300],
#                  ]
 
#         # Go through the array above and add platforms
#         for platform in level:
#             block = Platform(platform[0], platform[1])
#             block.rect.x = platform[2]
#             block.rect.y = platform[3]
#             block.player = self.player
#             self.platform_list.add(block)
 
# def main():
#     """ Main Program """
#     pygame.init()
 
#     # Set the height and width of the screen
#     size = [SCREEN_WIDTH, SCREEN_HEIGHT]
#     screen = pygame.display.set_mode(size)
 
#     pygame.display.set_caption("Platformer Jumper")
 
#     # Create the player
#     player = Player()
 
#     # Create all the levels
#     level_list = []
#     level_list.append( Level_01(player) )
 
#     # Set the current level
#     current_level_no = 0
#     current_level = level_list[current_level_no]
 
#     active_sprite_list = pygame.sprite.Group()
#     player.level = current_level
 
#     player.rect.x = 340
#     player.rect.y = SCREEN_HEIGHT - player.rect.height
#     active_sprite_list.add(player)
 
#     # Loop until the user clicks the close button.
#     done = False
 
#     # Used to manage how fast the screen updates
#     clock = pygame.time.Clock()
 
#     # -------- Main Program Loop -----------
#     while not done:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 done = True
            
 
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     done = True
#                 if event.key == pygame.K_LEFT:
#                     player.go_left()
#                 if event.key == pygame.K_RIGHT:
#                     player.go_right()
#                 if event.key == pygame.K_UP:
#                     player.jump()
 
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_LEFT and player.change_x < 0:
#                     player.stop()
#                 if event.key == pygame.K_RIGHT and player.change_x > 0:
#                     player.stop()
 
#         # Update the player.
#         active_sprite_list.update()
 
#         # Update items in the level
#         current_level.update()
 
#         # If the player gets near the right side, shift the world left (-x)
#         if player.rect.right > SCREEN_WIDTH:
#             player.rect.right = SCREEN_WIDTH
 
#         # If the player gets near the left side, shift the world right (+x)
#         if player.rect.left < 0:
#             player.rect.left = 0
 
#         # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
#         current_level.draw(screen)
#         active_sprite_list.draw(screen)
 
#         # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
#         # Limit to 60 frames per second
#         clock.tick(120)
 
#         # Go ahead and update the screen with what we've drawn.
#         pygame.display.flip()
 
#     pygame.quit()
#     sys.exit()
 
# if __name__ == "__main__":
#     main()
