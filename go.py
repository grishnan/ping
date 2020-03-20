"""
Описание классов игровых объектов: мяча, платформы
"""

import pygame as pg
from consts import *

class GameObject(pg.sprite.Sprite):
    ''' Базовый игровой объект '''
    def __init__(self, img, initpos, speed):
        super().__init__()                            # инициализация родительского класса
        self.img = pg.image.load(img).convert_alpha() # загрузка изображения
        self.rect = self.img.get_rect()               # снимаем прямоугольник с изображения
        self.rect.move_ip(initpos)                    # помещаем прямоугольник в указанное место
        self.mask = pg.mask.from_surface(self.img)    # снимаем маску с изображения
        self.speed = speed                            # скорость игрового объекта
    
    def move(self):
        ''' перемещение игровых объектов '''
        self.rect = self.rect.move(self.speed)
    
    def draw(self, screen):
        ''' отрисовка игровых объектов '''
        screen.blit(self.img, self.rect)

class Ball(GameObject):
    ''' Класс мяча '''
    def __init__(self, img, initpos, speed):
        super().__init__(img, initpos, speed)
    
    def logic(self):
        ''' логика отскока мяча от стен '''
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]

class Sled(GameObject):
    ''' Класс платформы '''
    def __init__(self, img, initpos, speed):
        super().__init__(img, initpos, speed)
    
    def logic(self):
        ''' логика перемещения платформы '''
        pressed = pg.key.get_pressed() # вернем все зажатые клавиши
        if pressed[pg.K_UP]:
            self.speed[1] = -2 if self.rect.top >= 0 else 0
        elif pressed[pg.K_DOWN]:
            self.speed[1] = 2 if self.rect.bottom <= height else 0
        else: self.speed[1] = 0

    def collide(self, gballs):
        ''' столкновение платформы с мячиками '''
        collided_balls = pg.sprite.spritecollide(self, gballs, True, pg.sprite.collide_mask)
        for ball in collided_balls:
            ball.rect.left += 3 # TODO
            ball.speed[0] = -ball.speed[0]
