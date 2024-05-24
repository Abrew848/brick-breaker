import pygame as pg


def display(screen):
    screen.fill((0,0,0))

    pg.display.flip()

def main():
    pg.init()
    pg.font.init()

    screen = pg.display.set_mode((1280, 720), pg.RESIZABLE)
    pg.display.set_caption("Brick-Breaker")

    clock = pg.time.Clock()
    run = True


    while run:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                run = False
        
        display(screen)

main()
