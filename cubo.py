import glfw                         # Biblioteca para criar janela e lidar com eventos
from OpenGL.GL import *             # Comandos básicos de OpenGL
from OpenGL.GLU import *            # Utilitários de OpenGL, como gluPerspective e gluLookAt

# Tamanho da janela
width, height = 800, 600

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

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Limpa a tela e o buffer de profundidade
        glLoadIdentity()  # Reseta a matriz de modelo

        # Configura a câmera
        gluLookAt(4, 4, 8,   # Posição da câmera
                  0, 0, 0,   # Para onde a câmera olha
                  0, 1, 0)   # Qual lado é "cima"

        glRotatef(ang, 1, 1, 0)  # Rotaciona a pirâmide nos eixos X e Y

        desenharPiramide()      # Chama a função que desenha a pirâmide
        ang += 0.5              # Incrementa o ângulo para próxima rotação

        glfw.swap_buffers(window)  # Troca os buffers para mostrar a imagem
        glfw.poll_events()         # Processa eventos (como fechar janela)

    glfw.terminate()  # Encerra a janela e limpa recursos

# Executa o programa
if __name__ == "__main__":
    main()
