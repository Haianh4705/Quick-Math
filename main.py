import pygame, time

from pygame.locals import *
from settings import *
from button import Button

class Game:
	def __init__(self):
		pygame.init()
		pygame.font.init()

		self.state = "menu"

		self.win = pygame.display.set_mode(WINSIZE)
		pygame.display.set_caption("Quick Math!")
		pygame.display.set_icon(pygame.image.load('img/number-one.png').convert_alpha())
		self.clock = pygame.time.Clock()

		self.menu_setup()
	
	def menu_setup(self):
		self.title_font = pygame.font.Font('font.ttf', 128)
		self.btn_font = pygame.font.Font('font.ttf', 64)

		self.menu_sprites = pygame.sprite.Group()

		self.start_btn = Button(self.menu_sprites, START_BTN_POS, 'Start', self.btn_font, BTN_COLOR_DEFAULT, BTN_COLOR_HOVER)
		self.highscores_btn = Button(self.menu_sprites, HIGHSCORES_BTN_POS, 'Highscores', self.btn_font, BTN_COLOR_DEFAULT, BTN_COLOR_HOVER)

		self.title_surf = self.title_font.render('Quick Math!', True, TITLE_MENU_COLOR)
		self.title_rect = self.title_surf.get_rect(center = TITLE_POS)
	
	def menu_update(self):
		mouse_pos = pygame.mouse.get_pos()
		mouse_press = pygame.mouse.get_pressed()[0]

		self.menu_sprites.update(mouse_pos)
	
	def menu(self):
		self.menu_update()

		self.win.fill(BG_MENU_COLOR)
		self.menu_sprites.draw(self.win)
		self.win.blit(self.title_surf, self.title_rect)
	
	def run(self):
		prev_time = time.time()
		while True:
			dt = time.time() - prev_time
			prev_time = time.time()

			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					quit()
				if event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						pygame.quit()
						quit()
			
			if self.state == "menu":
				self.menu()
			
			pygame.display.update()
			self.clock.tick(FPS)

if __name__ == "__main__":
	game = Game()
	game.run()
