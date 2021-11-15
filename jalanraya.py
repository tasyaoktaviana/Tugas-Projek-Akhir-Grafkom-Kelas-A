from OpenGL import GL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h= 850,850

def init():
    glClearColor(0.0,0.0,1.0,0.0)
    gluOrtho2D(-850.0, 850.0, -850.0, 850.0)

#Jalan

def jalan():
    glColor3ub(88, 92, 82)
    glBegin(GL_QUADS)
    glVertex2f(0, 260)
    glVertex2f(0, 200)
    glVertex2f(820, 200)
    glVertex2f(820, 260)
    glEnd()

def garisputihjalan1():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(55, 235)
    glVertex2f(55, 225)
    glVertex2f(105, 225)
    glVertex2f(105, 235)
    glEnd()

def garisputihjalan2():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(135, 235)
    glVertex2f(135, 225)
    glVertex2f(185, 225)
    glVertex2f(185, 235)
    glEnd()

def garisputihjalan3():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(215, 235)
    glVertex2f(215, 225)
    glVertex2f(265, 225)
    glVertex2f(265, 235)
    glEnd()

def garisputihjalan4():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(300, 260)
    glVertex2f(300, 200)
    glVertex2f(310, 200)
    glVertex2f(310, 260)
    glEnd()

def garisputihjalan5():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(340, 260)
    glVertex2f(340, 200)
    glVertex2f(350, 200)
    glVertex2f(350, 260)
    glEnd()

def garisputihjalan6():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(380, 260)
    glVertex2f(380, 200)
    glVertex2f(390, 200)
    glVertex2f(390, 260)
    glEnd()

def garisputihjalan7():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(430, 235)
    glVertex2f(430, 225)
    glVertex2f(480, 225)
    glVertex2f(480, 235)
    glEnd()

def garisputihjalan8():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(510, 235)
    glVertex2f(510, 225)
    glVertex2f(560, 225)
    glVertex2f(560, 235)
    glEnd()

def garisputihjalan9():
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(590, 235)
    glVertex2f(590, 225)
    glVertex2f(640, 225)
    glVertex2f(640, 235)
    glEnd()

def garisputihjalan10():
    glBegin(GL_QUADS)
    glVertex2f(670, 235)
    glVertex2f(670, 225)
    glVertex2f(720, 225)
    glVertex2f(720, 235)
    glEnd()

def iterate():
    glViewport(0, 0, 850, 850)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 850, 0.0, 850, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    jalan()
    garisputihjalan1()
    garisputihjalan2()
    garisputihjalan3()
    garisputihjalan4()
    garisputihjalan5()
    garisputihjalan6()
    garisputihjalan7()
    garisputihjalan8()
    garisputihjalan9()
    garisputihjalan10()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 800)
glutInitWindowPosition(100, 100)
wind = glutCreateWindow("OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
init()
glutMainLoop()