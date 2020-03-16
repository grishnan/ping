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

class Ball(GameObject):
    ''' Класс мяча '''
    def __init__(self, img, initpos, speed):
        super().__init__(img, initpos, speed)
    
    def logic(self):
        ''' логика отскока мяча от платформы '''
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]

class Sled(GameObject):
    ''' Класс платформы '''
    def __init__(self, img, initpos, speed):
        super().__init__(img, initpos, speed)
