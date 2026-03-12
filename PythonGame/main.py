import pygame
import random

pygame.init()

width = 1000
height = 500
red = (255,0,0)
screen = pygame.display.set_mode((width, height))

bg_img = pygame.image.load("bg.jpg")
aim_pointer = pygame.image.load("aim.png")
zombie_1 = pygame.image.load("zombie_1.png")
zombie_2 = pygame.image.load("zombie_2.png")
zombie_6 = pygame.image.load("zombie_6.png")
zombie_3 = pygame.image.load("zombie_3.png")
zombie_4 = pygame.image.load("zombie_4.png")
zombie_5 = pygame.image.load("zombie_5.png")
Gun_Man  = pygame.image.load("gun_man.png")

ZombieList = [zombie_1, zombie_2, zombie_6, zombie_3, zombie_4, zombie_5]


shotSound = pygame.mixer.Sound("shoot.wav")
reloadSound = pygame.mixer.Sound("reload_sound.mp3")

bgMusic = pygame.mixer.Sound("Advent.mp3")
bgMusic.play()

def score(counter):
    font = pygame.font.SysFont(None, 60 )
    text = font.render("Score : " + str(counter) , True, red)
    screen.blit(text, (10,10))
def game():
    counter = 0
    ZombieImage = random.choice(ZombieList)
    zombie_x = random.randint(0, width - 250)
    zombie_y = random.randint(0, height - 100)
    shot = 6
    while True:
        for event in pygame.event.get():
            # pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                shot -= 1
                if shot >= 0:
                    shotSound.play()
                    if rect_1.colliderect(rect_2):
                        print('Collision Detection...')
                        ZombieImage = random.choice(ZombieList)
                        zombie_x = random.randint(0, width - 250)
                        zombie_y = random.randint(0, height - 100)
                        counter += 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    shot = 6
                    reloadSound.play()

        posx, posy = pygame.mouse.get_pos()

        screen.blit(bg_img, (0, 0))
        screen.blit(ZombieImage, (zombie_x, zombie_y))
        screen.blit(aim_pointer, (posx - 100, posy - 100))
        screen.blit(Gun_Man, (posx, height - 200))
        score(counter)
        rect_1 = pygame.Rect(posx - 100, posy - 100, aim_pointer.get_width(), aim_pointer.get_height())
        rect_2 = pygame.Rect(zombie_x, zombie_y, ZombieImage.get_width(), ZombieImage.get_height())
        pygame.display.update()

game()