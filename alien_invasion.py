import sys

import pygame

from settings import Settings

class AlienInvasion:
	"""General class that runs resorses and the war of runing the game"""
	def __init__(self):
		"""begin the game and create resurses of it"""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")

		# set screen color
		self.bg_color = (230, 230, 230)

	def run_game(self):
		"""start the main sercle of the game"""
		while True:
			# Follw the keybord and mouse
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			#draw the screen again on every circle iteracion
			self.screen.fill(self.settings.bg_color)

			#Show the last drown screen
			pygame.display.flip()

if __name__ == '__main__':
	#create a game and rut it
	ai = AlienInvasion()
	ai.run_game()