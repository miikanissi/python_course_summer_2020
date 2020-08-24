
#!/usr/bin/env python3
#
# Assignment Pygame "Tux Jump"
#
# Week 11-12, pygame, Miika Nissi
#
# Player character Tux from https://opengameart.org/content/tux-the-linux-mascot
# CC-BY-SA 3.0 License
#
# Platforms from https://opengameart.org/content/physics-blocks-set
# CC0 License
#
# Background from https://opengameart.org/content/seamless-snow-texture
# CC-BY 3.0 License
#
# Game Licensed as GNU GENERAL PUBLIC LICENSE V3.0
#
# CONTROLS:
# Left & Right arrow keys or "a" & "d"
import os
import pygame
from pygame.locals import *
import time, random

# Paths
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, 'images')

""" 
Setup
"""

# Frames per second
FPS = 60
fps = pygame.time.Clock()

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Different variables for program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Player properties
PLAYER_ACC = 1
PLAYER_FRICTION = -0.2
PLAYER_GRAV = 0.7
PLAYER_JUMP = 20

# Starting platforms
PLATFORM_LIST = [(SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT * 3 / 4, 100, 20),
                 (125, SCREEN_HEIGHT - 350, 100, 20),
                 (250, 200, 100, 20),
                 (175, 100, 50, 20)]

# Title and font
TITLE = "Tux Jump"
FONT_NAME = "Liberation Sans"

# Background
BACKGROUND = pygame.image.load(os.path.join(image_path, "snow.png"))

vec = pygame.math.Vector2
"""
Player
"""
class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load(os.path.join(image_path, "tux_from_linux.png"))
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.surface = pygame.Surface((40, 60))
        self.rect = self.surface.get_rect(center = (SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2))
        self.pos = vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def jump(self):
        # Only jumps if touching a platform
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        if hits:
            self.vel.y = -PLAYER_JUMP
        
    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_LEFT] or pressed_keys[ord("a")]:
            self.acc.x = -PLAYER_ACC
        if pressed_keys[pygame.K_RIGHT] or pressed_keys[ord("d")]:
            self.acc.x = PLAYER_ACC

        # Applies friction and calculates motion
        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # Character wraps around the screen
        if self.pos.x > SCREEN_WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = SCREEN_WIDTH

        self.rect.midbottom = self.pos
"""
Platform
"""
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        if w > 70:
            image = "ice_platform_long.png"
        elif w <= 70 and w > 50:
            image = "ice_platform_medium.png"
        else:
            image = "ice_platform_small.png"
            
        self.image = pygame.image.load(os.path.join(image_path, image))
        self.image = pygame.transform.scale(self.image, (w, h))
        self.surface = pygame.Surface((w, h))
        self.rect = self.surface.get_rect()
        self.rect.x = x
        self.rect.y = y

"""
Game
"""
class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.font_name = pygame.font.match_font(FONT_NAME)
        self.platform_count = 7
        self.screen.blit(BACKGROUND, (0,0))

    def new(self):
        self.score = 0
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for platform in PLATFORM_LIST:
            p = Platform(*platform)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            
    def update(self):
        self.all_sprites.update()

        # Check if player hits platform when falling
        if self.player.vel.y > 0:
            hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
                self.player.jump()

        # Move screen as player hits top of the screen
        if self.player.rect.top <= SCREEN_HEIGHT / 4:
            self.player.pos.y += abs(self.player.vel.y)
            for platform in self.platforms:
                platform.rect.y += abs(self.player.vel.y)
                if platform.rect.top >= SCREEN_HEIGHT:
                    platform.kill()
                    self.score += 1

        # If player falls
        if self.player.rect.bottom > SCREEN_HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()
        if len(self.platforms) == 0:
            self.playing = False
            
        # Generate new platforms when old is killed
        while len(self.platforms) < self.platform_count:
            width = random.randint(40,100)
            p = Platform(random.randint(0, SCREEN_WIDTH - width),
                         random.randint(-75, -30),
                         width, 20)
            self.platforms.add(p)
            self.all_sprites.add(p)
        
                
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        self.screen.blit(BACKGROUND, (0,0))
        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score), 20, BLACK, SCREEN_WIDTH / 8, 15)
        pygame.display.flip()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

game = Game()
game.show_start_screen()
while game.running:
    game.new()
    game.show_go_screen()

pygame.quit()

