#jogo da cobrinha 
#duas classes: cobra e cubo
import pygame
import random

#criando classe dos cubos
#são retângulos que possuem uma posição e uma cor
class Cubo:
    def __init__(self,color,pos):
        self.color = color
        self.pos = pos
        
    def draw_cubo(self,surface):
        pygame.draw.rect(surface, self.color, (self.pos[0], self.pos[1], widght, height))
    
#função que redesenha a tela do jogo, após todas as alterações terem isso feitas
def redrawthegameWindow():
    win.fill((0,0,0))
    win.blit(bg,(0,0))
    snake_skin = Cubo((255,0,0),(head_x,head_y))
    snake_skin.draw_cubo(win)
    maça = Cubo((153,204,50),(maça_x,maça_y))
    maça.draw_cubo(win)
    pygame.display.update()

#carregando imagem de fundo do jogo
bg = pygame.image.load('./Downloads/Escritório_FEA.dev/Game/bg.jpg') 
#velocidade com que o cubo vermelho se move
vel = 10
#tamamho da tela
width = 600
#comprimento e largura dos cudos, são usados na função draw_cubo
height = 20
widght = 20
#posição da cabeça da cobra (cubo vermelho que se move)
head_x = 10
head_y = 10
#a posição inicial da Maça também vai ser aleatória
maça_x = random.randint(0,460)
maça_y = random.randint(0,460)
#criando uma relógio no pygame que controla o fps máximo
clock = pygame.time.Clock()


#iniciando pygame
pygame.init()
#criando janela do jogo
win = pygame.display.set_mode((width,width))
#criando título para essa janela 
pygame.display.set_caption("Snake game in python")

#loop principal onde ocorre o jogo
finished = False
while finished == False:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        head_x -=vel
    if keys[pygame.K_RIGHT]:
        head_x += vel
    if keys[pygame.K_UP]:
        head_y -=vel    
    if keys[pygame.K_DOWN]:
        head_y += vel
    #cria limites para os movimentos do cubo vermelho
    if head_x <= 0 or head_x >= width:
        finished = True
    if head_y <=0 or head_y >= width:
        finished = True
    
    redrawthegameWindow()
#saindo do pygame
pygame.quit()