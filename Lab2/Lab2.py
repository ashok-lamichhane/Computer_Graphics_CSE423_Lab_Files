from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def find_zone(dx, dy):
    if abs(dx) >= abs(dy):
       if dx >= 0 and dy >= 0:
           return 0
       elif dx <= 0 and dy >= 0:
           return 3
       elif dx <= 0 and dy <= 0:
           return 4
       elif dx >= 0 and dy <= 0:
           return 7

    else:
       if dx >= 0 and dy >= 0:
           return 1
       elif dx <= 0 and dy >= 0:
           return 2
       elif dx <= 0 and dy <= 0:
           return 5
       elif dx >= 0 and dy <= 0:
           return 6

def convert_to_zone_zero(zone, x, y):
   if zone == 0:
       return x, y
   if zone == 1:
       return y, x
   if zone == 2:
     return y, -x
   if zone == 3:
       return -x, y
   if zone == 4:
       return -x, -y
   if zone == 5:
       return -y, -x
   if zone == 6:
       return -y, x
   if zone == 7:
       return x, -y

def convert_to_original_zone(zone, x, y):
   if zone == 0:
       return x, y
   if zone == 1:
       return y, x
   if zone == 2:
       return -y, x
   if zone == 3:
       return -x, y
   if zone == 4:
       return -x, -y
   if zone == 5:
       return -y, -x
   if zone == 6:
       return y, -x
   if zone == 7:
       return x, -y

def mid_point_line(x1, y1, x2, y2, zone):
   dx = x2 - x1
   dy = y2 - y1

   d_init = (2*dy) - dx
   del_E = 2*dy
   del_NE = 2 * (dy-dx)

   x = x1
   y = y1

   while x < x2:
       x_org, y_org = convert_to_original_zone(zone, x, y)
       draw_points(x_org, y_org)
       if d_init < 0:
           x += 1
           d_init += del_E
       else:
           x += 1
           y += 1
           d_init += del_NE

def drawLine(x1, y1, x2, y2):
   dx = x2 - x1
   dy = y2 - y1
   zone = find_zone(dx, dy)

   new_x1, new_y1 = convert_to_zone_zero(zone, x1, y1)
   new_x2, new_y2 = convert_to_zone_zero(zone, x2, y2)
   mid_point_line(new_x1, new_y1, new_x2, new_y2, zone)

def number(x,y,a):
    if a == 0:
        drawLine(x, y, x+100, y)
        drawLine(x, y+100, x, y)
        drawLine(x+100, y, x+100, y+100)
        #drawLine(x, y+100, x+100, y+100)
        drawLine(x, y+100, x, y+200)
        drawLine(x, y + 200, x+100, y + 200)
        drawLine(x+100, y + 100, x+100, y + 200)

    elif a == 1:
        #drawLine(x, y, x+100, y)
        #drawLine(x, y+100, x, y)
        drawLine(x+100, y, x+100, y+100)
        #drawLine(x, y+100, x+100, y+100)
        #drawLine(x, y+100, x, y+200)
        #drawLine(x, y + 200, x+100, y + 200)
        drawLine(x+100, y + 100, x+100, y + 200)

    elif a == 2:
        drawLine(x, y, x+100, y)
        drawLine(x, y+100, x, y)
        #drawLine(x+100, y, x+100, y+100)
        drawLine(x, y+100, x+100, y+100)
        #drawLine(x, y+100, x, y+200)
        drawLine(x, y + 200, x+100, y + 200)
        drawLine(x+100, y + 100, x+100, y + 200)

    elif a == 3:
        drawLine(x, y, x+100, y)
        #drawLine(x, y+100, x, y)
        drawLine(x+100, y, x+100, y+100)
        drawLine(x, y+100, x+100, y+100)
        #drawLine(x, y+100, x, y+200)
        drawLine(x, y + 200, x+100, y + 200)
        drawLine(x+100, y + 100, x+100, y + 200)

    elif a == 4:
        #drawLine(x, y, x+100, y)
        #drawLine(x, y+100, x, y)
        drawLine(x+100, y, x+100, y+100)
        drawLine(x, y+100, x+100, y+100)
        drawLine(x, y+100, x, y+200)
        #drawLine(x, y + 200, x+100, y + 200)
        drawLine(x+100, y + 100, x+100, y + 200)

    elif a == 5:
        drawLine(x, y, x+100, y)
        #drawLine(x, y+100, x, y)
        drawLine(x+100, y, x+100, y+100)
        drawLine(x, y+100, x+100, y+100)
        drawLine(x, y+100, x, y+200)
        drawLine(x, y + 200, x+100, y + 200)
        #drawLine(x+100, y + 100, x+100, y + 200)

    elif a == 6:
        drawLine(x, y, x+100, y)
        drawLine(x, y+100, x, y)
        drawLine(x+100, y, x+100, y+100)
        drawLine(x, y+100, x+100, y+100)
        drawLine(x, y+100, x, y+200)
        drawLine(x, y + 200, x+100, y + 200)
        #drawLine(x+100, y + 100, x+100, y + 200)

    elif a == 7:
        #drawLine(x, y, x+100, y)
        #drawLine(x, y+100, x, y)
        drawLine(x+100, y, x+100, y+100)
        #drawLine(x, y+100, x+100, y+100)
        #drawLine(x, y+100, x, y+200)
        drawLine(x, y + 200, x+100, y + 200)
        drawLine(x+100, y + 100, x+100, y + 200)

    elif a == 8:
        drawLine(x, y, x+100, y)
        drawLine(x, y+100, x, y)
        drawLine(x+100, y, x+100, y+100)
        drawLine(x, y+100, x+100, y+100)
        drawLine(x, y+100, x, y+200)
        drawLine(x, y + 200, x+100, y + 200)
        drawLine(x+100, y + 100, x+100, y + 200)

    elif a == 9:
        drawLine(x, y, x+100, y)
        #drawLine(x, y+100, x, y)
        drawLine(x+100, y, x+100, y+100)
        drawLine(x, y+100, x+100, y+100)
        drawLine(x, y+100, x, y+200)
        drawLine(x, y + 200, x+100, y + 200)
        drawLine(x+100, y + 100, x+100, y + 200)

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1, 0.3, 0.8) #konokichur color set (RGB)
    #call the draw methods here
    #draw_points(250, 250)
    #number(100,150,9)
    id = '21201785'
    x = 100
    j = -2
    for i in range(2):
        number(x,150,int(id[j]))
        x += 150
        j += 1

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)  #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"A2: Drawing last 2 digit of Student ID ") #window name
glutDisplayFunc(showScreen)
glutMainLoop()