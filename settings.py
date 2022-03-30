import pygame

WINSIZE = W, H = (1080, 720)
FPS = 60

# Menu
# Color
BG_MENU_COLOR = (51,51,102)
TITLE_MENU_COLOR = (255,255,255)
BTN_COLOR_DEFAULT = (255,255,255)
BTN_COLOR_HOVER = (255,215,0)

# Pos
TITLE_POS = (W/2, H/2 - 150)
START_BTN_POS = (W/2, H/2)
HIGHSCORES_BTN_POS = (W/2, H/2 + 100)

# Func
def scale(surf: pygame.Surface, ratio: float):
	size = surf.get_size()
	new_surf = pygame.transform.scale(surf, (size[0] * ratio, size[1] * ratio))

	return new_surf
