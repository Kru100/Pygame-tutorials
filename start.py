import pygame as pg

pg.init()
screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()
run = True
dt = 0

pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            
    screen.fill('purple')
    
    pg.draw.circle(screen, 'red', pos, 40)
    
    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        pos.y -= 300 * dt
    if keys[pg.K_s]:
        pos.y += 300 * dt
    if keys[pg.K_a]:
        pos.x -= 300 * dt
    if keys[pg.K_d]:
        pos.x += 300 * dt
        
    pg.display.flip()
    
    dt = clock.tick(60) / 1000

pg.quit()
