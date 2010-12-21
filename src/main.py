'''
Created on 21 dec 2010

@author: robert
'''

from visual import *
import cmath

def create_world(f):
    objects = []
    
    # All the objects in the world
    floor = box(pos=(0,-2,0),length=200,height=1,width=200,color=color.green,frame=f,material=materials.rough)
    b1 = box(pos=(-20,0,0),length=20,height=2,width=20,color=color.blue,frame=f)
    b2 = box(pos=(-20,0,0),length=15,height=4,width=15,color=color.blue,frame=f)
    # Add them to the objects list
    objects.append(floor)
    objects.append(b1)
    objects.append(b2)
    
    return objects

def create_enemy(f):
    enemy = sphere(pos=(30,0,0),radius=10,color=color.red,frame=f)
    return enemy

def create_hud():
    ammo = label()
    ammo.text = "1337/1338"
    ammo.pos = vector(-2.5,-2.0,-5)

def move_objects(objects, pos):
    for obj in objects:
        obj.pos += pos

def main():
    game_scene = display(title='Charley',x=1000,y=500,width=800,height=600,center=(0,0,0),background=(0,1,1),userzoom=false,userspin=false,
                        autoscale=false,scale=(1,1,1),autocenter=false)
    f = frame()

    create_hud()
    objects = create_world(f)
    objects.append(create_enemy(f))
    
    yrot = 0
    player_angle = 0

    turn_angle = 3*0.034906585

    # Main loop
    while 1:
        rate(1000)
        if game_scene.kb.keys:
            s = game_scene.kb.getkey()
            if s == 'w':
                move_objects(objects, (-sin(player_angle),0,cos(player_angle)))
            elif s == 's':
                move_objects(objects, (sin(player_angle),0,-cos(player_angle)))
            elif s == 'd':
                yrot = turn_angle
                player_angle += turn_angle
            elif s == 'a':
                yrot = -turn_angle 
                player_angle -= turn_angle
                if player_angle < 0:
                    player_angle = 2*cmath.pi + player_angle 
            elif s == 'm':
                move_objects(objects, (0,-0.5,0))
            elif s == 'n':
                move_objects(objects, (0,0.5,0))
        if player_angle >= 2*cmath.pi:
            player_angle -= 2*cmath.pi            
        
        # Do the rotations on the y axis
        f.rotate(angle=yrot,axis=vector(0,1,0))
        yrot = 0


if __name__ == '__main__':
    main()