import pygame
class Fox:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("phone.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 0.1
        self.is_sped_up = False

    def move_direction(self, direction):
        if direction == "space":
            self.is_sped_up = True
        elif direction == "up_space":
            self.is_sped_up = True
            self.y -= self.delta
        elif direction == "down_space":
            self.is_sped_up = True
            self.y += self.delta
        elif direction == "right":
            self.x += self.delta
        elif direction == "left":
            self.x -= self.delta
        elif direction == "up":
            self.y -= self.delta
        elif direction == "down":
            self.y += self.delta

        if not self.is_sped_up:
            self.delta = 0.2  # set speed back to 0.1 if spacebar is not being held down
            self.image = pygame.image.load("phone.png")
            self.image_size = self.image.get_size()
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        else:
            self.image = pygame.image.load("cloud.thing.jpg")
            self.image_size = self.image.get_size()
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
            self.delta = 0.5  # set speed to 0.2 if spacebar is being held down

        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
