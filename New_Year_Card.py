#coding=utf-8
import turtle
import random
import time
from turtle import *
from random import *
import PyQt5.sip


# set the background color for the page
import time
import pygame

file='media/Music_1.mp3'
pygame.mixer.init()  #把mp3初始化出来
#print("播放音乐1")

track = pygame.mixer.music.load(file)

pygame.mixer.music.play()
#time.sleep(60)

#tommy.reset()

bg = turtle.Screen()
bg.bgcolor("black")

tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(1)

tommy.penup()
tommy.goto(-250,0)
tommy.color("orange")
tommy.write("插上耳机后观看哦",font=('微软雅黑', 25, 'normal'))

time.sleep(4)
tommy.clear()

x = -300
y = 250
tommy.goto(x,y)
tommy.color("pink")

pygame.mixer.music.stop()
file='media/Music_2.mp3'
# pygame.mixer.init()  #把mp3初始化出来
#print("播放音乐2")
track = pygame.mixer.music.load(file)
pygame.mixer.music.play()

time.sleep(3)

tommy.penup()
tommy.goto(x+150,y-75-25-25-25-25-25-25-25-25-25-50-25)  #每次减25
tommy.write(" φ(゜▽゜*)♪  HAPPY NEW YEAR!",font=('微软雅黑', 15, 'normal'))
time.sleep(3)


# tommy.clear()
#
#
# tommy.pensize(6)
# # draw lines
# tommy.penup()
# tommy.goto(-190, -180)
# tommy.color("yellow")
# tommy.pensize(6)
# tommy.pendown()
# tommy.goto(190,-180)
# tommy.penup()
#
# tommy.penup()
# tommy.goto(-160, -150)
# tommy.color("purple")
# tommy.pensize(6)
# tommy.pendown()
# tommy.goto(160,-150)
# tommy.penup()
#
# tommy.penup()
# tommy.goto(-130, -120)
# tommy.color("teal")
# tommy.pensize(6)
# tommy.pendown()
# tommy.goto(130,-120)
# tommy.penup()
#
# # draw cake
# tommy.goto(-74,-110)   #这个是画蛋糕
# tommy.begin_fill()
# tommy.pendown()
# tommy.color("white")
# tommy.goto(50,-110)
# tommy.left(90)
# tommy.forward(60)
# tommy.left(90)
# tommy.forward(125)
# tommy.left(90)
# tommy.forward(60)
# tommy.end_fill()
# tommy.penup()
#
#
# tommy.goto(-74,-110)   #这个是画蛋糕，到这个坐标去,这个是黄色那层
# tommy.begin_fill()
# tommy.pendown()   #放下画笔
# tommy.color("yellow")
# tommy.goto(50,-110)
# tommy.left(90)
# #tommy.forward(60) #向前60码，这个是那个横线
# tommy.left(90)
# tommy.forward(45)  #这个是一层的厚度
# tommy.left(90)  #这个是根据角度来转方像
# tommy.forward(125)
# tommy.left(90)  #这个是根据角度来转方像
# tommy.forward(45)
# tommy.end_fill()
# tommy.penup()
#
# tommy.goto(-74,-110)   #这个是画蛋糕，到这个坐标去,这个是黄色那层
# tommy.begin_fill()
# tommy.pendown()   #放下画笔
# tommy.color("#40E0D0")
# tommy.goto(50,-110)
# tommy.left(90)
# #tommy.forward(60) #向前60码，这个是那个横线
# tommy.left(90)
# tommy.forward(30)  #这个是一层的厚度
# tommy.left(90)  #这个是根据角度来转方像
# tommy.forward(125)
# tommy.left(90)  #这个是根据角度来转方像
# tommy.forward(30)
# tommy.end_fill()
# tommy.penup()
#
#
# tommy.goto(-74,-110)   #这个是画蛋糕，到这个坐标去,最下面那层
# tommy.begin_fill()
# tommy.pendown()   #放下画笔
# tommy.color("#BA55D3")
# tommy.goto(50,-110)
# tommy.left(90)
# #tommy.forward(60) #向前60码，这个是那个横线
# tommy.left(90)
# tommy.forward(15)  #这个是一层的厚度
# tommy.left(90)  #这个是根据角度来转方像
# tommy.forward(125)
# tommy.left(90)  #这个是根据角度来转方像
# tommy.forward(15)
# tommy.end_fill()
# tommy.penup()
#
# #draw candles
# tommy.goto(-60, -40)
# tommy.color("aquamarine")
# tommy.pendown()
# tommy.pensize(3)
# tommy.goto(-60, -20)
# tommy.penup()
#
# tommy.goto(-40, -40)
# tommy.color("yellow")
# tommy.pendown()
# tommy.pensize(3)
# tommy.goto(-40, -20)
# tommy.penup()
#
# tommy.goto(-20, -40)
# tommy.color("green")
# tommy.pendown()
# tommy.pensize(3)
# tommy.goto(-20, -20)
# tommy.penup()
#
# tommy.goto(0, -40)
# tommy.color("red")
# tommy.pendown()
# tommy.pensize(3)
# tommy.goto(0, -20)
# tommy.penup()
#
# tommy.goto(20, -40)
# tommy.color("blue")
# tommy.pendown()
# tommy.pensize(3)
# tommy.goto(20, -20)
# tommy.penup()
#
#
# tommy.goto(40, -40)
# tommy.color("#556B2F")
# tommy.pendown()
# tommy.pensize(3)
# tommy.goto(40, -20)
# tommy.penup()

# print message



# bg.bgcolor("pink")


def snow():
    tommy.hideturtle()
    tommy.speed(100)
    tommy.pensize(2)
    for i in range(100):
        r=random()
        g=random()
        b=random()
        tommy.pencolor(r,g,b)
        tommy.penup()
        tommy.setx(randint(-350,350))
        tommy.sety(randint(1,270))
        tommy.pendown()
        dens=randint(8,12)
        snowsize=randint(10,14)
        for j in range(dens):
            tommy.forward(snowsize)
            tommy.backward(snowsize)
            tommy.right(360/dens)



snow()

tommy.goto(-250, 90)
tommy.color("orange")
tommy.pendown()
tommy.write( "漫天 ｡･ﾟ･(ﾉД`)ヽ(ﾟДﾟ ) 烟花送给你~",font=('微软雅黑', 24, 'normal'))

# pygame.mixer.music.stop()
# file='media/Music_3.mp3'
# print("播放音乐3")
# track = pygame.mixer.music.load(file)
# pygame.mixer.music.play()

time.sleep(3)


tommy.penup()
tommy.goto(-250,-250)
tommy.write("新年快乐！",font=('微软雅黑', 24, 'normal'))

time.sleep(4)



# send the turtle to the corner


tommy.penup()
tommy.goto(-250, 250)


#tommy.exitonclick()
tommy.hideturtle()

time.sleep(4)
tommy.clear()  #清空屏幕了,然后设置背景色为黑色，滚动演员表


bg.bgcolor("white")

tommy.penup()
tommy.goto(-300, 90)
tommy.color("black")
tommy.pendown()
# tommy.write(" …(⊙_⊙;)…天呐！是不是很好看呀？坚持看到了这里",font=('微软雅黑', 24, 'normal'))
tommy.penup()
tommy.goto(-300, 60)
# tommy.write(" （〃｀ 3′〃）那好咯，后面还有一点点结尾！",font=('微软雅黑', 24, 'normal'))
tommy.penup()


# time.sleep(4)
# tommy.goto(-250, 90)
# tommy.clear()
# tommy.write("（Python支持）就是我 \n[手动狗头]",font=('微软雅黑', 24, 'normal'))
# time.sleep(4)

# tommy.clear()
# tommy.write("音乐 、后期、导演、声优、编辑、构思 ",font=('微软雅黑', 24, 'normal'))
# time.sleep(4)
#
# tommy.clear()
# tommy.write("♂ 是你那不善言辞的大猪蹄子男票 ",font=('微软雅黑', 24, 'normal'))
# time.sleep(4)
#

tommy.goto(-180, 90)
tommy.clear()
tommy.write("(◍•ᴗ•◍)ゝ特用此小程序祝\n 2021新年快乐 ",font=('微软雅黑', 24, 'normal'))
time.sleep(3)

tommy.clear()
tommy.write("(　◜◡‾) 万事顺利~ ☻ ",font=('微软雅黑', 24, 'normal'))
time.sleep(3)






# tommy.clear()
# tommy.write("最后biu 一个小心心给你把~",font=('微软雅黑', 24, 'normal'))
# time.sleep(3)

#这儿最后画一个小心心，

tommy.clear()
#coding=utf-8
#画一个圆的东西出来
import turtle

#turtle = tommy
turtle.speed(1)

turtle.pensize(6)#：设置画笔的宽度；
turtle.left(30)
turtle.circle(90,300)  #半径大小
#画眼睛

turtle.right(100)
turtle.forward(60)
turtle.left(150)
turtle.forward(55)
turtle.right(110)
turtle.forward(40)
turtle.penup()
turtle.goto(-15,90)
#画眼睛了
turtle.begin_fill()
turtle.color("black")
turtle.circle(8)
turtle.end_fill()


turtle.penup()
turtle.goto(-75,90)
#画眼睛了
turtle.begin_fill()
turtle.color("black")
turtle.circle(8)
turtle.end_fill()

# turtle.penup()
# turtle.goto(0,70)
# #画眼睛了
# turtle.begin_fill()
# turtle.color("red")
# turtle.circle(8)
# turtle.end_fill()
#
# turtle.penup()
# turtle.goto(-85,70)
# #画眼睛了
# turtle.begin_fill()
# turtle.color("red")
# turtle.circle(8)
# turtle.end_fill()

turtle.penup()
turtle.goto(-50,50)
#画眼睛了
# turtle.begin_fill()
turtle.pendown()
turtle.color("black")
turtle.left(45)
turtle.circle(20,90)
# turtle.end_fill()

#画另一只手
turtle.penup()
turtle.color("black")
turtle.goto(0,0)
turtle.right(35)
turtle.pendown()
turtle.forward(75)

turtle.left(85)
turtle.forward(25)
turtle.right(165)
turtle.forward(25)
turtle.left(90)
turtle.forward(35)
turtle.right(155)
turtle.forward(35)


turtle.left(75)
turtle.forward(20)
turtle.right(85)
turtle.forward(20)
turtle.right(85)
turtle.forward(25)


turtle.left(70)
turtle.forward(35)
turtle.left(15)
turtle.forward(20)

turtle.left(60)
turtle.forward(40)


# #爱心
# # turtle.begin_fill()
# turtle.penup()
# turtle.color("red")
# turtle.right(180)
# turtle.goto(135,135)
# turtle.pendown()
# turtle.circle(20,170)
# turtle.forward(15)
# turtle.left(45)
#
# turtle.forward(55)
#
# turtle.penup()
# turtle.color("red")
# turtle.right(250)
# turtle.goto(135,135)
# turtle.pendown()
# turtle.circle(-20,170)
# turtle.forward(15)
# turtle.right(45)
#
# turtle.forward(55)
#
# # turtle.end_fill()
#
# turtle.penup()
# turtle.goto(135,135)
# turtle.pendown()
# # turtle.right(90)
# turtle.forward(45)
# turtle.left(160)
# turtle.forward(75)
# turtle.right(160)
# turtle.forward(55)
# turtle.goto(135,100)

turtle.penup()
turtle.goto(-120,185)
turtle.write("你是这个 [Thumb Up]",font=("微软雅黑",24,"normal"))
time.sleep(4)

tommy.goto(-220, -150)
tommy.clear()
tommy.write("（Python支持）就是我 \n[手动狗头] 你猜我是谁 :)",font=('微软雅黑', 24, 'normal'))
time.sleep(4)

turtle.goto(120,-220)
turtle.write("The end",font=("微软雅黑",24,"normal"))
time.sleep(4)

done() #可以使窗口保持

pygame.mixer.music.stop()