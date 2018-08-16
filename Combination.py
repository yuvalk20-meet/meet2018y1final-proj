import turtle
import random
import time

turtle.speed(0)
turtle.tracer(1,0)

#CREATING THE PLAYER
turtle.register_shape("player1.gif")
turtle.register_shape("left.gif")
player = turtle.clone()
player.shape("player1.gif")

#CREATING THE SELLER
turtle.register_shape("Seller(1).gif")
seller = turtle.clone()
seller.shape("Seller(1).gif")

#LISTS
player_pos = []
obj_pos = []


turtle.hideturtle()
SIZE_X=1000
SIZE_Y=1000
turtle.setup(SIZE_X, SIZE_Y)
screen = turtle.Screen()
screen.bgpic('BackgroundRoom.gif')
SQUARE_SIZE = 20
turtle.register_shape("armsofa.gif")
turtle.register_shape("singlebed.gif")
turtle.register_shape("Seller(1).gif")



shape_ls = ["armsofa", "singlebed"]

turtle.up()
turtle.goto(0,400)
turtle.write(shape_ls, False, "center", font=("Arial", 18, "normal"))
turtle.down()


def check_item(item):
    if item == "singlebed":
        item_ap(item,singlebed)
        print(pricing() + 1400)
    if item == "armsofa":
        item_ap(item,armsofa)
    if item == "picture":
        item_ap(item,picture)




def choose_items():
    item = str(screen.textinput('Welcome to the house', "What item would you like to swap?"))
    check_item(item)
    item = str(screen.textinput('Choose more items, write no if you finished already', "What item would you like to swap?"))
    check_item(item)
    turtle.ht()
    
#item appear in a random place
def item_ap(item,item_turtle):
    #make a turtle whose shape is the item
    #item_turtle = turtle.Turtle()
    item_turtle.shape(item + '.gif')
    item_turtle.penup()
    #make borders for the items to appear
    min_x=-int(SIZE_X/4/SQUARE_SIZE)+1
    max_x=int(SIZE_X/4/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/4/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/4/SQUARE_SIZE)+1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    pos_x = random.randint(min_x,max_x)*SQUARE_SIZE
    pos_y = random.randint(min_y,max_y)*SQUARE_SIZE

    #make a stamp and put it on the random place

    item_turtle.goto(pos_x,pos_y)
    obj_pos.append(item_turtle.pos())

def pricing():
    item_age = int(screen.textinput('Age', "How old is your item?"))
    item_conditinal = str(screen.textinput('Condition', "Broken, Ok, As new"))
    price = 0
    if item_conditinal == 'Broken':
        price -= 200
        if item_age >= 5:
            price += 50
        elif item_age <= 2:
            price -=20
        elif item_age <= 10:
            price += 35
    elif item_conditinal == 'Ok':
        price += 100
        if item_age >= 5:
            price += 50
        elif item_age <= 2:
            price -=20
        elif item_age <= 10:
            price += 35
    elif item_conditinal == 'As new':
        price += 250
        if item_age >= 5:
            price += 50
        elif item_age <= 2:
            price -=20
        elif item_age >= 10:
            price += 35
    else:
        price = 0
    return price
    
    
    
    

singlebed = turtle.Turtle()
armsofa = turtle.Turtle()


objects = [singlebed, armsofa]

choose_items()

SIXE = 1000
SIZE = 1000
turtle.speed(0)

turtle.setup(SIXE,SIZE) # setting up the borders to be 1000x1000
#MAKING THE FIRST LEVEL(THE HOUSE)
turtle.pensize(10)
ishouse = True
 

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

edgeup = 400
edgedown = -270
edgeright = 400
edgeleft = -400


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
    print(obj_pos)

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

def drop():
    global obj_ind
    obj_ind = None

turtle.onkeypress(drop, "space")

turtle.listen()

obj_ind = None

def player_move():
    global ishouse, obj_ind
    STEP = 20
    player_pos = player.pos()
    # XOS YOS ARE X AND Y POSTIOTIONTOINS FOR PLAYER
    xos = player_pos[0] 
    yos = player_pos[1]
    if direc == UP:
        if not yos >= edgeup:
            player.goto(xos,yos+STEP)
        else:
            player.goto(xos,yos-STEP)
    elif direc == DOWN:
        if not yos <= edgedown:
            player.goto(xos,yos-STEP)
        else:
            player.goto(xos,yos+STEP)
    elif direc == LEFT:
        if not xos <= edgeleft:
            player.goto(xos-STEP,yos)
        elif ishouse: #THIS R CODE FOR HIT WALL LEFT
            player.goto(300,0)
            objects[obj_ind].goto(300,40)
            make_market()
            ishouse = False
        else:
            player.goto(xos+STEP,yos)
    elif direc == RIGHT:
        if not xos >= edgeright:
            player.goto(xos+STEP,yos)
        elif not ishouse:
            player.goto(-300,0)
            objects[obj_ind].goto(-300,40)
            make_house()
            ishouse = True
        else:
            player.goto(xos-STEP,yos)

    for x in objects:
        print("object:",x.pos()," player:",player.pos())
        if x.pos() == player.pos():
            print("picking up")
            print("seller pos: ", seller.pos())
            obj_ind = objects.index(x)
        if x.pos()[0] <= seller.pos()[0]+125 and x.pos()[0] > seller.pos()[0]-20 and not ishouse:
            x.ht()
            print("poof!") 
                        
    print(obj_ind)
    if obj_ind != None:
        objects[obj_ind].goto(xos ,yos + 40)
        if obj_ind == 0 and not ishouse:
            objects[1].hideturtle()
        elif obj_ind == 1 and not ishouse:
            objects[0].hideturtle()
        elif obj_ind == 1 and ishouse:
            objects[0].showturtle()
        elif obj_ind == 0 and ishouse:
            objects[1].showturtle()
        

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














