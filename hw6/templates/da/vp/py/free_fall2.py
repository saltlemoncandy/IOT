size = 0.25
height = 15.0

scene = display(width=800, height=800, center = vector(0, height/2, 0), background=vector(0.5, 0.5, 0))
floor = box(length=30, height=0.01, width=10, color=color.blue)

def ballfall(data):
    ball = sphere(radius = size, color = color.red)
    ball.pos = vector(0, height, 0)
    ball.velocity = vector(0,0,0)
    dt = 0.001
    g = data

    def fall():
        if ball.pos.y >= size:
            rate(1000, fall)
        else:
            ball.visible = False
        ball.pos = ball.pos + ball.velocity * dt
        ball.velocity.y += -g*dt
    
    fall()
	

def gValue(data):
    if data != None:
        ballfall(data[0])

def setup():
    profile = {
        'dm_name' : 'Free_Fall2',
        'odf_list' : [gValue]
    }	
    dai(profile)


setup()
#csmRegister(profile)
	
#rate(1, progress)	