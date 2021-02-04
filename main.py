from ursina import *
class Test_cube(Entity):
    def __init__(self):
        super().__init__(
            model ='cube',
            color = color.white,
            texture = 'white_cube'
            rotation = Vec3(0,0,0)
            )
def update():
    if held_keys['a']:
        test_square.x -= 3 * time.dt
    if held_keys['d']:
        test_square.x += 3 * time.dt
app = Ursina()
test_square = Entity (model = 'quad', color = color.red, scale = (1,4), position = (5,4 ))
sans = Entity (model = 'quad', texture = 'sans.png')

test_cube = Test_cube()

app.run()
