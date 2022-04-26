from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()

class level_1_Class(Entity):
    def __init__(self,**kwargs):
        self.player = PlatformerController2d( scale = (1.0,1.2,.01/2),color = color.white, texture = 'assets/player.png', y = -2 , z = 0.01 )
        super().__init__(parent=self.player)
        window.fullscreen = True


    def environment(self):

        #----------------------------- ground -----------------------------------------------------------------

        self.ground = Entity(model = 'quad' ,texture = 'assets/floor.png', y = -4 , scale_x = 30 , collider = 'box')
        self.ground1 = Entity(model = 'quad' ,texture = 'assets/floor.png', y = -5 , scale_x = 30 , collider = 'box')
        self.ground2 = Entity(model = 'quad' ,texture = 'assets/floor.png', y = -4, x=30 , scale_x = 30 , collider = 'box')
        self.ground3 = Entity(model = 'quad' ,texture = 'assets/floor.png', y = -5 , x=30, scale_x = 30 , collider = 'box')
        self.ground4 = Entity(model = 'quad' ,texture = 'assets/floor.png', y = -4, x=65 , scale_x = 30 , collider = 'box')
        self.ground5 = Entity(model = 'quad' ,texture = 'assets/floor.png', y = -5 , x=65, scale_x = 30 , collider = 'box')

        # ------------------------------ unknown levels --------------------------------------------------------

        self.nxy = [[-1,0],[-5,-1.5],[5,-0.5],[-7,1.3],[3,2]]

        self.nlevels = []
        self.nlevel = Entity(model='quad',texture = 'assets/ublock.png',scale=(1,0.7),position=self.nxy[0],
                       collider = 'box')
        self.nlevels.append(self.nlevel)





        self.nlevels.append(duplicate(self.nlevel, position=self.nxy[1]))
        self.nlevels.append(duplicate(self.nlevel, position=self.nxy[2]))
        self.nlevels.append(duplicate(self.nlevel, position=self.nxy[3]))
        self.nlevels.append(duplicate(self.nlevel, position=self.nxy[4]))

        # ------------------------------ brick levels --------------------------------------------------------

        self.bxy = [[0,0],[-4,-1.5],[4,-0.5],[-6,1.3],[4,2]]

        self.blevels = []
        self.blevel = Entity(model='quad',texture = 'assets/bblock.png',scale=(1,0.7),position=self.bxy[0],
                       collider = 'box')
        self.blevels.append(self.blevel)





        self.blevels.append(duplicate(self.blevel, position=self.bxy[1]))
        self.blevels.append(duplicate(self.blevel, position=self.bxy[2]))
        self.blevels.append(duplicate(self.blevel, position=self.bxy[3]))
        self.blevels.append(duplicate(self.blevel, position=self.bxy[4]))




        #-------------------------------------------------------------------------------------------------------------



        camera.add_script(SmoothFollow(target = self.player , offset = [0,3,-30],speed = 4))










def levelChoice(choice):

    if choice=="level_1":
        level1 = level_1_Class()
        level1.environment()
        #level1.player()
        #level1.enemy()



levelChoice("level_1")


app.run()










'''

m = 0
n_frame = 400

# Entities
player = PlatformerController2d( scale = (1.3,1.5,.01/2),color = color.white, texture = 'assets/player.png', y = -2 , z = 0.01 )
ground = Entity(model = 'quad' ,texture = 'assets/floor.png', y = -4 , scale_x = 30 , collider = 'box')
ground1 = Entity(model = 'quad' ,texture = 'assets/floor.png', y = -5 , scale_x = 30 , collider = 'box')
ground2 = Entity(model = 'quad' ,texture = 'assets/floor.png', y = -4, x=30 , scale_x = 30 , collider = 'box')
ground3 = Entity(model = 'quad' ,texture = 'assets/floor.png', y = -5 , x=30, scale_x = 30 , collider = 'box')
ground4 = Entity(model = 'quad' ,texture = 'assets/floor.png', y = -4, x=60 , scale_x = 30 , collider = 'box')
ground5 = Entity(model = 'quad' ,texture = 'assets/floor.png', y = -5 , x=60, scale_x = 30 , collider = 'box')

uxy = [[-1,0],[-5,-1.5],[5,-0.5],[-7,1.3],[3,2]]

ulevels = []
ulevel = Entity(model='quad',texture = 'assets/ublock.png',scale=(2,0.7),position=uxy[0],
               collider = 'box')
ulevels.append(ulevel)




nxy = [[-1,0],[-5,-1.5],[5,-0.5],[-7,1.3],[3,2]]

nlevels = []
nlevel = Entity(model='quad',texture = 'assets/ublock.png',scale=(2,0.7),position=nxy[0],
               collider = 'box')
nlevels.append(nlevel)





levels.append(duplicate(level, position=xy[1]))
levels.append(duplicate(level, position=xy[2]))
levels.append(duplicate(level, position=xy[3]))
levels.append(duplicate(level, position=xy[4]))

camera.add_script(SmoothFollow(target = player , offset = [0,3,-30],speed = 4))

#app.run()

'''