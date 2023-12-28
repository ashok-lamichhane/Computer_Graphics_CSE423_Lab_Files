
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random  #for import the random values:


def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()

def draw_tirangle(a,b,c,d,e,f):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_TRIANGLES)
    glVertex2f(a,b) #jekhane show korbe pixel
    glVertex2f(c, d)
    glVertex2f(e, f)
    glEnd()

def draw_lines(x, y,z,w):
    glPointSize(5) #pixel size. by default 1 thake
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(x,y) #jekhane show korbe pixel
    glVertex2f(z, w)
    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 1.0) #konokichur color set (RGB)
    #call the draw methods here
    draw_points(260, 95)
    draw_tirangle(100,350,400,350,250,495)
    draw_lines(100,350,100,50)
    draw_lines(400, 350, 400, 50)
    draw_lines(100, 50, 400, 50)
    draw_tirangle(150,250,200,250,200,300)
    draw_tirangle(200, 300, 150, 300, 150, 250)
    draw_tirangle(300, 250, 350, 250, 350, 300)
    draw_tirangle(350, 300, 300, 300, 300, 250)
    draw_lines(220, 50, 220, 150)
    draw_lines(220, 150, 270, 150)
    draw_lines(270, 50, 270, 150)
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)  #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task 2 Solution")  #window name
glutDisplayFunc(showScreen)
glutMainLoop()

