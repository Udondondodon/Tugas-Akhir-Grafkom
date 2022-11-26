import OpenGL.GLUT as glut
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import random

#Position awal pesawat
x_body = 0
y_body = -100

pos_x_tombol = 0
pos_y_tombol = -200

pos_x_bangun1 = 600
pos_y_bangun1 = -500
pos_x_bangun2 = 900
pos_y_bangun2 = -500
pos_x_bangun3 = 1150
pos_y_bangun3 = -500
pos_x_bangun4 = 1400
pos_y_bangun4 = -500

gameMulai = False

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-500.0, 500.0, -500.0, 500.0)

def drawTextBold(ch,xpos,ypos):
    glPushMatrix()
    font_style = glut.GLUT_BITMAP_HELVETICA_18
    glColor3ub(255,255,255)
    line=0
    glRasterPos2f (xpos, ypos)
    for i in ch:
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))  
    glPopMatrix()
    
def lingkaranPlay(xn,yn,sugmentyn):
    
    glColor3ub(0,0,0)
    glBegin(GL_POLYGON)
    for i in range(sugmentyn):
        theta= 2 *3.1415926*i/sugmentyn
        x = 64* math.cos(theta)
        y = 64* math.sin(theta)
        glVertex2f(x + xn, y + yn)
    glEnd()
    
def tombolPlay(cx,cy,num_seg):
    global pos_x_tombol, pos_y_tombol
    glPushMatrix()
    glColor3ub(102, 255, 0)
    glTranslated(pos_x_tombol,pos_y_tombol,0)
    
    glBegin(GL_POLYGON)
    for i in range(num_seg):
        theta= 2 *3.1415926*i/num_seg
        x = 100* math.cos(theta)
        y = 100* math.sin(theta)
        glVertex2f(x + cx, y + cy)
    glEnd()
    
    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-20,52)#c
    glVertex2f(-20,-52)#d
    glVertex2f(-5,-56)#k
    glVertex2f(38,-5)#n
    glVertex2f(38,5)#e
    glVertex2f(-5,56)#j
    # glBegin(GL_QUADS)
    # glVertex2f(-20,-20)
    # glVertex2f(20,-20)
    # glVertex2f(20,20)
    # glVertex2f(-20,20)

    glEnd()
    glPopMatrix()

#Player Pesawat
def bodyAir(cx,cy,num_segment):
    glPushMatrix()
    glScale(0.5,0.5,0)
    global y_body
    glTranslatef(-700,-300,0)
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
    glVertex2f(-500,-500)
    glVertex2f(-500,500)
    glVertex2f(500,500)
    glVertex2f(500,-500)
    glEnd()
    glPopMatrix()

def bangunan1():
    global pos_x_bangun1, pos_y_bangun1

    glPushMatrix()
    glColor3ub(117, 108, 106)
    glTranslated(pos_x_bangun1,pos_y_bangun1,0)
    pos_x_bangun1 -= 1
    if pos_x_bangun1 < -650:
        pos_x_bangun1 = 600

    glBegin(GL_POLYGON)
    glVertex2f(0,0)
    glVertex2f(140,0)
    glVertex2f(140,200)
    glVertex2f(0,200)
    glEnd()
    glColor3ub(77, 76, 73)
    glBegin(GL_POLYGON)
    glVertex2f(20,150)
    glVertex2f(50,150)
    glVertex2f(50,180)
    glVertex2f(20,180)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(90,180)
    glVertex2f(120,180)
    glVertex2f(120,150)
    glVertex2f(90,150)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(20,130)
    glVertex2f(20,100)
    glVertex2f(50,100)
    glVertex2f(50,130)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(90,100)
    glVertex2f(120,100)
    glVertex2f(120,130)
    glVertex2f(90,130)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(20,50)
    glVertex2f(50,50)
    glVertex2f(50,80)
    glVertex2f(20,80)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(90,50)
    glVertex2f(120,50)
    glVertex2f(120,80)
    glVertex2f(90,80)
    glEnd()
    glPopMatrix()

def bangunan2():
    global pos_x_bangun2, pos_y_bangun2

    glPushMatrix()
    glColor3ub(227, 178, 113)
    glTranslated(pos_x_bangun2,pos_y_bangun2,0)
    pos_x_bangun2 -= 1
    if pos_x_bangun2 < -650:
        pos_x_bangun2 = 600

    glBegin(GL_POLYGON)
    glVertex2f(0,0)
    glVertex2f(140,0)
    glVertex2f(140,150)
    glVertex2f(0,150)
    glEnd()
    glColor3ub(77, 76, 73)
    glBegin(GL_POLYGON)
    glVertex2f(20,130)
    glVertex2f(20,100)
    glVertex2f(50,100)
    glVertex2f(50,130)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(90,100)
    glVertex2f(120,100)
    glVertex2f(120,130)
    glVertex2f(90,130)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(20,50)
    glVertex2f(50,50)
    glVertex2f(50,80)
    glVertex2f(20,80)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(90,50)
    glVertex2f(120,50)
    glVertex2f(120,80)
    glVertex2f(90,80)
    glEnd()
    glPopMatrix()

def bangunan3():
    global pos_x_bangun3, pos_y_bangun3
    glPushMatrix()
    glColor3ub(224, 92, 127)
    glTranslated(pos_x_bangun3,pos_y_bangun3,0)
    pos_x_bangun3 -= 1
    if pos_x_bangun3 < -650:
        pos_x_bangun3 = 600

    glBegin(GL_POLYGON)
    glVertex2f(0,0)
    glVertex2f(140,0)
    glVertex2f(140,200)
    glVertex2f(0,200)
    glEnd()
    glColor3ub(77, 76, 73)
    glBegin(GL_POLYGON)
    glVertex2f(20,150)
    glVertex2f(50,150)
    glVertex2f(50,180)
    glVertex2f(20,180)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(90,180)
    glVertex2f(120,180)
    glVertex2f(120,150)
    glVertex2f(90,150)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(20,130)
    glVertex2f(20,100)
    glVertex2f(50,100)
    glVertex2f(50,130)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(90,100)
    glVertex2f(120,100)
    glVertex2f(120,130)
    glVertex2f(90,130)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(20,50)
    glVertex2f(50,50)
    glVertex2f(50,80)
    glVertex2f(20,80)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(90,50)
    glVertex2f(120,50)
    glVertex2f(120,80)
    glVertex2f(90,80)
    glEnd()
    glPopMatrix()

def bangunan4():
    global pos_x_bangun4, pos_y_bangun4
    glPushMatrix()
    glColor3ub(50, 179, 86)
    glTranslated(pos_x_bangun4,pos_y_bangun4,0)
    pos_x_bangun4 -= 1
    if pos_x_bangun4 < -650:
        pos_x_bangun4 = 600

    glBegin(GL_POLYGON)
    glVertex2f(0,0)
    glVertex2f(140,0)
    glVertex2f(140,200)
    glVertex2f(0,200)
    glEnd()
    glColor3ub(77, 76, 73)
    glBegin(GL_POLYGON)
    glVertex2f(20,150)
    glVertex2f(50,150)
    glVertex2f(50,180)
    glVertex2f(20,180)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(90,180)
    glVertex2f(120,180)
    glVertex2f(120,150)
    glVertex2f(90,150)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(20,130)
    glVertex2f(20,100)
    glVertex2f(50,100)
    glVertex2f(50,130)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(90,100)
    glVertex2f(120,100)
    glVertex2f(120,130)
    glVertex2f(90,130)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(20,50)
    glVertex2f(50,50)
    glVertex2f(50,80)
    glVertex2f(20,80)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(90,50)
    glVertex2f(120,50)
    glVertex2f(120,80)
    glVertex2f(90,80)
    glEnd()
    glPopMatrix()


def gamestart():
    background()
    bodyAir(75,11,360)
    bangunan1()
    bangunan2()
    bangunan3()
    bangunan4()
        
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,1.0,1.)
    glViewport(0,0,1280,1280)
    
    if gameMulai == True:
        gamestart()
    else:
        lingkaranPlay(-12,52,360)#bagian atas
        lingkaranPlay(-12,-52,360)#bagian bawah
        lingkaranPlay(32,0,360)#bagian tengah
        tombolPlay(0,0,360)
    glFlush()

def input_untuk_mouse(button, state, x,y):
    global pos_x_tombol, gameMulai

    if button == GLUT_LEFT_BUTTON:
        gameMulai = True
    
def input_keyboard(key,x,y):
    global y_body
    if key == GLUT_KEY_UP:
        if y_body == 440:
            y_body +=0
        else:
            y_body += 10
            
    elif key == GLUT_KEY_DOWN:
        if y_body == 60:
            y_body -=0
        else:
            y_body -= 10

def update(value):
    glutPostRedisplay()
    glutTimerFunc(10,update,0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(1280,550)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Game Pesawat")
    glutDisplayFunc(display)
    glutSpecialFunc(input_keyboard)
    # glutSpecialFunc(positionPesawat)
    glutMouseFunc(input_untuk_mouse)
    glutTimerFunc(1,update,0)
    init()
    glutMainLoop()

main()