import pygame
import math
from Configuracoes import *
from Obstaculo import *
from Vida import *
from Impulsionador import *
from Tiro import *
import os
vec = pygame.math.Vector2

class Jogador():
    def __init__(self, game):
        self.x = X_CHAO
        self.y = Y_CHAO
        self.carregarImagemPersonagem(game)
        self.largura = self.image.get_width()
        self.altura = self.image.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)  # retangulo de colisoes
        self.rect.center = (self.x + self.largura/2, self.y + self.altura/2)
        self.pos = vec(self.x + self.largura/2, self.y + self.altura/2)
        self.vel = vec(0.0, 0.0)
        self.acc = vec(0.0, 0.0)

    # carrega a imagem do personagem de acordo com a escolha do usuario
    def carregarImagemPersonagem(self, game):
        self.imagemF = pygame.image.load(os.path.join('Imagens', 'personagem_principal_FEC_1.png'))
        self.imagemD = pygame.image.load(os.path.join('Imagens', 'personagem_principal_DIR_1.png'))
        self.imagemE = pygame.image.load(os.path.join('Imagens', 'personagem_principal_ESQ_1.png'))
        # carregar imagens para modo invencivel
        self.imagemInvencivelF = pygame.image.load(os.path.join('Imagens', 'personagem_principal_invencivel_FEC_1.png'))
        self.imagemInvencivelD = pygame.image.load(os.path.join('Imagens', 'personagem_principal_invencivel_DIR_1.png'))
        self.imagemInvencivelE = pygame.image.load(os.path.join('Imagens', 'personagem_principal_invencivel_ESQ_1.png'))
        self.image = self.imagemD

        # vetor com as imagens
        if game.ehInvencivel == False:
            self.imagens = [self.imagemF, self.imagemD, self.imagemE]
            if self.pular:
                self.image = self.imagemD
            else:
                self.image = self.imagemE
        if game.ehInvencivel == True:
            self.imagens = [self.imagemInvencivelF, self.imagemInvencivelD, self.imagemInvencivelE]
            if self.pular:
                self.image = self.imagemInvencivelD
            else:
                self.image = self.imagemInvencivelE

    # esse metodo atualiza as posicoes do jogador para que ele pule
    def pular(self, game):
        #verificar se a jogadora esta no chao (impossivel pular sem estar no chao)
        if self.pos.y == Y_CHAO:
            #atualiza a velocidade em y
            self.vel.y = VELOC_INICIAL_PULO
            #atualiza a aceleracao em y (efeito da gravidade)
            self.acc.y = ACE_GRAV
            #Correcao do pulo para o aumento da velocidade do jogo
            if len(game.obstaculos):
                self.acc.y = 0.014*game.obstaculos[0].vel*game.obstaculos[0].vel
                self.vel.y = -2.5*game.obstaculos[0].vel
            else:
                if len(game.inimigos):
                    self.acc.y = 0.014*game.inimigos[0].vel*game.inimigos[0].vel
                    self.vel.y = -2.5*game.inimigos[0].vel

    # esse metodo faz carregar o tiro do jogador na tela
    def atirar(self, game):
        game.tiros.append(Tiro(self.pos.x, self.pos.y - 200, pygame.image.load(os.path.join('Imagens', 'tiro.png')), -10 -
                               game.dvel))


    # esse metodo atualiza as posicoes do jogador
    def atualizar(self, game):
        # Equações de Movimento
        dt = 1

        # Atualizar velocidade e posição do jogador
        self.vel.y += self.acc.y * dt  # Atualiza a velocidade
        self.pos += self.vel * dt  # Atualiza a posição
        self.rect.midbottom = self.pos  # Atualiza o retângulo de colisão

        # Verificar quando chegamos ao chão
        if self.pos.y >= (Y_CHAO):
            # corrigir a posição para parar exatamente no chão
            self.pos.y = (Y_CHAO)
            # Zerar a velocidade para a personagem parar de cair
            self.vel.y = 0

    # desenha o jogador na tela com a imagem correspondente ao seu estado atual
    def desenhar(self, game, tela):
        # vetor com as imagens
        if game.ehInvencivel == False:
            self.imagens = [self.imagemF, self.imagemD, self.imagemE]
            if self.pular:
                self.image = self.imagemD
            else:
                self.image = self.imagemE
        if game.ehInvencivel == True:
            self.imagens = [self.imagemInvencivelF, self.imagemInvencivelD, self.imagemInvencivelE]
            if self.pular:
                self.image = self.imagemInvencivelD
            else:
                self.image = self.imagemInvencivelE

        # gerar efeito gradual no pulo
        # Se a posição estiver muito baixa, manter a imagem fechada
        if self.pos.y == (Y_CHAO):
            self.image = self.imagens[0]
        # Para uma posição intermediária, usar a posição intermediária
        elif self.pos.y < (Y_CHAO) and self.pos.y > (0.95 * Y_CHAO):
            self.image = self.imagens[1]
        # Para os demais casos, usar a imagem final (braços abertos)
        else:
            self.image = self.imagens[2]

        # gerar efeito de andar
        if self.pos.y == Y_CHAO and tela.tempo % 12 < 3:
            self.image = self.imagens[0]
        elif self.pos.y == Y_CHAO and tela.tempo % 12 < 6:
            self.image = self.imagens[1]
        elif self.pos.y == Y_CHAO and tela.tempo % 12 < 9:
            self.image = self.imagens[2]
        elif self.pos.y == Y_CHAO and tela.tempo % 12 < 12:
            self.image = self.imagens[1]

        game.janela.blit(self.image, (self.rect.left, self.rect.top))
        # pygame.draw.rect(game.janela, (255, 0, 0), self.rect, 2)