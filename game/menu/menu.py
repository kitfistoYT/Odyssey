import pygame
import menu_background
import buttons
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode([1280, 720], pygame.DOUBLEBUF)


def animate(image):
    screen.fill([0, 0, 0])
    screen.blit(image, [0, 0])
    return screen

pygame.mixer.music.load("./sound/menu_background_music.wav")
pygame.mixer.music.set_volume(0.30)
sound = pygame.mixer.Sound("./sound/button_click.wav")

continue_game = buttons.ButtonClass("./pictures/buttons/continue_game.png", [28, 50])
new_game = buttons.ButtonClass("./pictures/buttons/new_game.png", [28, 150])
save_game = buttons.ButtonClass("./pictures/buttons/save.png", [28, 250])
load_game = buttons.ButtonClass("./pictures/buttons/load_game.png", [28, 350])
options = buttons.ButtonClass("./pictures/buttons/options.png", [28, 450])
quit_game = buttons.QuitGame("./pictures/buttons/quit_game.png", [28, 550])

ship1_image = pygame.image.load("./pictures/Ship/ship1.png")
ship2_image = pygame.image.load("./pictures/Ship/ship2.png")
ship3_image = pygame.image.load("./pictures/Ship/ship3.png")
wave_r_image = pygame.image.load("./pictures/Ship/waves_r.png")
wave_l_image = pygame.image.load("./pictures/Ship/waves_l.png")
back_image = pygame.image.load("./pictures/Ship/background.png")
menu_image = pygame.image.load("./pictures/Menu.png")

ship_pic = [ship1_image, ship2_image, ship3_image]
ship_x = 1280
wave_r_x = -200
wave_l_x = 0
oar_counter = 0
t = 0

ship = menu_background.Ship(ship_pic, [1280, 30], [-5, 0], 10, t, oar_counter)
wave_r = menu_background.Waves(wave_r_image, [wave_r_x, 512], [2, 0], -1164, 0, "r")
wave_l = menu_background.Waves(wave_l_image, [wave_l_x, 412], [-2, 0], 0, -1164, "l")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # hintergrund funktionen
    ship.pos, menu_background.oar_counter, menu_background.t, ship_pic = ship.move()
    wave_r.pos = wave_r.move()
    wave_l.pos = wave_l.move()
    animate(back_image)
    wave_l.draw()
    ship.draw()
    wave_r.draw()

    # musik funktionen
    if pygame.mixer.music.get_busy() == 0:
        pygame.mixer.music.play()

    # menue funktionen
    screen.blit(menu_image, [0, 0])
    continue_game.click()
    new_game.click()
    load_game.click()
    save_game.click()
    options.click()
    quit_game.click()
    pygame.display.flip()

pygame.quit()
