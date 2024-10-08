freq = 240
# dt = 1.0/freq
dt = 0.001

def scene_init():
    global scene1, ironball, ping_pong, Label, Label2
    scene1 = display(width=600, height=400, background=vector(0.5,0.6,0.5), y=0)
    arrow1 = arrow(display=scene1, pos=vector(-1,0,0), axis=vector(2,0,0), shaftwidth=0.005)
    arrow4 = arrow(display=scene1, pos=vector(0,0,0), axis=vector(0,0.3,0), shaftwidth=0.005)
    
    gd1 = gdisplay(x=600, y=0, title='v vs t', xtitle='t', ytitle='v', ymax=1, xmax=2, background=vector(0.3,0.3,0.3))
    vt1 = gcurve(gdisplay=gd1, color=vector(0.5, 0.5, 0.5))
    vt2 = gcurve(gdisplay=gd1, color=color.orange)
    vts= (vt1, vt2)
    
    ironball = sphere(display=scene1, radius=0.05, pos=vector(-0.2,0,0), color=vector(0.5, 0.5, 0.5)) 
    ironball.m = 0.5
    ironball.v = 0.5#(pi*4/3*(0.05)**3)*7.9*1e3, 0
    
    ping_pong = sphere(display=scene1, radius=0.02, pos=vector(0.1,0,0), color=color.orange)
    ping_pong.m = 0.1
    ping_pong.v = 0#2.6*10e-3, 0
    balls=(ironball, ping_pong)
    Label = label(pos=vector(0.3,0.4,0), text='GG', height = 0.2)
    Label2 = label(pos=vector(0.3,0.2,0), text='GG', height = 0.2)
#spring = helix(pos=vector(-0.15,0,0), radius=0.01, coils=10, thickness = 0.01, length = 0.23)

def resetScene():
    scene1.background = vector(0.5, 0.6, 0.5)
    ironball.pos = vector(-0.2, 0, 0)
    scene1.background = vector(0.5, 0.6, 0.5)
    ironball.pos = vector(-0.2,0,0)
    ping_pong.pos = vector(0.1,0,0)
    ironball.v = 0
    ping_pong.v = 0

def Command(data):
    global speed, ironball
    if data != None:
        ironball.v = data[0]/20

def setup():
   #df = 'Speed'
   scene_init()
   profile = {
       'dm_name': 'Collision1',
       'odf_list': [Command]
   }
   dai(profile)

setup()

while True:
    rate(freq)

    if ping_pong.pos.x > 0.8:
        resetScene()

    Label.text = 'Ironball ' + ironball.v
    Label2.text = 'Pingpong ' + ping_pong.v
    ironball.pos.x = ironball.pos.x + ironball.v * dt
    
    ping_pong.pos.x = ping_pong.pos.x + ping_pong.v * dt

    if abs(ironball.pos.x-ping_pong.pos.x) < (ironball.radius+ping_pong.radius) and ironball.v > ping_pong.v:
        m_add = ironball.m + ping_pong.m
        m_sub = ironball.m - ping_pong.m
        ironball.v = ironball.v*m_sub/m_add + ping_pong.v*2*ping_pong.m/m_add
        ping_pong.v = ironball.v*2*ironball.m/m_add - ping_pong.v*m_sub/m_add

