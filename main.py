"""

 _______         _   _              _______         _   _     

|__   __|       | | | |            |__   __|       | | | |    

   | |_   _ _ __| |_| | ___ _   _     | |_   _ _ __| |_| | ___

   | | | | | '__| __| |/ _ \ | | |    | | | | | '__| __| |/ _ \

   | | |_| | |  | |_| |  __/ |_| |    | | |_| | |  | |_| |  __/

   |_|\__,_|_|   \__|_|\___|\__, |    |_|\__,_|_|   \__|_|\___|

                             __/ |                            

                            |___/                             

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                       Version 1.4.1

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                         Credits:

  

   turtle module, time module, random module, math module, and other built

   in python functions.

  

   IETF for base64 documentation.

   https://www.rfc-editor.org/rfc/rfc4648#section-4

"""

# import modules

import turtle

import time

import random

import math

# config files

from gameconfig import *

# initialize variables / lists

points = 0

pointSet1 = True

pointSet2 = True

highScore = 0

gamesList = []

gamesPlayed = 0

currentWindow = "game"

pointSum = 0

randomDecay = 0

buyOn = False

# setup window

win = turtle.Screen()

win.setup(400, 450)

win.tracer(0)

# import textures

win.addshape("shop(0).png")

win.addshape("shop(1).png")

win.addshape("shop(2).png")

win.addshape("shop_bg(0).png")

win.addshape("moonlander.png")

win.addshape("sunset_bg.png")

win.addshape("pizza.png")

win.addshape("torpedo.png")

win.addshape("Game_Over.png")

win.addshape("comingsoon.png")

win.addshape("gamebackground.png")

win.addshape("gameforeground.png")

win.addshape("options.png")

win.addshape("menu.png")

win.addshape("pearl.png")

win.addshape("pole.png")

win.addshape("rock.png")

win.addshape("sub.png")

win.addshape("current.png")

win.addshape("charge_empty.png")

win.addshape("charge_1.png")

win.addshape("charge_2.png")

win.addshape("charge_full.png")

win.addshape("buybutton.png")

win.addshape("time-machine.png")

win.addshape("urchin.png")

win.addshape("otter.png")

# background

bg = turtle.Turtle()

bg.shape("gamebackground.png")

bg.hideturtle()

bg.left(90)

bg.stamp()

bg2 = turtle.Turtle()

bg2.shape("gamebackground.png")

bg2.hideturtle()

bg2.penup()

bg2.left(90)

bg2.goto(600, 0)

bg2.stamp()

# move background function

def bgMove():

   global s

   bg.clear()

   bg2.clear()

   x = bg.xcor()

   x2 = bg2.xcor()

   if x <= -600:

       bg.goto(600, 0)

   if x2 <= -600:

       bg2.goto(600, 0)

   x = bg.xcor()

   x2 = bg2.xcor()

   bg.setx(x - (s / 2))

   bg2.setx(x2 - (s / 2))

   bg.stamp()

   bg2.stamp()


# make the turtle

turt = turtle.Turtle()

turt.speed(0)

turt.shape("turtle")

turt.color("green")

turt.penup()

turt.goto(-150, 0)

turt.direction = "stop"

# poles

# pole1 center

pole1 = turtle.Turtle()

pole1.speed(0)

pole1.shape("pole.png")

pole1.hideturtle()

pole1.penup()

pole1.goto(250, 0)

pole1.left(90)

pole1.direction = "stop"

# pole2 center

pole2 = turtle.Turtle()

pole2.speed(0)

pole2.shape("pole.png")

pole2.hideturtle()

pole2.penup()

pole2.goto(450, 0)

pole2.left(90)

pole2.direction = "stop"

# foreground

fg = turtle.Turtle()

fg.shape("gameforeground.png")

fg.hideturtle()

fg.penup()

fg.left(90)

fg.stamp()

fg2 = turtle.Turtle()

fg2.shape("gameforeground.png")

fg2.hideturtle()

fg2.penup()

fg2.goto(660, 0)

fg2.left(90)

fg2.stamp()


def fgMove():

   global s

   fg.clear()

   fg2.clear()

   x = fg.xcor()

   x2 = fg2.xcor()

   if x <= -700:

       fg.goto(620, 0)

   if x2 <= -700:

       fg2.goto(620, 0)

   x = fg.xcor()

   x2 = fg2.xcor()

   fg.setx(x - (s * 1.2))

   fg2.setx(x2 - (s * 1.2))

   fg.stamp()

   fg2.stamp()


# current

current1 = turtle.Turtle()

current1.shape("current.png")

current1.penup()

current1.left(90)

currentState = False

currentPos = [600, 800, 1000, 1200]

current1.goto(random.choice(currentPos), 0)


def current():

   global s

   global currentState

   x = turt.xcor()

   x1 = current1.xcor()

   current1.setx(x1 - s)

   if x > (x1 - 60):

       if (x < (x1 + 60)) and currentState == False:

           currentOn()

   elif (x > (x1 + 60)) and currentState == True:

       currentOff()

       print("off")

   elif (x < (x1 - 60)) and currentState == True:

       currentOff()

   if x1 < -250:

       current1.goto(random.choice(currentPos), 0)


def currentOn():

   global flapS

   global flapHeight

   global gravInc

   global gravityIncrease

   global currentState

   flapS = flapHeight / currentHandicap

   gravInc = gravityIncrease * 1.1

   currentState = True


def currentOff():

   global flapS

   global flapHeight

   global gravInc

   global gravityIncrease

   global currentState

   flapS = flapHeight

   gravInc = gravityIncrease

   currentState = False


# game running?

running = True

start = False

# gravity stuff

grav = gravityConst

gravInc = gravityIncrease

# reset the game

def reset():

   time.sleep(0.1)

   global grav

   global points

   global s

   global pointSet1

   global pointSet2

   global flapS

   global currentWindow

   global abilityOn

   global currentSkin

   global pointStore

   global disableFlap

   global unlockedSkins

   currentWindow = "game"

   s = speed

   flapS = flapHeight

   current1.goto(1400, 0)

   turt.goto(-150, 0)

   turt.direction = "stop"

   pole1.goto(250, 0)

   pole1.direction = "stop"

   pole2.goto(450, 0)

   pole2.direction = "stop"

   pearl.goto(350, 0)

   bg.goto(0, 0)

   bg2.goto(700, 0)

   grav = gravityConst

   points = 0

   pointSet1 = True

   pointSet2 = True

   win.bgpic("gamebackground.png")

   display.clear()

   display2.clear()

   pages.clear()

   turt.showturtle()

   pearl.showturtle()

   current1.showturtle()

   abilityOn = False

   pointsStore = 0

   abilityT = 0

   disableFlap = False

   abilityCooldown()

   buy.hideturtle()

   skinUnlocked = False

   if currentSkin in unlockedSkins:

       skinUnlocked = True

   if skinUnlocked == False:

       currentSkin = "turtle"

       turt.shape("turtle")

   if currentSkin != "turtle":

       chargeBar.showturtle()

   else:

       chargeBar.hideturtle()


# enact gravity on the turtle

def gravity():

   global grav

   global gravInc

   y = turt.ycor()

   turt.sety(y - grav)

   if grav <= 10:

       grav += gravInc


# points system

def point():

   global pointSet1

   global pointSet2

   global points

   global difLevel

   global polePoints

   x = turt.xcor()

   x1 = pole1.xcor()

   x2 = pole2.xcor()

   if x > (x1):

       if pointSet1 == True:

           pointSet1 = False

           points += polePoints

           difLevel = difLevel + 1

           score.clear()

   if x > (x2):

       if pointSet2 == True:

           pointSet2 = False

           points += polePoints

           difLevel = difLevel + 1

           score.clear()


display = turtle.Turtle()

display.hideturtle()

display.penup()

display.goto(0, 0)

display.color("white")

display.write(

   "press space or click to swim", font=(gameFont, fontSize, "bold"), align="center"

)


# high score for the session

def highScoreFunction():

   global highScore

   if points > highScore:

       highScore = points


# when you loose the game

looseSeq = False


def loose():

   global start

   global looseSeq

   global highScore

   global points

   global gamesPlayed

   global numGames

   global currentWindow

   global pointSum

   global previousWindows

   currentWindow = "game over"

   previousWindows.append("loose")

   start = False

   looseSeq = True

   turt.hideturtle()

   pearl.hideturtle()

   current1.hideturtle()

   chargeBar.hideturtle()

   # for the game list

   gamesList.append(points)

   gamesPlayed += 1

   if gamesPlayed >= 15:

       numGames += 1

   highScoreFunction()

   pointSum += points

   display.penup()

   display.goto(0, -150)

   display.color("white")

   display.write(highScore, font=(gameFont, fontSize, "bold"), align="center")

   display.penup()

   display.goto(0, -175)

   display.color("white")

   display.write(

       "session high score", font=(gameFont, fontSize, "bold"), align="center"

   )

   pole1.clear()

   pole2.clear()

   bg.clear()

   bg2.clear()

   fg.clear()

   fg2.clear()

   pages.clear()

   win.update()

   win.bgpic("Game_Over.png")

   time.sleep(1)

   looseSeq = False


score = turtle.Turtle()

score.hideturtle()

score.penup()

score.color("white")

score.goto(0, 175)


def scoreDisplay():

   # display points

   score.clear()

   score.write(

       "points - " + str(points), font=(gameFont, fontSize, "bold"), align="center"

   )


poleGap = 75

poleGap = poleGap / 2

# define pearls

pearl = turtle.Turtle()

pearl.shape("pearl.png")

pearl.penup()

pearl.setx(350)

pearlPosList = [300, 500, 700]

# all things to do with pearls

def pearlMove():

   global s

   global peralPoints

   x = pearl.xcor()

   pearl.setx(x - s)

   # recycles pearl

   if x < -210:

       pearl.goto(

           pole1.xcor() + random.choice(pearlPosList), random.randint(-150, 150)

       )

   # collision

   global points

   turtX = turt.xcor()

   turtY = turt.ycor()

   y = pearl.ycor()

   cooldown = 0

   if (

       (turtY + 9) > (y - 9)

       and (turtY - 9) < (y + 9)

       and (turtX + 9) > (x - 9)

       and (turtX + 9) < (x + 9)

   ):

       if not (cooldown):

           points += pearlPoints

           pearl.goto(

               pole1.xcor() + random.choice(pearlPosList), random.randint(-150, 150)

           )


s = 1

# moves poles

def pole():

   global start

   global s

   global pointSet1

   global pointSet2

   pole1.clear()

   pole2.clear()

   x = pole1.xcor()

   pole1.setx(x - s)

   x2 = pole2.xcor()

   pole2.setx(x2 - s)

   pole1.stamp()

   pole2.stamp()

   # recycles poles

   if x < -210:

       pole1.goto(200, random.randint(-150, 150))

       pointSet1 = True

   if x2 < -210:

       pole2.goto(200, random.randint(-150, 150))

       pointSet2 = True


# flap to make turtle go up

flapS = flapHeight

# previous games window

numGames = 0


def previousGames():

   global gamesList

   global gamesPlayed

   global numGames

   display.clear()

   score.clear()

   win.bgcolor("black")

   win.update()

   display.penup()

   display.color("white")

   display.goto(0, -175)

   display.write(

       "<press space or click anywhere to continue>",

       font=(gameFont, fontSize),

       align="center",

   )

   while len(gamesList) > 15:

       gamesList.pop(0)

   reps = 1

   for i in gamesList:

       display.goto(0, 175 - (reps * 20))

       display.write(

           "Game " + str(reps + numGames) + ": " + str(i),

           font=(gameFont, fontSize, "bold"),

           align="center",

       )

       reps += 1


# customize settings

# pages

pages = turtle.Turtle()

pages.penup()

pages.left(90)

pages.hideturtle()

pages.speed(0)

pages.shape("page(0).png")

# page the shop is on

shopPage = 0


def customize():

   global currentWindow

   global pointSum

   global shopPage

   shopPage = 0

   currentWindow = "shop"

   display.clear()

   score.clear()

   win.update()

   win.bgpic("shop_bg(0).png")

   shopPageUpdate()

   turt.goto(0, 50)

   turt.showturtle()


# update the shop

def shopPageUpdate():

   global shopPage

   score.clear()

   if shopPage == 0:

       pages.clear()

       pages.shape("shop(0).png")

       pages.stamp()

   elif shopPage == 1:

       pages.clear()

       pages.shape("shop(1).png")

       pages.stamp()

   elif shopPage == 2:

       pages.clear()

       pages.shape("shop(2).png")

       pages.stamp()

   else:

       print("error: shop page does not exist!")

   display.clear()

   display.penup()

   display.goto(0, 0)

   display.color("black")

   display.write(

       "total points - " + str(pointSum),

       font=(gameFont, fontSize, "bold"),

       align="center",

   )


# coming soon

def options():

   global currentWindow

   time.sleep(0.1)

   score.clear()

   display.clear()

   win.bgpic("options.png")

   currentWindow = "options"


def flap():

   global grav

   global start

   global disableFlap

   if disableFlap == False:

       if start == False:

           if looseSeq == False:

               reset()

               start = True

       else:

           y = turt.ycor()

           grav = 0

           turt.sety(y + flapS)

   else:

       pass


# display #2

display2 = turtle.Turtle()

display2.hideturtle()

display2.penup()

display2.color("red")

currentSkin = "turtle"

buy = turtle.Turtle()

buy.penup()

buy.shape("buybutton.png")

buy.goto(0, -190)

buy.hideturtle()

onSkin = "turtle"

onSkinCost = 0


def doBuy():

   global currentSkin

   global unlockedSkins

   global buyOn

   global pointSum

   global onSkin

   global onSkinCost

   pointSum -= onSkinCost

   unlockedSkins.append(onSkin)

   turt.shape(onSkin + ".png")

   win.update()

   currentSkin = onSkin

   buy.hideturtle()

   buyOn = False

   shopPageUpdate()


# buying feature for skins

def shopBuy(skin, cost):

   global pointSum

   global unlockedSkins

   global currentSkin

   global buyOn

   global onSkin

   global onSkinCost

   locked = True

   for x in unlockedSkins:  # if the skin is owned or not

       if x == skin:

           locked = False

   if pointSum >= cost and locked:

       display2.clear()

       display2.color("white")

       display2.goto(0, -165)

       display2.write(

           "cost: " + str(cost), font=(gameFont, fontSize, "bold"), align="center"

       )

       turt.shape(skin + ".png")

       currentSkin = skin

       buy.showturtle()

       buyOn = True

       onSkin = skin

       onSkinCost = cost

   elif locked == False:

       display2.clear()

       turt.shape(skin + ".png")

       currentSkin = skin

       buy.hideturtle()

   else:

       buy.hideturtle()

       turt.shape(skin + ".png")

       currentSkin = skin

       display2.clear()

       display2.color("red")

       display2.goto(0, -200)

       display2.write(

           "you need " + str(cost) + " points to unlock this.",

           font=(gameFont, fontSize, "bold"),

           align="center",

       )

   shopPageUpdate()


encoded = ""

binaryList = []

decoded = ""

decodeList = []

base64 = {

   "000000": "A",

   "000001": "B",

   "000010": "C",

   "000011": "D",

   "000100": "E",

   "000101": "F",

   "000110": "G",

   "000111": "H",

   "001000": "I",

   "001001": "J",

   "001010": "K",

   "001011": "L",

   "001100": "M",

   "001101": "N",

   "001110": "O",

   "001111": "P",

   "010000": "Q",

   "010001": "R",

   "010010": "S",

   "010011": "T",

   "010100": "U",

   "010101": "V",

   "010110": "W",

   "010111": "X",

   "011000": "Y",

   "011001": "Z",

   "011010": "a",

   "011011": "b",

   "011100": "c",

   "011101": "d",

   "011110": "e",

   "011111": "f",

   "100000": "g",

   "100001": "h",

   "100010": "i",

   "100011": "j",

   "100100": "k",

   "100101": "l",

   "100110": "m",

   "100111": "n",

   "101000": "o",

   "101001": "p",

   "101010": "q",

   "101011": "r",

   "101100": "s",

   "101101": "t",

   "101110": "u",

   "101111": "v",

   "110000": "w",

   "110001": "x",

   "110010": "y",

   "110011": "z",

   "110100": "0",

   "110101": "1",

   "110110": "2",

   "110111": "3",

   "111000": "4",

   "111001": "5",

   "111010": "6",

   "111011": "7",

   "111100": "8",

   "111101": "9",

   "111110": "+",

   "111111": "/",

}


def encode(string):

   global binaryList

   global encoded

   binaryList = []

   encoded = ""

   binary = ""

   end = ""

   try:

       binary = "".join([bin(ord(c))[2:].rjust(8, "0") for c in string])

       i = 0

       for x in binary:

           encoded += x

           i += 1

           if i > 5:

               binaryList.append(encoded)

               encoded = ""

               i = 0

       if encoded != "":

           binaryList.append(encoded)

       encoded = ""

       for x in binaryList:

           if len(x) == 6:

               encoded += str(base64.get(str(x)))

           else:

               for i in range(6 - len(x)):

                   x += str(0)

               encoded += str(base64.get(str(x)))

   except Exception as e:

       print("an error occured with encoding save: " + str(e))


def decode(string):

   global decoded

   global decodedList

   global base64

   decode = ""

   decodeList = []

   try:

       # lookup base64 and encode to binary

       keyList = list(base64.keys())

       valList = list(base64.values())

       for x in string:

           try:

               position = valList.index(x)

               decodeList.append(str(keyList[position]))

           except:

               pass

       for x in decodeList:

           decode += x

       while decode != "":

           i = chr(int(decode[:8], 2))

           decoded = decoded + i

           decode = decode[8:]

   except Exception as e:

       print("an error occured with decoding save: " + str(e))


def saveData():

   global pointSum

   global currentSkin

   global unlockedSkins

   skinList = ""

   for x in unlockedSkins:

       skinList += "|"

       skinList += x

   if currentSkin == "":

       currentSkin = "turtle"

   save = "turtleyturtle|" + str(pointSum) + "|" + currentSkin + skinList + "|"

   encode(save)

   print(encoded)

   saveFile = open("save", "w")

   saveFile.write(encoded)

   saveFile.close()


def openData(saveCode):

   global pointSum

   global currentSkin

   global unlockedSkins

   saveList = []

   saved = ""

   # write to save file

   saveFile = open("save", "w")

   saveFile.write(saveCode)

   saveFile.close()

   try:

       decode(saveCode)  # decode the base64

       for x in decoded:

           if x == "|":

               saveList.append(saved)

               saved = ""

           else:

               saved += x

       if saveList[0] == "turtleyturtle":  # check if it is a turtleyturtle save code

           unlockedSkins = []

           pointSum = int(saveList[1])

           currentSkin = saveList[2]

           turt.shape(saveList[2] + ".png")

           for x in saveList[3:]:

               unlockedSkins.append(x)

           print("save loaded succesfully!")

       else:

           print("error: not a valid save code!")

   except Exception as e:

       print("there was an error with the save code")


# check if saves

saveFile = open("save", "r")

code = saveFile.read()

code = code.rstrip()

if code != "":  # skip if empty

   openData(code)

saveFile.close()

previousWindows = []


def flapClick(x, y):

   global grav

   global start

   global currentWindow

   global shopPage

   global currentSkin

   global pointSum

   global buyOn

   global previousWindows

   # costs for skins

   global costOfRock

   global costOfSub

   global costOfTorpedo

   global costOfPizza

   global costOfMoonlander

   global costOfTimeMachine

   global costOfUrchin

   global costOfOtter

   if currentWindow == "game":

       if start == False:

           if looseSeq == False:

               reset()

               start = True

       elif (x > -190) and (y > -215) and (x < -89) and (y < -174):

           abilityOnKey()

       else:

           y = turt.ycor()

           grav = 0

           turt.sety(y + flapS)

   elif currentWindow == "game over":

       # buttons for loose screen

       if (x > -78) and (y > -19) and (x < 79) and (y < 1):

           previousGames()  # see previous games

           previousWindows.append("previousGames")

       elif (x > -72) and (y > -48) and (x < 74) and (y < -30):

           customize()  # customize turtle, bakcground, and more

           previousWindows.append("customize")

       elif (x > -43) and (y > -83) and (x < 44) and (y < -56):

           options()  # options window

           previousWindows.append("options")

       elif (x > -29) and (y > -144) and (x < 28) and (y < -97):

           win.bye()

       else:

           if looseSeq == False:

               reset()

               start = True

   elif currentWindow == "escape":

       if (x > -73) and (y > 93) and (x < 67) and (y < 115):

           options()  # options window

           previousWindows.append("options")

       if (x > -67) and (y > 42) and (x < 59) and (y < 65):

           currentWindow = "game"

           start = True

           disableFlap = False

           turt.showturtle()

           pearl.showturtle()

       if (x > -46) and (y > 0) and (x < 35) and (y < 19):

           win.bye()

       else:

           pass

   elif currentWindow == "shop":

       if (x > -190) and (y > -225) and (x < -150) and (y < -155):

           # if shop page is not on index 0

           if shopPage != 0:

               shopPage -= 1

               shopPageUpdate()

       elif (x > 150) and (y > -225) and (x < 190) and (y < -155):

           # if shop page is not on index 1

           if shopPage != 2:

               shopPage += 1

               shopPageUpdate()

       elif shopPage == 0:

           if (x > -189) and (y > -145) and (x < -70) and (y < -26):

               turt.shape("turtle")

               win.update()

               currentSkin = "turtle"

               display2.clear()

           elif (x > -59) and (y > -146) and (x < 61) and (y < -26):

               shopBuy("rock", costOfRock)

           elif (x > 71) and (y > -144) and (x < 190) and (y < -26):

               shopBuy("sub", costOfSub)

           elif buyOn == True:

               if (x < 36) and (y > -202) and (x > -36) and (y < -178):

                   doBuy()

           else:

               reset()

               start = True

       elif shopPage == 1:

           if (x > -189) and (y > -145) and (x < -70) and (y < -26):

               shopBuy("torpedo", costOfTorpedo)

           elif (x > -59) and (y > -146) and (x < 61) and (y < -26):

               shopBuy("pizza", costOfPizza)

           elif (x > 71) and (y > -144) and (x < 190) and (y < -26):

               shopBuy("moonlander", costOfMoonlander)

           elif buyOn == True:

               if (x < 36) and (y > -202) and (x > -36) and (y < -178):

                   doBuy()

       elif shopPage == 2:

           if (x > -189) and (y > -145) and (x < -70) and (y < -26):

               shopBuy("time-machine", costOfTimeMachine)

           elif (x > -59) and (y > -146) and (x < 61) and (y < -26):

               shopBuy("urchin", costOfUrchin)

           elif (x > 71) and (y > -144) and (x < 190) and (y < -26):

               shopBuy("otter", costOfOtter)

           elif buyOn == True:

               if (x < 36) and (y > -202) and (x > -36) and (y < -178):

                   doBuy()

           else:

               reset()

               start = True

       else:

           print("error: shop page does not exist!")

   elif currentWindow == "options":

       if (x > -54) and (y > 121) and (x < 55) and (y < 150):

           print("save code:")

           saveData()

       elif (x > -54) and (y > 74) and (x < 55) and (y < 105):

           saveCode = input("enter save code here: ")

           openData(saveCode)

       else:

           reset()

           start = True

   else:

       print("error: window does not exist!")


def escape():

   global currentWindow

   global previousWindows

   global start

   global disableFlap

   if currentWindow != "game" and currentWindow != "escape":

       try:

           previousWindow = previousWindows[len(previousWindows) - 2]

           del previousWindows[len(previousWindows) - 1]

           function = globals()[previousWindow]

           function()

       except Exception as e:

           print(e)

   elif currentWindow == "game":

       currentWindow = "escape"

       previousWindows.append("escape")

       start = False

       disableFlap = True

       time.sleep(0.1)

       win.bgpic("menu.png")

       turt.hideturtle()

       bg.clear()

       bg2.clear()

       fg.clear()

       fg2.clear()

       pole1.clear()

       pole2.clear()

       score.clear()

       pearl.hideturtle()

   else:

       currentWindow = "game"

       start = True

       disableFlap = False

       turt.showturtle()

       pearl.showturtle()


# bounding box for first pole

def pole1Bound():

   global poleGap

   x = pole1.xcor()

   y = pole1.ycor()

   x1 = turt.xcor()

   y1 = turt.ycor()

   if (y1 + 9) > (y + poleGap) and (x1 + 9) > (x - 15) and (x1 + 9) < (x + 15):

       loose()

   if (y1 - 9) < (y - poleGap) and (x1 + 9) > (x - 15) and (x1 + 9) < (x + 15):

       loose()


# bounding box for second pole

def pole2Bound():

   x = pole2.xcor()

   y = pole2.ycor()

   x1 = turt.xcor()

   y1 = turt.ycor()

   if (y1 + 9) > (y + poleGap) and (x1 + 9) > (x - 15) and (x1 + 9) < (x + 15):

       loose()

   if (y1 - 9) < (y - poleGap) and (x1 + 9) > (x - 15) and (x1 + 9) < (x + 15):

       loose()


# floor

floorCheckEnabled = True


def floorCheck():

   global floorCheckEnabled

   global grav

   y = turt.ycor()

   if floorCheckEnabled:

       if y < -210:

           loose()

       if y > 230:

           loose()

   else:

       if y < -210:

           turt.sety(y + grav + 30)

           grav = 0


difLevel = 0

# increase difficulty level

def dif():

   global s

   global points

   global difLevel

   global difIncrease

   if difLevel >= 5:

       s = s + difIncrease

       difLevel = 0


abilityOn = False  # whether the ability is on or not

abilityT = 0  # for triggering reset only the first time ability has been deactivated

storePoints = 0  # stores points when ability goes on cooldown


def abilityCooldown():

   global points

   global storePoints

   storePoints = points  # storing point value


# key function for toggling ability

def abilityOnKey():

   global abilityOn

   global storePoints

   global points

   global cooldownLength

   if points >= (

       storePoints + cooldownLength

   ):  # must gain cooldownLength more points from when the point value was stored

       if abilityOn:  # toggle off ability

           abilityOn = False

       else:  # toggle on ability

           abilityOn = True


def AutoPilot():

   global abilityOn

   global randomDecay

   global decayRate

   x = turt.xcor()

   y = turt.ycor()

   pole1x = pole1.xcor()

   pole1y = pole1.ycor()

   pole2x = pole2.xcor()

   pole2y = pole2.ycor()

   if ((pole1x < pole2x) and (pole1x + 15 >= x)) or (

       (pole2x < pole1x) and (pole2x + 15 <= x)

   ):

       if not (y > (pole1y - 15) and y < (pole1y + 15)):

           if y > pole1y + 15:  # if above gap

               1 == 1

           elif y < pole1y - 15:  # if below gap

               flap()

       else:

           if y <= pole1y - 30:

               flap()

   else:

       if not (y > (pole2y - 15) and y < (pole2y + 15)):

           if y > pole2y + 15:  # if above gap

               1 == 1

           elif y < pole2y - 15:  # if below gap

               flap()

       else:

           if y <= pole2y - 30:

               flap()

   if randomDecay < decayRate and abilityOn == True:

       abilityCooldown()

       abilityOn = False


def magnet():

   global abilityOn

   global randomDecay

   global decayRate

   # pearl coordinates

   pearlX = pearl.xcor()

   pearlY = pearl.ycor()

   # player coordinates

   turtX = turt.xcor()

   turtY = turt.ycor()

   # range of effect

   dist = 150

   # if turtle is in magnet range

   if ((turtX > (pearlX - dist)) and (turtX < (pearlX + dist))) and (

       (turtY > (pearlY - dist)) and (turtY < (pearlY + dist))

   ):

       # distance from point a to point b

       D = math.sqrt(((turtX - pearlX) ** 2) + ((turtY - pearlY) ** 2))

       # distance curve

       d = 3 + (100 / (D * 2)) ** 2

       # what coordinate to go to

       xCoord = pearlX + ((d / D) * (turtX - pearlX))

       yCoord = pearlY + ((d / D) * (turtY - pearlY))

       # move to coordinate

       pearl.goto(xCoord, yCoord)

   if randomDecay < decayRate and abilityOn == True:

       abilityCooldown()

       abilityOn = False


disableFlap = False

# abilities for each skin

def ability():

   global grav

   global gravInc

   global s

   global speed

   global currentSkin

   global abilityOn

   global abilityT

   global storePoints

   global points

   global randomDecay

   global gravityConst

   global gravityIncrease

   global flapS

   global disableFlap

   global floorCheckEnabled

   y = turt.ycor()

   x = turt.xcor()

   pole1X = pole1.xcor()

   pole2X = pole2.xcor()

   # rock ability; increase gravity to make rock heavier

   if currentSkin == "rock":

       if abilityOn:

           if abilityT == 0:

               grav = 8

               abilityT = 1

               disableFlap = True

       else:

           if abilityT == 1:

               grav = gravityConst

               abilityCooldown()

               abilityT = 0

               disableFlap = False

   # sub ability; destroy pillar in front

   elif currentSkin == "sub":

       if abilityOn:

           if pole1X < pole2X and x < pole1X - 15:

               pole1.goto(pole1X + 410, random.randint(-150, 150))

           elif pole2X < pole1X and x < pole2X - 15:

               pole2.goto(pole2X + 410, random.randint(-150, 150))

           else:

               pole1.goto(pole1X + 410, random.randint(-150, 150))

           abilityOn = False

           abilityCooldown()

   # torpedo ability; stay locked in one plane of movement

   elif currentSkin == "torpedo":

       if abilityOn:

           if abilityT == 0:

               grav = 0

               gravInc = 0

               abilityT = 1

               disableFlap = True

       elif abilityT == 1:

           grav = gravityConst

           gravInc = gravityIncrease

           abilityCooldown()

           abilityT = 0

           disableFlap = False

   # pizza ability; autopilot

   elif currentSkin == "pizza":

       if abilityOn:

           randomDecay = random.randint(0, 750)

           AutoPilot()

   # moonlander ability; make gravity reverse

   elif currentSkin == "moonlander":

       if abilityOn:

           if abilityT == 0:

               flapS = -flapHeight

               grav = -gravityConst

               gravInc = -gravityIncrease

               abilityT = 1

       else:

           if abilityT == 1:

               flapS = flapHeight

               grav = gravityConst

               gravInc = gravityIncrease

               abilityCooldown()

               abilityT = 0

   # time machine ability; slow down pole movment speed

   elif currentSkin == "time-machine":

       if abilityOn:

           s = speed * 0.75

           randomDecay = random.randint(0, 750)

           abilityT = 1

       else:

           if abilityT == 1:

               s = speed

               abilityCooldown()

               abilityT = 0

       if randomDecay < decayRate and abilityOn == True:

           abilityCooldown()

           abilityOn = False

   # sea urchin ability; bounce along the floor

   elif currentSkin == "urchin":

       if abilityOn:

           floorCheckEnabled = False

           abilityT = 1

           randomDecay = random.randint(0, 2000)

       else:

           if abilityT == 1:

               floorCheckEnabled = True

               abilityCooldown()

               abilityT = 0

       if randomDecay < decayRate and abilityOn == True:

           abilityCooldown()

           abilityOn = False

   # golden otter ability; attract pearls

   elif currentSkin == "otter":

       if abilityOn:

           randomDecay = random.randint(0, 1000)

           magnet()


# ability charge bar

chargeBar = turtle.Turtle()

chargeBar.penup()

chargeBar.shape("charge_empty.png")

chargeBar.left(90)

chargeBar.hideturtle()


def charge():

   global storePoints

   global points

   global cooldownLength

   global currentSkin

   if points >= storePoints + cooldownLength:

       chargeBar.shape("charge_full.png")

   elif points - (storePoints + cooldownLength) == -1:

       chargeBar.shape("charge_2.png")

   elif points - (storePoints + cooldownLength) == -2:

       chargeBar.shape("charge_1.png")

   else:

       chargeBar.shape("charge_empty.png")


# keybinds

win.listen()

win.onkey(flap, flapKey)

win.onkey(abilityOnKey, abilityKey)

win.onkey(escape, "escape")

win.onscreenclick(flapClick)

# game loop

while running:

   if start == True:

       gravity()  # start by enacting gravity

       current()  # write in current patches

       ability()  # do ability

       bgMove()  # move the background

       pole()  # move the poles

       pearlMove()  # move the pearls

       fgMove()  # move the foreground

       pole1Bound()  # check the boundries of pole 1

       pole2Bound()  # check the boundries of pole 2

       floorCheck()  # check if player has hit floor, or reached height limit

       point()  # calculate points

       scoreDisplay()  # write the score

       dif()  # check if difficulty should be increased

       charge()  # changes charge bar besed on ability cooldown

   win.update()  # update the window
