import turtle
import random
import time

turtle.speed(0)
turtle.tracer(1,0)
price = 0

SIZE_X = 1920
SIZE_Y = 1060

turtle.setup(SIZE_X,SIZE_Y) # setting up the borders to be 1000x1000
turtle.color("blue")

#CREATING THE PLAYER
turtle.register_shape("player1.gif")
turtle.register_shape("left.gif")
player = turtle.clone()
player.shape("player1.gif")

#CREATING THE SELLER
turtle.register_shape("Seller(1).gif")
seller = turtle.clone()
seller.shape("Seller(1).gif")

#CREATING WRITING DUDE
writer = turtle.clone()
writer.shape("turtle")
writer.up()
writer.goto(860,440)

#LISTS
player_pos = []
obj_pos = []

turtle.hideturtle()

screen = turtle.Screen()


screen.bgpic('BackgroundRoom.gif')
SQUARE_SIZE = 20

#Registering the shapes To make them available players!
turtle.register_shape("armsofa.gif")
turtle.register_shape("singlebed.gif")
turtle.register_shape("Seller(1).gif")
turtle.register_shape("tree.gif")

shape_ls = ["armsofa", "singlebed"]

#Writing the List of Shapes
turtle.up()
turtle.goto(0,400)
turtle.write(shape_ls, False, "center", font=("Arial", 18, "normal"))
turtle.down()

sold_list = []


def check_item(item):
    global price
    if item == "singlebed":
        item_ap(item,singlebed)
    if item == "armsofa":
        item_ap(item,armsofa)

def choose_items():
    item = str(screen.textinput('Welcome to the house', "What item would you like to swap?(armsofa or singlebed)"))
    check_item(item)
    item = str(screen.textinput('Choose more items, write no if you finished already', "What item would you like to swap?(armsofa or singlebed)"))
    check_item(item)
    turtle.ht()
    
#item appear in a random place
def item_ap(item,item_turtle):
    #make a turtle whose shape is the item
    #item_turtle = turtle.Turtle()
    item_turtle.shape(item + '.gif')
    item_turtle.penup()
    #make borders for the items to appear
    min_x=0 #-int(SIZE_X/4/SQUARE_SIZE)+1
    max_x=int(SIZE_X/5/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/5/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/5/SQUARE_SIZE)+1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    pos_x = random.randint(min_x,max_x)*SQUARE_SIZE
    pos_y = random.randint(min_y,max_y)*SQUARE_SIZE

    #make a stamp and put it on the random place

    item_turtle.goto(pos_x,pos_y)
    obj_pos.append(item_turtle.pos())

#Creating The Objects
singlebed = turtle.Turtle()
armsofa = turtle.Turtle()

#Puttin em in a list
objects = [singlebed, armsofa]

choose_items()

#MAKING THE FIRST LEVEL(THE HOUSE)
turtle.pensize(10)
ishouse = True
 
#Setting position for seller character
seller.up()
seller.goto(-225, 0)

seller.speed(1)

#This variable is to see if plant tree was called
istree = None

def plant_tree():
    global price, istree
    if not istree:
        if price >= 2000:
            istree = True
            turtle.clear()
            writer.undo()
            writer.color("red")
            writer.write("$" + str(price),False,"center",font=("Arial", 30, "bold"))
            time.sleep(0.2)
            screen.bgpic('forestobig.gif')
            trees_num = int(screen.textinput('With the money you have gained', "How many trees would you like to plant? every tree cost 2$"))
            tree_turtle = turtle.Turtle()
            tree_turtle.up()
            tree_turtle.shape("tree.gif")
            if (trees_num * 2) < price:
                for i in range(0,trees_num):
                    min_x=-int(1000/2/SQUARE_SIZE)+1
                    max_x=int(1000/2/SQUARE_SIZE)-1
                    min_y=-int(1000/2/SQUARE_SIZE)-1
                    max_y=int(1000/2/SQUARE_SIZE)+1
            
                        #Pick a position that is a random multiple of SQUARE_SIZE
                    pos_x = random.randint(min_x,max_x)*SQUARE_SIZE
                    pos_y = random.randint(min_y,max_y)*SQUARE_SIZE
                    tree_turtle.goto(pos_x,pos_y)
                    idtree = tree_turtle.stamp()
                    tree_list.append(idtree)
            #time.sleep(2)
            print("You planted " + str(trees_num) + " trees!")
            print("keep helping the enviorment")
            #for t in tree_list:
                #tree_turtle.clearstamp()
            price -= trees_num * 2
            time.sleep(4)
            tree_turtle.clearstamps()
            tree_turtle.ht()
            make_house()
            turtle.listen()
            writer.undo()
    else:
        turtle.clear()
        writer.undo()
        writer.goto(860,440)
        writer.color("red")
        writer.write("$" + str(price),False,"center",font=("Arial", 30, "bold"))
        time.sleep(0.2)
        screen.bgpic('forestobig.gif')
        trees_num = int(screen.textinput('With the money you have gained', "How many trees would you like to plant? every tree cost 2$"))
        tree_turtle = turtle.Turtle()
        tree_turtle.up()
        tree_turtle.shape("tree.gif")
        if (trees_num * 2) < price:
            for i in range(0,trees_num):
                min_x=-int(1000/2/SQUARE_SIZE)+1
                max_x=int(1000/2/SQUARE_SIZE)-1
                min_y=-int(1000/2/SQUARE_SIZE)-1
                max_y=int(1000/2/SQUARE_SIZE)+1
        
                    #Pick a position that is a random multiple of SQUARE_SIZE
                pos_x = random.randint(min_x,max_x)*SQUARE_SIZE
                pos_y = random.randint(min_y,max_y)*SQUARE_SIZE
                tree_turtle.goto(pos_x,pos_y)
                idtree = tree_turtle.stamp()
                tree_list.append(idtree)
        #time.sleep(2)
        print("You planted " + str(trees_num) + " trees!")
        print("keep helping the enviorment")
        #for t in tree_list:
            #tree_turtle.clearstamp()
        price -= trees_num * 2
        time.sleep(4)
        tree_turtle.clearstamps()
        tree_turtle.ht()
        make_house()
        turtle.listen()
        writer.undo()


#function to make house
def make_house():
    global sold_list
    turtle.clear()
    screen.bgpic("BackgroundRoom.gif")
    seller.hideturtle()
    turtle.up()
    turtle.goto(-400,-300)
    turtle.down()
    house_pos = [(400,-300),(400,300),(-400,300),(-400,-300)]
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

turtle.onkeypress(up, UP_ARROW)


#MAKING THE THING MOVE
def down():
    global direc
    direc = DOWN
    player_move()

turtle.onkeypress(down, DOWN_ARROW)

def right():
    global direc
    direc = RIGHT
    player_move()
    player.shape("player1.gif")

turtle.onkeypress(right, RIGHT_ARROW)

def left():
    global direc
    direc = LEFT
    player.shape("left.gif")
    player_move()

turtle.onkeypress(left, LEFT_ARROW)

obj_ind = None

tree_list = []
        
seller.speed(1)

def player_move():
    global ishouse, obj_ind, sold_list, price
    STEP = 20
    player_pos = player.pos()
    # XOS YOS ARE X AND Y POSTIONS FOR PLAYER
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
        elif not ishouse: #THIS R CODE FOR HIT WALL RIGHT
            player.goto(-300,0)
            objects[obj_ind].goto(-300,40)
            make_house()
            ishouse = True
        elif istree and ishouse:
            plant_tree()
        else:
            player.goto(xos-STEP,yos)

    #This is for selling the objects to the seller character
    for x in objects:
        if ishouse and x not in sold_list:
            x.st()
        if x.pos() == player.pos():
            obj_ind = objects.index(x)
        if x.pos()[0] <= seller.pos()[0]+125 and x.pos()[0] > seller.pos()[0]-20 and not ishouse and x not in sold_list:
            x.ht()
            sold_list.append(x)
            print("poof!")
            price += 1001
            print("supreme, gucci... most importantly TREES")
            plant_tree()
            writer.color("green")
            writer.write("$" + str(price),False,"center",font=("Arial", 30, "bold"))
    #This is to make items disappear when changing rooms
    if obj_ind != None:
        objects[obj_ind].goto(xos ,yos + 40)
        if obj_ind == 0 and not ishouse:
            objects[1].hideturtle()
        elif obj_ind == 1 and not ishouse:
            objects[0].hideturtle()

def make_market():
    turtle.clear()
    screen.bgpic("market(2).gif")
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



turtle.listen()













