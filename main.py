import pygame
import random
import sys

pygame.init()

genislik = 500
yukseklik = 600
ekran = pygame.display.set_mode((genislik, yukseklik))
pygame.display.set_caption("Engellerden Kaç - KankaBot 👊")

beyaz = (255, 255, 255)
kirmizi = (200, 0, 0)
mavi = (0, 0, 200)

oyuncu_boyut = 50
oyuncu_x = genislik // 2 - oyuncu_boyut // 2
oyuncu_y = yukseklik - oyuncu_boyut - 10
oyuncu_hiz = 7

engel_boyut = 50
engel_x = random.randint(0, genislik - engel_boyut)
engel_y = -engel_boyut
engel_hiz = 5

clock = pygame.time.Clock()

calisiyor = True
while calisiyor:
    ekran.fill(beyaz)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            calisiyor = False

    tuslar = pygame.key.get_pressed()
    if tuslar[pygame.K_LEFT] and oyuncu_x > 0:
        oyuncu_x -= oyuncu_hiz
    if tuslar[pygame.K_RIGHT] and oyuncu_x < genislik - oyuncu_boyut:
        oyuncu_x += oyuncu_hiz

    engel_y += engel_hiz
    if engel_y > yukseklik:
        engel_y = -engel_boyut
        engel_x = random.randint(0, genislik - engel_boyut)

    pygame.draw.rect(ekran, mavi, (oyuncu_x, oyuncu_y, oyuncu_boyut, oyuncu_boyut))
    pygame.draw.rect(ekran, kirmizi, (engel_x, engel_y, engel_boyut, engel_boyut))

    oyuncu_rect = pygame.Rect(oyuncu_x, oyuncu_y, oyuncu_boyut, oyuncu_boyut)
    engel_rect = pygame.Rect(engel_x, engel_y, engel_boyut, engel_boyut)

    if oyuncu_rect.colliderect(engel_rect):
        print("💀 GAME OVER - KankaBot çarptı!")
        pygame.quit()
        sys.exit()

    pygame.display.update()
    clock.tick(60)



