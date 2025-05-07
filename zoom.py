import glfw                         # Biblioteca para criar janela e lidar com eventos
from OpenGL.GL import *             # Comandos básicos de OpenGL
from OpenGL.GLU import *            # Utilitários de OpenGL, como gluPerspective e gluLookAt

# Tamanho da janela
width, height = 800, 600

distance = 45
mouse_pressed = False
mouse_pos = (0,0)
rot_x = 0
rot_y = 0

# Inicialização do OpenGL e da janela
def init():
    glfw.init()  # Inicializa o GLFW
    window = glfw.create_window(width, height, "Pirâmide 3D", None, None)  # Cria uma janela
    glfw.make_context_current(window)  # Torna o contexto atual para renderização

    glViewport(0, 0, width, height)  # Define a área de renderização

    # Configura a projeção em perspectiva (visão 3D)
    glMatrixMode(GL_PROJECTION)     # Seleciona a matriz de projeção
    glLoadIdentity()
    gluPerspective(45, width / height, 0.1, 100.0)  # Ângulo de visão, proporção, plano próximo e distante

    glMatrixMode(GL_MODELVIEW)      # Volta para a matriz de modelo (posição dos objetos)
    glEnable(GL_DEPTH_TEST)         # Habilita o teste de profundidade (evita sobreposição errada de objetos)

    return window

def scroll_callback(window, xpos, ypos):
    global distance

    if(ypos>=1):
        distance-=1
    elif(ypos<=-1):
        distance+=1

def mouse_button_callback(window, button, action, mods):
    global mouse_pressed
    if (button == glfw.MOUSE_BUTTON_LEFT):
        mouse_pressed = (action == glfw.PRESS)

def cursor_callback(window, xpos, ypos):
    global mouse_pos, rot_x, rot_y
    if(mouse_pressed):
        dx = xpos - mouse_pos[0]
        dy = ypos - mouse_pos[1]
        rot_y += dx * 0.005
        rot_x += dy * 0.005

def key_callback(window, key, scancode, action, mods):
    global rot_x, rot_y
    if action in [glfw.PRESS, glfw.REPEAT]:
        if key == glfw.KEY_UP:
            rot_x -= 5
        elif key == glfw.KEY_DOWN:
            rot_x += 5
        elif key == glfw.KEY_LEFT:
            rot_y -= 5  
        elif key == glfw.KEY_RIGHT:
            rot_y += 5          

# Função para desenhar uma pirâmide 3D
def desenharPiramide():
    # Base da pirâmide (quadrado)
    glBegin(GL_QUADS)
    glColor3f(0.5, 0.5, 0.5)  # Cor cinza
    glVertex3f(-1, 0, -1)     # Vértice 1
    glVertex3f(1, 0, -1)      # Vértice 2
    glVertex3f(1, 0, 1)       # Vértice 3
    glVertex3f(-1, 0, 1)      # Vértice 4
    glEnd()

    # Lados da pirâmide (triângulos)
    glBegin(GL_TRIANGLES)

    # Lado da frente
    glColor3f(1, 0, 0)  # Vermelho
    glVertex3f(-1, 0, 1)   # Base esquerda
    glVertex3f(1, 0, 1)    # Base direita
    glVertex3f(0, 2, 0)    # Topo

    # Lado da direita
    glColor3f(0, 1, 0)  # Verde
    glVertex3f(1, 0, 1)
    glVertex3f(1, 0, -1)
    glVertex3f(0, 2, 0)

    # Lado de trás
    glColor3f(0, 0, 1)  # Azul
    glVertex3f(1, 0, -1)
    glVertex3f(-1, 0, -1)
    glVertex3f(0, 2, 0)

    # Lado da esquerda
    glColor3f(1, 1, 0)  # Amarelo
    glVertex3f(-1, 0, -1)
    glVertex3f(-1, 0, 1)
    glVertex3f(0, 2, 0)

    glEnd()

# Função principal
def main():
    window = init()  # Inicializa janela e OpenGL
    ang = 0          # Ângulo de rotação
    glfw.set_scroll_callback(window, scroll_callback)
    glfw.set_mouse_button_callback(window, mouse_button_callback)
    glfw.set_cursor_pos_callback(window, cursor_callback) 
    glfw.set_key_callback(window,key_callback)

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Limpa a tela e o buffer de profundidade
        glLoadIdentity()  # Reseta a matriz de modelo

        # Configura a câmera
        gluLookAt(distance*0.5, distance*0.4, distance,   # Posição da câmera
                  0, 0, 0,   # Para onde a câmera olha
                  0, 1, 0)   # Qual lado é "cima"

        glRotatef(rot_x, 1, 0, 0) 
        glRotatef(rot_y, 0, 1, 0)

        desenharPiramide()      # Chama a função que desenha a pirâmide

        glfw.swap_buffers(window)  # Troca os buffers para mostrar a imagem
        glfw.poll_events()         # Processa eventos (como fechar janela)

    glfw.terminate()  # Encerra a janela e limpa recursos

# Executa o programa
if __name__ == "__main__":
    main()
