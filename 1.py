#!/usr/bin/env python3

import pygame as pg
from pygame.locals import *
from go import Ball, Sled # игровые объекты
from consts import *
from random import randint as rnd

pg.init()

screen = pg.display.set_mode(SIZE)         # создаём окошко
clock  = pg.time.Clock()                   # создаем таймер

# список мячей
balls = [Ball("ball.png", (rnd(50, 500), rnd(50, 400)), [(-1)**rnd(1, 9)*rnd(1, 9), (-1)**rnd(1, 9)*rnd(1, 9)]) for i in range(0, NUMBALLS)]

sled = Sled("sled.png", (20, 0), [0, 0]) # создаём платформу

gballs = pg.sprite.Group() # группа мячей

again = True
while again:
    for event in pg.event.get():
        if event.type == pg.QUIT: again = False
    
    for ball in balls: ball.add(gballs)  # добавляем мячи в группу
    sled.logic()                         # логика перемещения платформы
    sled.collide(gballs)                 # логика столкновения мяча с платформой
    for ball in balls: ball.logic()      # логика отскока мячей от платформы
    sled.move()                          # пермещение платформы
    for ball in balls: ball.move()       # перемещение мячиков
    
    screen.fill(BGCOLOR)                 # заливка экрана
    sled.draw(screen)                    # отрисовка платформы
    for ball in balls: ball.draw(screen) # отрисовка мячиков

    pg.display.update()
    clock.tick(FPS)

# выход из программы
pg.quit()
