from library.game import Game
from library.states import GameScreen, PauseState, SplashScreen

g = Game()
loading_state = SplashScreen()
game_state = GameScreen()
pause_state = PauseState()
g.add_state('loading', loading_state)
g.add_state('game', game_state)
g.add_state('pause', pause_state)
g.set_current_state('loading')
g.run()
