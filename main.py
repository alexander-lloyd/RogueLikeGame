from library.game import Game
from library import GameScreen, SplashScreen

g = Game()
loading_state = SplashScreen()
game_state = GameScreen()
g.add_state('loading', loading_state)
g.add_state('game', game_state)
g.set_current_state('loading')
g.run()
