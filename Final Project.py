import turtle
import random

SIZE_X=1000
SIZE_Y=1000
turtle.setup(SIZE_X, SIZE_Y)
screen = turtle.Screen()
screen.bgpic('BackgroundRoom.gif')
SQUARE_SIZE = 20
turtle.register_shape("armsofa.gif")
turtle.register_shape("long_shirt.gif")
turtle.register_shape("singlebed.gif")
turtle.register_shape("tablelamp.gif")
turtle.register_shape("thegirl.gif")

def check_item(item):
    if item == "singlebed":
        item_ap(item,singlebed)
        print(pricing() + 1400)
    if item == "armsofa":
        item_ap(item,armsofa)
    if item == "long_shirt":
        item_ap(item,long_shirt)
    if item == "tablelamp":
        item_ap(item,tablelamp)
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
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)+1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    pos_x = random.randint(min_x,max_x)*SQUARE_SIZE
    pos_y = random.randint(min_y,max_y)*SQUARE_SIZE

    #make a stamp and put it on the random place
    item_turtle.goto(pos_x,pos_y)

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
long_shirt = turtle.Turtle()
tablelamp = turtle.Turtle()




choose_items()
