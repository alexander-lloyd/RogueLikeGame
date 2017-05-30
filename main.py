from library.game import Game
from library.states import SplashScreen

g = Game()
state = SplashScreen()
g.add_state(state)
g.set_current_state(state)
g.run()
