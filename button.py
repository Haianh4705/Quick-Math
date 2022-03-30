import pygame

from pygame.locals import *
from settings import *

class Button(pygame.sprite.Sprite):
	def __init__(self, groups, pos, text, font: pygame.font.Font, default_color, hover_color, click_function = None):
		super().__init__(groups)
		self.pos = pos
		self.text = text
		self.font = font
		self.default_color = default_color
		self.hover_color = hover_color
		self.click_function = click_function

		self.image = self.font.render(self.text, True, self.default_color)
		self.rect = self.image.get_rect(center = self.pos)

	def hover(self, mouse_pos):
		if self.rect.collidepoint(mouse_pos):
			self.image = self.font.render(self.text, True, self.hover_color)
			self.rect = self.image.get_rect(center = self.rect.center)
		else:
			self.image = self.font.render(self.text, True, self.default_color)
			self.rect = self.image.get_rect(center = self.rect.center)
	
	def update(self, mouse_pos):
		self.hover(mouse_pos)
