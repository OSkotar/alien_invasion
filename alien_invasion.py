import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
	"""General class that runs resorses and the war of runing the game"""
	def __init__(self):
		"""begin the game and create resurses of it"""
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")

		self.ship = Ship(self)


	def run_game(self):
		"""start the main cercle of the game"""
		while True:
			self._check_events()
			self._update_screen()

			#Show the last drown screen
			pygame.display.flip()

	def _check_events(self):
		# Follw the keybord and mouse
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

	def _update_screen(self):
		#draw the screen again on every circle iteracion
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()

if __name__ == '__main__':
	#create a game and rut it
	ai = AlienInvasion()
	ai.run_game()