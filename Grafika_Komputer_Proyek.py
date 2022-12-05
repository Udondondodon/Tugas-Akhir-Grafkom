import OpenGL.GLUT as glut
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random

#Position awal pesawat
x_body = 0
y_body = 0

pos_x_tombol = 0
pos_y_tombol = 200

tingkatLevel = 1
kecepatan = 5

point = 0

x_poin = 2000
y_poin = 0

gameMulai = False
gameOver = False

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1280, 1280, 0, 700)

def Matahari(xn,yn,sugmentyn):
    glPushMatrix()
    # glScale(0.5,0.5,0)
    glColor3ub(255,230,0)
    glBegin(GL_POLYGON)
    for i in range(sugmentyn):
        theta= 2 *3.1415926*i/sugmentyn
        x = 180* math.cos(theta)
        y = 50* math.sin(theta)
        glVertex2f(x + xn, y + yn)
    glEnd()
    glPopMatrix()
    
def drawText(text,xpos,ypos,r,g,b):
    glPushMatrix()
    glColor3ub(r,g,b)
    fontStyle = glut.GLUT_BITMAP_TIMES_ROMAN_24
    glRasterPos2i(xpos,ypos)
    for i in str(text):
        c = ord(i)
        glutBitmapCharacter(fontStyle, c)
    glPopMatrix()
    
def collision():
    global x_body, y_body, x_poin, y_poin, gameMulai, kecepatan, point, tingkatLevel
    x_body += kecepatan

def collision():
    global x_body, y_body, x_poin, y_poin, gameMulai, kecepatan, point
    x_body += kecepatan
    print(y_body, y_poin)
    
    if x_body-300 >= x_poin:
        if y_body+40 >= y_poin >= y_body-40:
            x_body = 0
            y_poin = random.randint(-680,100)
            point += 1
    if x_body-70 >= x_poin:
        if y_body+40 >= y_poin >= y_body-40:
            x_body = 0
            y_poin = random.randint(-680,100)
            point += 1
    if point == 2:
        point = 0
        kecepatan += 1
        tingkatLevel +=1

    if x_body >= 2400:
        gameMulai = False
        x_body = 0
        kecepatan = 5
        tingkatLevel = 1

def poin():
    global x_poin, y_poin
    glPushMatrix()
    glScale(1.0,0.3,0)
    glTranslated(x_poin,y_poin,0)
    glTranslatef(0,1000,0)
    glBegin(GL_QUADS)
    glColor3ub(255,0,47)
    glVertex2f(-1000,0)
    glVertex2f(-1000,55)
    glVertex2f(-1055,55)
    glVertex2f(-1055,0)
    glEnd()
    glPopMatrix() 

def tombolPlay():
    # global pos_x_tombol, pos_y_tombol
    glPushMatrix()
    glColor3ub(41, 184, 255)
    glTranslated(0,-50,0)
    
    # glBegin(GL_POLYGON)
    # glVertex2f(-100,50)
    # glVertex2f(-100,0)
    # glVertex2f(100,0)
    # glVertex2f(100,50)
    
    #kotakBelakang
    glBegin(GL_POLYGON)
    glVertex2f(-700,180)#d1
    glVertex2f(-700,320)#e1
    glVertex2f(700,320)#f1
    glVertex2f(700,180)#g1
    glEnd()
    
    #Huruf S
    # glColor3ub(0,0,0)
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(-616,193)#g
    glVertex2f(-614,227)#f
    glVertex2f(-372,220)#e
    glVertex2f(-300,200)#h
    glEnd()
    # glColor3ub(0,0,0)
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(-372,220)#e
    glVertex2f(-300,200)#h
    glVertex2f(-309,262)#i
    glVertex2f(-376,244)#d
    glEnd()
    # glColor3ub(0,0,0)
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(-572,241)#c
    glVertex2f(-376,244)#d
    glVertex2f(-309,262)#i
    glVertex2f(-505,260)#j
    glEnd()
    # glColor3ub(0,0,0)
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(-572,241)#c
    glVertex2f(-505,260)#j
    glVertex2f(-512,278)#k
    glVertex2f(-548,297)#a
    glVertex2f(-597,277)#b
    glEnd()
    # glColor3ub(0,0,0)
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(-548,297)#a
    glVertex2f(-300,300)#m
    glVertex2f(-275,280)#l
    glVertex2f(-512,278)#k
    glEnd()
    
    #Huruf P
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(-242,297)#n
    glVertex2f(-265,200)#o
    glVertex2f(-142,201)#p
    glVertex2f(-185,248)#q
    glVertex2f(-254,248)#l2
    glEnd()
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(-242,297)#n
    glVertex2f(-189,281)#h1
    glVertex2f(-188,260)#i1
    glVertex2f(-254,248)#l2
    glEnd()
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(-242,297)#n
    glVertex2f(-189,281)#h1
    glVertex2f(-115,287)#k1
    glVertex2f(-53,308)#s
    glEnd()
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(-53,308)#s
    glVertex2f(-115,287)#k1
    glVertex2f(-118,265)#j1
    glVertex2f(-66,250)#r
    glEnd()
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(-254,248)#l2
    glVertex2f(-188,260)#i1
    glVertex2f(-118,265)#j1
    glVertex2f(-66,250)#r
    glEnd()
    
    #Huruf A
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(-55,191)#u
    glVertex2f(33,190)#v
    glVertex2f(17,281)#l1
    glVertex2f(-28,292)#t
    glEnd()
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(-28,292)#t
    glVertex2f(17,281)#l1
    glVertex2f(58,283)#o1
    glVertex2f(100,300)#c1
    glEnd()
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(100,200)#a1
    glVertex2f(183,205)#b1
    glVertex2f(100,300)#c1
    glVertex2f(58,283)#o1
    glEnd()
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(20,257)#m1
    glVertex2f(70,260)#n1
    glVertex2f(76,244)#z
    glVertex2f(24,240)#w
    glEnd()
    
    #Huruf C
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(204,193)#q1
    glVertex2f(140,303)#p1
    glVertex2f(227,281)#u1
    glVertex2f(252,226)#t1
    glEnd()
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(140,303)#p1
    glVertex2f(334,307)#w1
    glVertex2f(323,272)#v1
    glVertex2f(227,281)#u1
    glEnd()
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(204,193)#q1
    glVertex2f(252,226)#t1
    glVertex2f(364,254)#s1
    glVertex2f(358,204)#r1
    glEnd()
    
    #Huruf E
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(391,193)#a2
    glVertex2f(461,219)#d2
    glVertex2f(628,236)#c2
    glVertex2f(565,193)#b2
    glEnd()
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(391,193)#a2
    glVertex2f(388,244)#m2
    glVertex2f(461,244)#e2
    glVertex2f(461,219)#d2
    glEnd()
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(388,244)#m2
    glVertex2f(461,244)#e2
    glVertex2f(456,265)#h2
    glVertex2f(386,265)#n2
    glEnd()
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(456,265)#h2
    glVertex2f(461,224)#e2
    glVertex2f(558,247)#f2
    glVertex2f(564,270)#g2
    glEnd()
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(386,265)#n2
    glVertex2f(383,306)#z1
    glVertex2f(448,287)#i2
    glVertex2f(456,265)#h2
    glEnd()
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(383,306)#z1
    glVertex2f(448,287)#i2
    glVertex2f(565,283)#j2
    glVertex2f(621,304)#k2
    glEnd()
    
    glPopMatrix() 

def bodyAir(cx,cy,num_segment):
    glPushMatrix()
    glScale(1.0,0.3,0)
    global y_body, x_body, kecepatan, game_over
    glTranslatef(-1200,1000,0)
    glTranslated(x_body, y_body, 0)
        
    #Body Pesawat
    glColor3ub(240,240,240)
    # glLineWidth(3)
    glBegin(GL_POLYGON)
    for i in range(num_segment):
        theta= 2 *3.1415926*i/num_segment
        x = 6* math.cos(theta)
        y = 6 * math.sin(theta)
        glVertex2f(x + cx, y + cy)
    glEnd()
    
    #Body Pesawat
    glColor3ub(240,240,240)
    glBegin(GL_POLYGON)
    glVertex2f(77,5)#l
    glVertex2f(80,16)#c
    glVertex2f(50,40)#d
    glVertex2f(-100,40)#n
    glColor3ub(240,0,0)
    glVertex2f(-115,5)#k
    glEnd()
    glColor3ub(240,240,240)
    glBegin(GL_POLYGON)
    glVertex2f(-100,40)#n
    glColor3ub(240,0,0)
    glVertex2f(-120,80)#f
    glVertex2f(-140,80)#g
    glVertex2f(-140,35)#h
    glVertex2f(-130,25)#i
    glVertex2f(-140,25)#j
    glVertex2f(-140,15)#m
    glVertex2f(-115,5)#k
    glEnd()
    
    #Body Sayap Depan Pesawat
    glColor3ub(240,240,240)
    glBegin(GL_POLYGON)
    glVertex2f(20,10)#e
    glVertex2f(-15,10)#o
    glVertex2f(-50,-20)#q
    glVertex2f(-75,-25)#r
    glColor3ub(240,0,0)
    glVertex2f(-20,-25)#s
    glEnd()
    #Body Sayap Belakang Pesawat
    glColor3ub(240,240,240)
    glBegin(GL_POLYGON)
    glVertex2f(-80,10)#t
    glVertex2f(-110,10)#u
    glVertex2f(-140,-10)#v
    glColor3ub(240,0,0)
    glVertex2f(-110,-10)#w
    glEnd()
    
    #Cendela Pesawat Pilot
    glColor3ub(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(65,28)#z
    glVertex2f(57,34)#a1
    glVertex2f(42,34)#b1
    glVertex2f(42,28)#c1
    glEnd()
    
    #Pintu Pesawat Depan
    glColor3ub(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(36,36)#p
    glVertex2f(36,22)#d1
    glVertex2f(28,22)#e1
    glVertex2f(28,36)#f1
    glEnd()
    
    #Pintu Pesawat Belakang
    glColor3ub(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(-36,22)#g2
    glVertex2f(-36,36)#h2
    glVertex2f(-44,36)#i2
    glVertex2f(-44,22)#j2
    glEnd()
    
    #Cendela penumpang Pesawat
    glColor3ub(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(24,30)#h1
    glVertex2f(24,34)#g1
    glVertex2f(20,34)#j1
    glVertex2f(20,30)#i1
    glEnd()
    glColor3ub(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(14,30)#k1
    glVertex2f(14,34)#l1
    glVertex2f(10,34)#m1
    glVertex2f(10,30)#n1
    glEnd()
    glColor3ub(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(4,30)#o1
    glVertex2f(4,34)#p1
    glVertex2f(0,34)#q1
    glVertex2f(0,30)#r1
    glEnd()
    glColor3ub(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(-6,30)#s1
    glVertex2f(-6,34)#t1
    glVertex2f(-10,34)#u1
    glVertex2f(-10,30)#v1
    glEnd()
    glColor3ub(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(-16,30)#w1
    glVertex2f(-16,34)#z1
    glVertex2f(-20,34)#a2
    glVertex2f(-20,30)#b2
    glEnd()
    glColor3ub(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(-26,30)#c2
    glVertex2f(-26,34)#d2
    glVertex2f(-30,34)#e2
    glVertex2f(-30,30)#f2
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-48,30)#k2
    glVertex2f(-48,34)#l2
    glVertex2f(-52,34)#m2
    glVertex2f(-52,30)#n2
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-58,30)#o2
    glVertex2f(-58,34)#p2
    glVertex2f(-62,34)#q2
    glVertex2f(-62,30)#r2
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-68,30)#s2
    glVertex2f(-68,34)#t2
    glVertex2f(-72,34)#u2
    glVertex2f(-72,30)#v2
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-78,30)#w2
    glVertex2f(-78,34)#z2
    glVertex2f(-82,34)#a3
    glVertex2f(-82,30)#b3
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-88,30)#c3
    glVertex2f(-88,34)#d3
    glVertex2f(-92,34)#e3
    glVertex2f(-92,30)#f3
    glEnd()
    glPopMatrix()

def background():
    glPushMatrix()
    glColor3ub(90, 221, 242)
    glBegin(GL_POLYGON)
    glVertex2f(-1280,0)
    glVertex2f(-1280,700)
    glVertex2f(1280,700)
    glVertex2f(1280,-0)
    glEnd()
    glPopMatrix()

def Bangunan():
    #Bangunan 3
    glPushMatrix()
    glColor3ub(131,128,128)
    glBegin(GL_POLYGON)
    glVertex2f(600,20)#e1
    glVertex2f(600,200)#a3
    glVertex2f(1000,200)#b3
    glVertex2f(1000,20)#c3
    glEnd()
    #Bangunan 2
    glColor3ub(156,156,156)
    glBegin(GL_POLYGON)
    glVertex2f(-1000,20)#e2
    glVertex2f(-1000,160)#f2
    glVertex2f(-700,160)#g2
    glVertex2f(-700,20)#h2
    glEnd()
    glColor3ub(156,156,156)
    glBegin(GL_POLYGON)
    glVertex2f(-600,20)#12
    glVertex2f(-600,200)#j2
    glVertex2f(-300,200)#k2
    glVertex2f(-300,20)#l2
    glEnd()
    glColor3ub(156,156,156)
    glBegin(GL_POLYGON)
    glVertex2f(-200,20)#m2
    glVertex2f(-200,170)#n2
    glVertex2f(100,170)#p2
    glVertex2f(100,20)#o2
    glEnd()
    glColor3ub(156,156,156)
    glBegin(GL_POLYGON)
    glVertex2f(240,20)#q2
    glVertex2f(240,170)#r2
    glVertex2f(650,170)#t2
    glVertex2f(650,20)#s2
    glEnd()
    glColor3ub(156,156,156)
    glBegin(GL_POLYGON)
    glVertex2f(800,20)#u2
    glVertex2f(800,180)#w2
    glVertex2f(1100,180)#z2
    glVertex2f(1100,20)#v2
    glEnd()
    #bangunan
    glColor3ub(217,217,217)
    glBegin(GL_POLYGON)
    glVertex2f(-1280,0)#a
    glVertex2f(-1280,20)#b
    glVertex2f(1280,20)#d
    glVertex2f(1280,0)#c
    glEnd()
    glColor3ub(92,92,92)
    glBegin(GL_POLYGON)
    glVertex2f(-800,20)#e
    glVertex2f(-800,150)#f
    glVertex2f(-500,150)#g
    glVertex2f(-500,20)#h
    glEnd()
    glColor3ub(92,92,92)
    glBegin(GL_POLYGON)
    glVertex2f(-450,20)#i
    glVertex2f(-450,100)#j
    glVertex2f(-150,100)#l
    glVertex2f(-150,20)#k
    glEnd()
    glColor3ub(92,92,92)
    glBegin(GL_POLYGON)
    glVertex2f(-100,20)#m
    glVertex2f(-100,190)#n
    glVertex2f(200,190)#p
    glVertex2f(200,20)#o
    glEnd()
    glColor3ub(92,92,92)
    glBegin(GL_POLYGON)
    glVertex2f(260,20)#w
    glVertex2f(260,150)#z
    glVertex2f(560,150)#b1
    glVertex2f(560,20)#a1
    glEnd()
    glColor3ub(92,92,92)
    glBegin(GL_POLYGON)
    glVertex2f(600,20)#e1
    glVertex2f(600,120)#f1
    glVertex2f(900,120)#h1
    glVertex2f(900,20)#g1
    glEnd()
    glColor3ub(92,92,92)
    glBegin(GL_POLYGON)
    glVertex2f(-950,20)#q1
    glVertex2f(-950,100)#r1
    glVertex2f(-1200,100)#t1
    glVertex2f(-1200,20)#s1
    glEnd()
    glColor3ub(92,92,92)
    glBegin(GL_POLYGON)
    glVertex2f(1150,20)#d3
    glVertex2f(1150,160)#e3
    glVertex2f(1300,160)#f3
    glVertex2f(1300,20)#g3
    glEnd()
    #Cendela
    glColor3ub(217,217,217)
    glBegin(GL_POLYGON)
    glVertex2f(-1150,90)#h3
    glVertex2f(-1150,40)#i3
    glVertex2f(-1100,40)#j3
    glVertex2f(-1100,90)#k3
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-1050,90)#l3
    glVertex2f(-1050,40)#m3
    glVertex2f(-1000,40)#n3
    glVertex2f(-1000,90)#o3
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-750,130)#t3
    glVertex2f(-650,130)#w3
    glVertex2f(-650,90)#v3
    glVertex2f(-750,90)#u3
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-750,40)#g4
    glVertex2f(-750,80)#d4
    glVertex2f(-650,80)#e4
    glVertex2f(-650,40)#f4
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-600,130)#z3
    glVertex2f(-550,130)#a4
    glVertex2f(-550,90)#b4
    glVertex2f(-600,90)#c4
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-600,80)#h4
    glVertex2f(-550,80)#i4
    glVertex2f(-550,40)#k4
    glVertex2f(-600,40)#j4
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-400,80)#l4
    glVertex2f(-350,80)#m4
    glVertex2f(-350,40)#n4
    glVertex2f(-400,40)#o4
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-250,80)#p4
    glVertex2f(-200,80)#q4
    glVertex2f(-200,40)#r4
    glVertex2f(-250,40)#s4
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-50,180)#t4
    glVertex2f(0,180)#u4
    glVertex2f(0,140)#v4
    glVertex2f(-50,140)#w4
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(100,180)#z4
    glVertex2f(150,180)#c5
    glVertex2f(150,140)#b5
    glVertex2f(100,140)#a5
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-50,120)#d5
    glVertex2f(0,120)#e5
    glVertex2f(0,60)#f5
    glVertex2f(-50,60)#g5
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(100,120)#h5
    glVertex2f(150,120)#i5
    glVertex2f(150,60)#j5
    glVertex2f(100,60)#k5
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(300,140)#l5
    glVertex2f(300,100)#m5
    glVertex2f(350,100)#n5
    glVertex2f(350,140)#o5
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(420,140)#p5
    glVertex2f(420,100)#q5
    glVertex2f(520,100)#r5
    glVertex2f(520,140)#s5
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(420,80)#t5
    glVertex2f(420,40)#u5
    glVertex2f(520,40)#v5
    glVertex2f(520,80)#w5
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(650,100)#z5
    glVertex2f(650,40)#a6
    glVertex2f(700,40)#b6
    glVertex2f(700,100)#c6
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(750,100)#d6
    glVertex2f(750,40)#e6
    glVertex2f(850,40)#f6
    glVertex2f(850,100)#g6
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(1300,140)#h6
    glVertex2f(1200,140)#i6
    glVertex2f(1200,100)#j6
    glVertex2f(1300,100)#k6
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(1300,80)#l6
    glVertex2f(1200,80)#m6
    glVertex2f(1200,40)#n6
    glVertex2f(1300,40)#o6
    glEnd()
    #pohon - kayu1
    glColor3ub(97,60,17)
    glBegin(GL_POLYGON)
    glVertex2f(250,20)#q
    glVertex2f(250,40)#r
    glVertex2f(300,40)#s
    glVertex2f(300,20)#t
    glEnd()
    #pohon - daun1
    glColor3ub(19,134,0)
    glBegin(GL_POLYGON)
    glVertex2f(210,40)#d1
    glVertex2f(210,80)#u
    glVertex2f(340,80)#v
    glVertex2f(340,40)#c1
    glEnd()
    #pohon - kayu2
    glColor3ub(97,60,17)
    glBegin(GL_POLYGON)
    glVertex2f(980,20)#i1
    glVertex2f(980,40)#j1
    glVertex2f(1030,40)#k1
    glVertex2f(1030,20)#l1
    glEnd()
    #pohon - daun2
    glColor3ub(19,134,0)
    glBegin(GL_POLYGON)
    glVertex2f(940,40)#m1
    glVertex2f(940,80)#o1
    glVertex2f(1070,80)#p1
    glVertex2f(1070,40)#n1
    glEnd()
    #pohon - kayu3
    glColor3ub(97,60,17)
    glBegin(GL_POLYGON)
    glVertex2f(-900,20)#v1
    glVertex2f(-900,40)#z1
    glVertex2f(-850,40)#w1
    glVertex2f(-850,20)#u1
    glEnd()
    #pohon - daun3
    glColor3ub(19,134,0)
    glBegin(GL_POLYGON)
    glVertex2f(-970,40)#a2
    glVertex2f(-970,80)#d2
    glVertex2f(-780,80)#c2
    glVertex2f(-780,40)#b2
    glEnd()
    glPopMatrix()

def gamestart():
    background()
    Matahari(800,300,360)
    Bangunan()
    poin()
    bodyAir(75,11,360)
    collision()
    
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,1.0,1.)
    # glOrtho(-1280, 1280, 0, 700, 0.0, 1.0)
    glViewport(0, 0, 1280, 1280)
    
    if gameMulai == True:
        gamestart()
        drawText('LEVEL : ' + str(tingkatLevel), -1150 ,350, 0,0,0)
    else:
        tombolPlay()
    glFlush()

def input_untuk_mouse(button, state, x,y):
    global pos_x_tombol, gameMulai

    if button == GLUT_LEFT_BUTTON:
        gameMulai = True
    
def input_keyboard(key,x,y):
    global y_body
    if key == GLUT_KEY_UP:
        if y_body >= 195:
            y_body +=0
        else:
            y_body += 15
            
    elif key == GLUT_KEY_DOWN:
        if y_body <= -680:
            y_body -=0
        else:
            y_body -= 15

def update(value):
    glutPostRedisplay()
    glutTimerFunc(10,update,0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(1280,700)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Game Pesawat")
    glutDisplayFunc(display)
    glutSpecialFunc(input_keyboard)
    glutMouseFunc(input_untuk_mouse)
    glutTimerFunc(1,update,0)
    init()
    glutMainLoop()

main()
