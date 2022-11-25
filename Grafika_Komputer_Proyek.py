from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

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

def tombolPlay():
    global pos_x_tombol, pos_y_tombol
    glPushMatrix()
    glColor3ub(102, 255, 0)
    glTranslated(pos_x_tombol,pos_y_tombol,0)

    glBegin(GL_QUADS)
    glVertex2f(-20,-20)
    glVertex2f(20,-20)
    glVertex2f(20,20)
    glVertex2f(-20,20)

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
        tombolPlay()
    glFlush()

def input_untuk_mouse(button, state, x,y):
    global pos_x_tombol, gameMulai

    if button == GLUT_LEFT_BUTTON:
        gameMulai = True
    
def input_keyboard(key,x,y):
    global pos_x_kotak, pos_y_kotak
    if key == GLUT_KEY_UP:
        pos_y_kotak = 10
    elif key == GLUT_KEY_DOWN:
        pos_y_kotak -= 5
    elif key == GLUT_KEY_RIGHT:
        pos_x_kotak += 5
    elif key == GLUT_KEY_LEFT:
        pos_x_kotak -= 5

def update(value):
    glutPostRedisplay()
    glutTimerFunc(10,update,0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(1280,550)
    glutInitWindowPosition(100,100)
    glutCreateWindow("collision")
    glutDisplayFunc(display)
    glutSpecialFunc(input_keyboard)
    glutMouseFunc(input_untuk_mouse)
    glutTimerFunc(1,update,0)
    init()
    glutMainLoop()

main()