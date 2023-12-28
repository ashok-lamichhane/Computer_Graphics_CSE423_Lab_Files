from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_lines(x, y,z,w):
    glPointSize(5) #pixel size. by default 1 thake
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(x,y) #jekhane show korbe pixel
    glVertex2f(z, w)
    glEnd()

def draw_numbers(x, y,a):
    if a == 0:
        glColor3f(1.0, 0.0, 0.0)
        draw_lines(x,y,x+55,y)
        draw_lines(x+55, y, x + 55, y+55)
        draw_lines(x+55, y+55, x + 55, y+110)
        draw_lines(x, y+110, x + 55, y+110)
        draw_lines(x, y+55, x, y+110)
        #draw_lines(x, y+55, x + 55, y+55)
        draw_lines(x, y, x, y+55)

    elif a == 1:
        glColor3f(0.0, 1.0, 0.0)
        #draw_lines(x,y,x+55,y)
        draw_lines(x+55, y, x + 55, y+55)
        draw_lines(x+55, y+55, x + 55, y+110)
        #draw_lines(x, y+110, x + 55, y+110)
        #draw_lines(x, y+55, x, y+110)
        #draw_lines(x, y+55, x + 55, y+55)
        #draw_lines(x, y, x, y+55)

    elif a == 2:
        glColor3f(0.0, 0.0, 1.0)
        draw_lines(x,y,x+55,y)
        #draw_lines(x+55, y, x + 55, y+55)
        draw_lines(x+55, y+55, x + 55, y+110)
        draw_lines(x, y+110, x + 55, y+110)
        #draw_lines(x, y+55, x, y+110)
        draw_lines(x, y+55, x + 55, y+55)
        draw_lines(x, y, x, y+55)

    elif a == 3:
        glColor3f(1.0, 1.0, 0.0)
        draw_lines(x,y,x+55,y)
        draw_lines(x+55, y, x + 55, y+55)
        draw_lines(x+55, y+55, x + 55, y+110)
        draw_lines(x, y+110, x + 55, y+110)
        #draw_lines(x, y+55, x, y+110)
        draw_lines(x, y+55, x + 55, y+55)
        #draw_lines(x, y, x, y+55)

    elif a == 4:
        glColor3f(0.0, 1.0, 1.0)
        #draw_lines(x,y,x+55,y)
        draw_lines(x+55, y, x + 55, y+55)
        draw_lines(x+55, y+55, x + 55, y+110)
        #draw_lines(x, y+110, x + 55, y+110)
        draw_lines(x, y+55, x, y+110)
        draw_lines(x, y+55, x + 55, y+55)
        #draw_lines(x, y, x, y+55)

    elif a == 5:
        glColor3f(1.0, 0.0, 1.0)
        draw_lines(x,y,x+55,y)
        draw_lines(x+55, y, x + 55, y+55)
        #draw_lines(x+55, y+55, x + 55, y+110)
        draw_lines(x, y+110, x + 55, y+110)
        draw_lines(x, y+55, x, y+110)
        draw_lines(x, y+55, x + 55, y+55)
        #draw_lines(x, y, x, y+55)

    elif a == 6:
        glColor3f(1.0, 0.5, 0.8)
        draw_lines(x,y,x+55,y)
        draw_lines(x+55, y, x + 55, y+55)
        #draw_lines(x+55, y+55, x + 55, y+110)
        draw_lines(x, y+110, x + 55, y+110)
        draw_lines(x, y+55, x, y+110)
        draw_lines(x, y+55, x + 55, y+55)
        draw_lines(x, y, x, y+55)

    elif a == 7:
        glColor3f(1.0, 1.0, 1.0)
        #draw_lines(x,y,x+55,y)
        draw_lines(x+55, y, x + 55, y+55)
        draw_lines(x+55, y+55, x + 55, y+110)
        draw_lines(x, y+110, x + 55, y+110)
        #draw_lines(x, y+55, x, y+110)
        #draw_lines(x, y+55, x + 55, y+55)
        #draw_lines(x, y, x, y+55)

    elif a == 8:
        glColor3f(0.35, 0.05, 0.6)
        draw_lines(x,y,x+55,y)
        draw_lines(x+55, y, x + 55, y+55)
        draw_lines(x+55, y+55, x + 55, y+110)
        draw_lines(x, y+110, x + 55, y+110)
        draw_lines(x, y+55, x, y+110)
        draw_lines(x, y+55, x + 55, y+55)
        draw_lines(x, y, x, y+55)

    elif a == 9:
        glColor3f(0.4, 0.55, 0.05)
        draw_lines(x,y,x+55,y)
        draw_lines(x+55, y, x + 55, y+55)
        draw_lines(x+55, y+55, x + 55, y+110)
        draw_lines(x, y+110, x + 55, y+110)
        draw_lines(x, y+55, x, y+110)
        draw_lines(x, y+55, x + 55, y+55)
        #draw_lines(x, y, x, y+55)

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
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)

    id = '21201785'
    x = 3
    for i in id:
        draw_numbers(x,200,int(i))
        x += 63

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task 3 Solution ") #window name
glutDisplayFunc(showScreen)
glutMainLoop()