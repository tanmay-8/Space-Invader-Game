import random
from time import sleep
from turtle import Screen, onkey, onkeypress
from Invader import Invader
from player import Player
from bullet import Bullet
from scoreboard import ScoreBoard
from pygame import mixer
import pygame

POSITIONS = [[-200, 240], [-200, 180], [-200, 120], [-150, 240], [-150, 180], [-150, 120],  [-90, 240], [-90, 180], [-90, 120], [-30, 240], [-30, 180], [-30, 120], [30, 240], [30, 180], [30, 120], [90, 240], [90, 180], [90, 120], [150, 240], [150, 180], [150, 120], [200, 240], [200, 180], [200, 120]]


movedown  = 0.1
movehor = 0.1

def createbullet():
    global bullets,player
    bullets.append(Bullet(player.xcor()))
    FIRE.play()

def createInvaders():
    global invaders
    num_of_invaders = random.randint(16,24)
    chosen_ones = random.choices(POSITIONS,[1 for i in POSITIONS],k=num_of_invaders)
    invaders = []
    for i in chosen_ones:
        invader = Invader((i[0],i[1]),movedown,movehor)
        invaders.append(invader)

def refreshinvaders():
    global invaders
    for i in invaders:
        i.goto(1000,1000)
    invaders.clear()
    createInvaders()


pygame.init()


DESTROYED_MUSIC = mixer.Sound(r"D:\CODING\100 Day Python Course\Day81-100\_14_P_spaceinvaders\explosion.wav")
FIRE = mixer.Sound(r"D:\CODING\100 Day Python Course\Day81-100\_14_P_spaceinvaders\shoot.wav")
INVADER_KILLED = mixer.Sound(r"D:\CODING\100 Day Python Course\Day81-100\_14_P_spaceinvaders\invaderkilled.wav")

screen =  Screen()
screen.setup(width=450,height=550)
screen.title("Space Invaders")
screen.bgcolor("black")
screen.bgpic(r"D:\CODING\100 Day Python Course\Day81-100\_14_P_spaceinvaders\bg.gif")
screen.tracer(0)
sb = ScoreBoard()

player = Player()

invaders = []
bullets = []
createInvaders()

mixer.music.load(r'D:\CODING\100 Day Python Course\Day81-100\_14_P_spaceinvaders\bg.mp3')
mixer.music.play(-1)
is_gameOn = True
while is_gameOn:
    screen.update()
    screen.listen()

    onkey(createbullet,"space")
    onkeypress(player.toleft,"Left")
    onkeypress(player.toright,"Right")

    for i in bullets:
        i.move()
    
    if(len(invaders)==0):
        movedown += 0.1
        movehor += 0.1
        sleep(1)
        createInvaders()

    for i in bullets:
        if(i.ycor()>=275):
            i.destroy()
            bullets.remove(i)
        
        for invader in invaders:
            if(i.distance(invader)<=20):
                i.destroy()
                try:
                    bullets.remove(i)
                except:
                    None
                invaders.remove(invader)
                invader.destroy()
                INVADER_KILLED.play()
                sb.increase()

    for i in invaders:    
        if(i.ycor()>=-200):
            i.todown()
            i.random()
        if(i.xcor()>=210 or i.xcor()<=-210):
            i.bouncex()
        if(i.ycor()<=-200):
            sb.gameover()
            DESTROYED_MUSIC.play()
            is_gameOn=False
            what = screen.textinput("GAME OVER","Enter q to quit c to continue")
            if(what.lower()=="q"):
                quit()
            else:
                refreshinvaders()
                sb.refreshscoreboard()
                movedown = 0.1
                movehor  = 0.1
                is_gameOn = True


screen.exitonclick()