import pygame as pg
import sys
WIDTH=500; HEIGHT=500
pg.init()
screen=pg.display.set_mode((WIDTH, HEIGHT))

text_1= "pie:         $2.50"
text_2="half-sandwich: $4.50"

price = 0
font = pg.font.Font('freesansbold.ttf',20)

#text surfaces for menu items
text_surface_1 = font.render(text_1, True, (55, 2, 222), (0,0,0))
text_surface_2 = font.render(text_2, True, (55, 199, 22), (0,0,0))

#text rects for menu text surfaces
text_rect_1 = text_surface_1.get_rect(center = (100, 100))
text_rect_2 = text_surface_2.get_rect(center = (100, 130))

while True:
    collision1 = pg.Rect.collidepoint(text_rect_1, pg.mouse.get_pos())
    collision2 = pg.Rect.collidepoint(text_rect_2, pg.mouse.get_pos())
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            if collision1: price += 2.5
            elif collision2: price += 4.50

    #draw
    price_sum_surface=font.render(str(price), True, (255, 100, 100))
    price_sum_surface_rect = price_sum_surface.get_rect(center = (WIDTH - 50, 100))
    screen.fill((100,100,199), price_sum_surface.get_rect(center = (WIDTH - 50, 100)))

    screen.blit(text_surface_1, text_rect_1)
    screen.blit(text_surface_2, text_rect_2)
    screen.blit(price_sum_surface, price_sum_surface.get_rect(center = (WIDTH - 50, 100)))

    pg.display.flip()