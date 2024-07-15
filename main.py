import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Plants VS Zombies"

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height,title)
        self.setup()

    def setup(self):
        pass

    def on_draw(self):
        pass

    def update(self, delta_time):
        pass

    def on_mouse_press(self,x,y,button,modifiers):
        pass

    def on_mouse_motion(self,x,y,dx,dy):
        pass

window = Game(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
arcade.run()