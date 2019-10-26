#!/usr/bin/env python3

import pygame as pg
from pygame.locals import *
from go import Ball # игровые объекты

pg.init()

FPS  = 60
SIZE = width, height = 640, 480
speedsled = [0, 0]
BGCOLOR = 90, 90, 90

screen = pg.display.set_mode(SIZE)         # создаём окошко
clock  = pg.time.Clock()                   # создаем таймер

sled = pg.image.load("sled.png").convert() # загрузка изображения платформы
sledrect = sled.get_rect()                 # снимаем прямоугольник для платформы
sledrect.move_ip((20, 0))                  # поместить прямоугольник платформы в указанное место
sledmask = pg.mask.from_surface(sled)      # снимаем маску с платформы

ball = Ball("ball.png", (50, 20), [4, 4])  # создаём мяч

again = True
while again:
    for event in pg.event.get():
        if event.type == pg.QUIT: again = False
    
    # логика перемещения платформы
    pressed = pg.key.get_pressed() # вернем все зажатые клавиши
    if pressed[pg.K_UP]:
        speedsled[1] = -2 if sledrect.top >= 0 else 0
    elif pressed[pg.K_DOWN]:
        speedsled[1] = 2 if sledrect.bottom <= height else 0
    else: speedsled[1] = 0

    # логика столкновения мяча с платформой
    if sledrect.colliderect(ball.rect):
        ball.speed[0] = -ball.speed[0]

    # логика отскока мяча от границ экрана
    if ball.rect.left < 0 or ball.rect.right > width:
        ball.speed[0] = -ball.speed[0]
    if ball.rect.top < 0 or ball.rect.bottom > height:
        ball.speed[1] = -ball.speed[1]
        
    sledrect = sledrect.move(speedsled)    # сдвинуть прямоугольник платформы
    ball.rect = ball.rect.move(ball.speed) # сдвинуть прямоугольник мяча

    # отрисовка изображений
    screen.fill(BGCOLOR)
    screen.blit(sled, sledrect)
    screen.blit(ball.img, ball.rect)

    pg.display.update()
    clock.tick(FPS)

# выход из программы
pg.quit()
