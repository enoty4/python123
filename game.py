import arcade as ar
import random as ran

WIDTH = 960
HEIGHT = 640
TITLE = "Fish game"

class Game(ar.View):

    def __init__(self):
        super().__init__()

        self.map = ar.load_tilemap("fbey.tmj", 0.5)

        self.scene = ar.Scene.from_tilemap(self.map)

        self.fish = ar.Sprite("fishTile_100.png")
        self.fish.center_x = 301
        self.fish.center_y = 100
         
        self.mortal = ar.SpriteList()
        for i in range(10):
            s = ar.Sprite("fishTile_096.png", 0.5)
            s.center_x = ran.randint(0, WIDTH)
            s.center_y = ran.randint(HEIGHT, HEIGHT+200)
            s.change_y = ran.randint(1, 3) * -1
            self.mortal.append(s)

 
        self.feeds = ar.SpriteList()
        for i in range(10):
            f = ar.Sprite("fishTile_120.png")
            f.center_x = ran.randint(0, WIDTH)
            f.center_y = ran.randint(HEIGHT, HEIGHT+200)
            f.change_y = ran.randint(1, 3) * -1
            self.feeds.append(f)

            self.score = 0
        
    def on_draw(self):
        self.scene.draw()
        self.fish.draw()
        self.feeds.draw()
        self.mortal.draw()
        ar.draw_text(f"Баллы: {self.score}", 10, 620, ar.color.WHITE, 30)

    def update(self, delta_time: float):
        self.fish.update()
        self.feeds.update()
        self.mortal.update()

        for f in self.feeds:
            if f.center_y < 0:
                game = Game()
                self.window.show_view(game)
            if ar.check_for_collision(self.fish, f):
               self.score += 1
               f.center_x = ran.randint(0, WIDTH)
               f.center_y = ran.randint(HEIGHT, HEIGHT+200)
               f.change_y = f.change_y * 1.05
       
        for s in self.mortal:
             if ar.check_for_collision(self.fish, s):
               s.center_x = ran.randint(0, WIDTH)
               s.center_y = ran.randint(HEIGHT, HEIGHT+200)
               s.change_y = f.change_y * 1.05

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.fish.center_x = x  
        self.fish.center_y = y  

def main():
    window = ar.Window(WIDTH, HEIGHT, TITLE)
    window.set_mouse_visible(False)

    game = Game()
    window.show_view(game)

    ar.run()
main()