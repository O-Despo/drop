import pygame as pg
import sys

pg.init()

WIDTH= 500; HEIGHT= 500
price = 0
state = 0

pg.init()
screen=pg.display.set_mode((WIDTH, HEIGHT))
font = pg.font.Font('freesansbold.ttf',20)

#A list of list of dictionarys each inner list is a scene 
screen_item_list = [
                [{'screen': 0,'text': 'start', 'color': (0, 35, 250)},
                {'screen': 0,'text': 'forward: \'w\'', 'color': (0, 35, 250)},
                {'screen': 0,'text': 'back: \'s\'', 'color': (0, 35, 250)},
                {'screen': 0,'text': 'click item to buy', 'color': (0, 35, 250)}],
                [{'screen': 1,'name': 'half-sandwich', 'price': 4.50, 'color': (55, 199, 22)},
                {'screen': 1,'name': 'pie', 'price': 2.50, 'color': (55, 2, 222)},
                {'screen': 1,'name': 'soda', 'price': 1.52, 'color': (220, 23, 2)},
                {'screen': 1,'name': 'chips', 'price': 1.75, 'color': (0, 35, 250)}],
                [{'screen': 0,'text': 'Thanks for shopping', 'color': (0, 35, 250)}, 
                {'screen': 0,'text': 'Your final cost is shown', 'color': (0, 35, 250)},
                {'screen': 0,'text': 'Have a nice day', 'color': (0, 35, 250)}]
            ]

#goes through each scene and then for each dictionary it makes the render and rect for the text 
for scene_num, scene in enumerate(screen_item_list):
    for distance, text_item in enumerate(scene):
        if scene_num == 1 : text_item['text'] = f'{text_item["name"]}: $ {text_item["price"]}' #adds text:px to each dict
        text_item['surface'] = font.render(text_item['text'], True, text_item['color']) #adds a text surface
        text_item['rect'] = text_item['surface'].get_rect(center = (200, (100 + distance * 40)))#add a rect

while True:
    #this is a list comprehension they are complex but powerfull tools as a note they should not be this long This one only calculates collisions for the menu items 
    collides_and_price = [[pg.Rect.collidepoint(text_item['rect'], pg.mouse.get_pos()), text_item['price']] for text_item in screen_item_list[1] if text_item['screen'] == 1]

    for event in pg.event.get(): #game loop that takes  into account
        if event.type == pg.KEYUP: 
            if event.unicode == 'w': state += 1
            elif event.unicode == 's':state -= 1
        if event.type == pg.QUIT or state > len(screen_item_list) - 1: sys.exit() #quits if at end of scenes
        elif event.type == pg.MOUSEBUTTONDOWN:
            for collide_price in collides_and_price:
                if collide_price[0] and state == 1: price += collide_price[1]

    screen.fill((0,0,0))
    for text_item in screen_item_list[state]:
        screen.blit(text_item['surface'], text_item['rect'])

    price_sum_surface = font.render(f'${price}', True, (255, 100, 100)) #this must be rendered as the values of price is changeing 
    screen.blit(price_sum_surface, price_sum_surface.get_rect(center = (WIDTH - 50, 100)))
    pg.display.flip()