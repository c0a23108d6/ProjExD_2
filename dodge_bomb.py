import os
import random
import sys
import pygame as pg
import time


WIDTH, HEIGHT = 1400, 750
DELTA = {  # 移動量辞書
    pg.K_UP:(0, -5),
    pg.K_DOWN: (0, 5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (5, 0)
}
"""KAITEN = {  # 演習１
    (-5, -5): pg.transform.rotozoom(pg.image.load("fig/3.png"), 45, 2.0),
    (-5, 0): pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 2.0),
    (-5, 5): pg.transform.rotozoom(pg.image.load("fig/3.png"), 315, 2.0),
    (0, 5): pg.transform.rotozoom(pg.image.load("fig/3.png"), 270, 2.0),
    (5, 5): pg.transform.rotozoom(pg.image.load("fig/3.png"), 225, 2.0),
    (5, 0): pg.transform.rotozoom(pg.image.load("fig/3.png"), 180, 2.0),
    (5, -5): pg.transform.rotozoom(pg.image.load("fig/3.png"), 135, 2.0),
    (0, -5): pg.transform.rotozoom(pg.image.load("fig/3.png"), 90, 2.0),
}"""
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def check_bound(rct: pg.Rect) -> tuple[bool, bool]:
    """
    引数:こうかとんRectまたは爆弾Rect
    戻り値:横方向・縦方向の真理値タプル
    (True:画面内/False:画面外）
    """
    yoko, tate = True, True
    if rct.left < 0 or WIDTH < rct.right:
        yoko = False
    if rct.top < 0 or HEIGHT < rct.bottom:
        tate = False
    return yoko, tate


"""def kaiten():  #演習１
    for k, v in KAITEN.items():
        if KAITEN[3]:
            pg.transform.flip(pg.image.load("fig/3.png"), True, False)
        if sum_mv == 
        """

            
def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 2.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400
    bb_img = pg.Surface((20,20))  # 1辺が20の空のsurfaceを作る
    bb_img.set_colorkey((0,0,0))
    pg.draw.circle(bb_img, (255,0,0), (10,10), 10)  # 空のsurfaceに赤い円を描く
    bb_rct = bb_img.get_rect()
    bb_rct.center = random.randint(0, WIDTH), random.randint(0, HEIGHT)
    vx, vy = 5, -5
    clock = pg.time.Clock()
    tmr = 0

    go_img = pg.Surface((WIDTH, HEIGHT))
    pg.draw.rect(go_img, (0,0,0), (0, 0, WIDTH, HEIGHT))
    go_img.set_alpha(128)
    go_rct = go_img.get_rect()
    fonto = pg.font.Font(None, 80)
    txt = fonto.render("Game Over", True, (255, 255, 255))
    sad_kk = pg.image.load("fig/8.png")
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        if kk_rct.colliderect(bb_rct):
            screen.blit(go_img, go_rct)
            screen.blit(txt, [WIDTH/2, HEIGHT/2])
            screen.blit(sad_kk, [WIDTH/2, HEIGHT/2+200])
            screen.blit(sad_kk, [WIDTH/2, HEIGHT/2-200])
            time.sleep(5)
            return
        screen.blit(bg_img, [0, 0]) 
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for k, v in DELTA.items():
            if key_lst[k]:
                sum_mv[0] += v[0]
                sum_mv[1] += v[1]
        kk_rct.move_ip(sum_mv)
        if check_bound(kk_rct) != (True, True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])
        screen.blit(bb_img, bb_rct)
        bb_rct.move_ip(vx, vy)
        yoko, tate = check_bound(bb_rct)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1
        screen.blit(kk_img, kk_rct)

        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
