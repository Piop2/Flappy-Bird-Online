import pygame
import win32api
import win32con
import win32gui

pygame.init()
screen = pygame.display.set_mode((400, 400), pygame.NOFRAME)
pygame.display.set_icon(pygame.image.load("resource/icon/flappy29.png"))
clock = pygame.time.Clock()

fuchsia = (255, 0, 128)
# Create layered window
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
# Set window transparency color
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)


def load_image(path: str, scale=4) -> pygame.Surface:
    img = pygame.image.load(path)
    return pygame.transform.scale(img, (img.get_width() * scale, img.get_height() * scale))


bird = load_image(path="resource/image/bird.png")
background = load_image(path="resource/image/background.png")

running = True
while running:
    dt = clock.tick(60)

    screen.fill(fuchsia)

    screen.blit(background, (-92, -488))
    screen.blit(bird, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()
