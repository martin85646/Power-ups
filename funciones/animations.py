import pygame



class SpriteSheet():
    def __init__(self, image, num_frames, cooldown, width, height):
        self.sheet = image
        self.num_frames = num_frames
        self.cooldown = cooldown
        self.animation_list = []
        self.frame = 0
        self.width = width
        self.height = height

        self.current_time = 0
        self.last_update = 0

    def get_frames(self):
        for i in range(self.num_frames):
            image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            image.blit(self.sheet, (0,0), (self.width * i, 0, self.width, self.height))
            self.animation_list.append(image)

    def animate(self):
        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.last_update >= self.cooldown:
            self.frame += 1
            self.last_update = self.current_time
        if self.frame >= len(self.animation_list):
            self.frame = 0
    
    def screen_blit(self, screen, entity, size):
        resized = pygame.transform.scale(self.animation_list[self.frame], (size, size))
        screen.blit(resized, entity.rect)


'''
current_time = pygame.time.get_ticks()
if current_time - last_update >= animation_cooldown:
    frame += 1
    last_update = current_time
    if frame >= len(animation_list):
        frame = 0
'''
'''
num_frames = 3
animation_list = []
last_update = pygame.time.get_ticks()
animation_cooldown = 100
frame = 0

for i in range(num_frames):
    aa = bug_sprite_sheet.get_frame(i, 32, 32)
    
    animation_list.append(aa)
''' 