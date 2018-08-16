import turtle

SIXE = 1000
SIZE = 1000
turtle.speed(0)

turtle.setup(SIXE,SIZE) # setting up the borders to be 1000x1000
#MAKING THE FIRST LEVEL(THE HOUSE)
turtle.pensize(10)
ishouse = True
 
#CREATING THE SELLER
turtle.register_shape("Seller(1).gif")
seller = turtle.clone()
seller.shape("Seller(1).gif")

seller.up()
seller.goto(-225, 0)

seller.speed(1)
 
def make_house():
    turtle.clear()
    seller.hideturtle()
    turtle.up()
    print("REEEEE")
    turtle.goto(-400,-270)
    turtle.down()
    house_pos = [(400,-270),(400,200),(-400,200),(-400,-270),(-400,200),(0,350),(400,200)]
    for da_hous_pos in house_pos:
        turtle.goto(da_hous_pos[0],da_hous_pos[1])
    turtle.up()
    turtle.goto(0,0)
    turtle.down()
    
make_house()

edgeup = 200
edgedown = -270
edgeright = 400
edgeleft = -400

#LISTS
player_pos = []
obj_pos = []
obj_stamps = []

#CREATING THE PLAYER
turtle.register_shape("player1.gif")
turtle.register_shape("left.gif")
player = turtle.clone()
player.shape("player1.gif")



turtle.hideturtle()
player.up()

                               #O
                            #O  O
#MAKING IT MO     OVE
                            #O  O
                               #O

UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"
if not ishouse:
    counter = 300
time_step = 5

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

direc = None #Direction but too lazy to write it fully :p

def up():
    global direc
    direc = UP
    player_move()
    print("up")

turtle.onkeypress(up, UP_ARROW)

def down():
    global direc
    direc = DOWN
    player_move()
    print("down")

turtle.onkeypress(down, DOWN_ARROW)

def right():
    global direc
    direc = RIGHT
    player_move()
    player.shape("player1.gif")
    print("right")

turtle.onkeypress(right, RIGHT_ARROW)

def left():
    global direc
    direc = LEFT
    player.shape("left.gif")
    player_move()
    print("left")

turtle.onkeypress(left, LEFT_ARROW)

turtle.listen()

def player_move():
    global ishouse
    player_pos = player.pos()
    # XOS YOS ARE X AND Y POSTIOTIONTOINS FOR PLAYER
    xos = player_pos[0] 
    yos = player_pos[1]
    if direc == UP:
        if not yos >= edgeup:
            player.goto(xos,yos+25)
        else:
            player.goto(xos,yos-25)
    elif direc == DOWN:
        if not yos <= edgedown:
            player.goto(xos,yos-25)
        else:
            player.goto(xos,yos+25)
    elif direc == LEFT:
        if not xos <= edgeleft:
            player.goto(xos-25,yos)
        elif ishouse: #THIS R CODE FOR HIT WALL LEFT
            player.goto(400,0)
            make_market()
            ishouse = False
        else:
            player.goto(xos+25,yos)
    elif direc == RIGHT:
        if not xos >= edgeright:
            player.goto(xos+25,yos)
        elif not ishouse:
            player.goto(-400,0)
            make_house()
            ishouse = True
        else:
            player.goto(xos-25,yos)

    #THIS R IS EDGE
        


def make_market():
    turtle.clear()
    seller.showturtle()
    turtle.penup()
    turtle.goto(-400,-270)
    turtle.pendown()
    market_pos = [(400,-270),(400,270),(-400,270),(-400,-270)]
    for da_mark_pos in market_pos:
        turtle.goto(da_mark_pos[0],da_mark_pos[1])
    turtle.penup()
    turtle.goto(-200,75)
    turtle.pendown()
    turtle.goto(-250,75)
    turtle.goto(-200,75)
    turtle.goto(-200,-75)
    turtle.goto(-250,-75)
    for x in range(10):
        seller.goto(-225, 20)
        seller.goto(-225, -20)
    seller.goto(-225, 0)












