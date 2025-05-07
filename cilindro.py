import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import math


distance = 8


mouse_pressed = False
mouse_pos = (0, 0)
rot_x = 0
rot_y = 0


poliform = False


width, height = 800, 600


def init():
    glfw.init()
    window = glfw.create_window(width,height, "Cubo 3D", None, None)    
    glfw.make_context_current(window)
    glViewport(0, 0, width, height)
    # Configuração do pipeline gráfico
    glMatrixMode(GL_PROJECTION) #seleciona matriz projeção
    glLoadIdentity()
    #define a projeção perspectiva
    gluPerspective(45, width / height, 0.1, 100.0) #configura campo de visão e proporção, ponto mais próximo e ponto mais distante
    glMatrixMode(GL_MODELVIEW) #volta para a matriz de modelo
    glEnable(GL_DEPTH_TEST) #garante que objetos mais distantes não sejam desenhados sobre objetos mais próximos


    return window




def scroll_callback(window, xpos, ypos):
    global distance


    if(ypos >= 1):
        distance -= 1
    elif(ypos <= -1):
        distance += 1


def mouse_button_callback(window, button, action, mods):
    global mouse_pressed
    if(button == glfw.MOUSE_BUTTON_LEFT):
        mouse_pressed = (action == glfw.PRESS)


def cursor_pos_callback(window, xpos, ypos):
    global mouse_pos, rot_x, rot_y
    if mouse_pressed:
        dx = xpos - mouse_pos[0]
        dy = ypos - mouse_pos[1]
        rot_x += dx * 0.5
        rot_y += dy * 0.5
    mouse_pos = (xpos, ypos)


def key_callback(window, key, scancode, action, mods):
    global rot_x, rot_y, poliform
    if action in [glfw.PRESS, glfw.REPEAT]:
        if key == glfw.KEY_UP:
            rot_x -= 5
        elif key == glfw.KEY_DOWN:
            rot_x += 5
        elif key == glfw.KEY_LEFT:
            rot_y -= 5
        elif key == glfw.KEY_RIGHT:
            rot_y += 5
        elif key == glfw.KEY_SPACE:
            poliform = not poliform
       


def desenharPiramide():
    glBegin(GL_QUADS)
    # Base
    glColor3f(1, 0, 0)
    glVertex3f(1, 1,  0) # A
    glVertex3f(1, -1,  0) # B
    glVertex3f(-1,  -1,  0) # C
    glVertex3f(-1,  1,  0) # D
    glEnd()


    glBegin(GL_TRIANGLES)
    # Triângulo face 1 (ABE)
    glColor3f(0.72, 0.25, 0.50)
    glVertex3f(1, 1,  0) # A
    glVertex3f(1, -1,  0) # B
    glVertex3f(0, 0, 2) # E
    glEnd()
   
    glBegin(GL_TRIANGLES)
    # Triângulo face 1 (BCE)
    glColor3f(0.22, 0.72, 0.77)
    glVertex3f(1, -1,  0) # B
    glVertex3f(-1,  -1,  0) # C
    glVertex3f(0, 0, 2) # E
    glEnd()


    glBegin(GL_TRIANGLES)
    # Triângulo face 1 (CDE)
    glColor3f(0.12, 0.62, 0.37)
    glVertex3f(-1,  -1,  0) # C
    glVertex3f(-1,  1,  0) # D
    glVertex3f(0, 0, 2) # E
    glEnd()


    glBegin(GL_TRIANGLES)
    # Triângulo face 1 (DAE)
    glColor3f(0.42, 0.22, 0.97)
    glVertex3f(1, 1,  0) # A
    glVertex3f(-1,  1,  0) # D
    glVertex3f(0, 0, 2) # E
    glEnd()


def desenharCilindro():
    radius = 0.25
    # Circulo inf
    glColor3f(0.42, 0.22, 0.97)
    glBegin(GL_POLYGON)
    glVertex3f(0, 0, 0)
    for i in range(50 + 1):
        angle = 2 * math.pi * i / 50
        glVertex3f(0 + radius * math.cos(angle), 0 + radius * math.sin(angle), 0)
    glEnd()


    for i in range(500 + 1):
        glColor3f(0.1,0.6,0.6)
        glBegin(GL_LINE_LOOP)
        glVertex3f(0 + radius * math.cos(angle), 0 + radius * math.sin(angle), 0)
        angle = 2 * math.pi * i / 500
        glVertex3f(0 + radius * math.cos(angle), 0 + radius * math.sin(angle), 1)
        glEnd()


    # Circulo sup
    glColor3f(0.42, 0.22, 0.97)
    glBegin(GL_POLYGON)
    glVertex3f(0, 0, 1)
    for i in range(50 + 1):
        angle = 2 * math.pi * i / 50
        glVertex3f(0 + radius * math.cos(angle), 0 + radius * math.sin(angle), 1)
    glEnd()




def main():
   
    window = init()


    glfw.set_scroll_callback(window, scroll_callback)
    glfw.set_mouse_button_callback(window, mouse_button_callback)
    glfw.set_cursor_pos_callback(window, cursor_pos_callback)
    glfw.set_key_callback(window, key_callback)


    ang = 0


    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()


        # Câmera
        #Posição da câmera (4, 4, 8) indica a posição da câmera no espaço 3D.
        #Ponto de observação (centerX, centerY, centerZ):(0, 0, 0) é o ponto para onde a câmera está olhando
        #Vetor "para cima" (upX, upY, upZ):(0, 1, 0) define a orientação "para cima" da câmera.
        #gluLookAt(0, 0, 0, 0, 0, 0, 0, 1, 0)
        gluLookAt(
            distance * 0.5, distance * 0.4, distance,
            0, 0, 0,
            0, 1, 0
        )


        glRotatef(rot_x, 1, 0, 0)
        glRotatef(rot_y, 0, 1, 0)


        if(poliform):
            desenharPiramide()
        else:
            desenharCilindro()


        glfw.swap_buffers(window)
        glfw.poll_events()


    glfw.terminate()


if __name__ == "__main__":
    main()





