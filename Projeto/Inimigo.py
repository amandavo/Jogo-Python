from Cenario import *
from Tiro import *
import pygame
import os
import math
import random

class Inimigo(Cenario):
    def __init__(self, x, y, imagem, vel, vida, tipo):
        super().__init__(x, y, imagem, vel)
        self.vida = vida
        self.tempo = pygame.time.get_ticks()
        self.velY = -2.5 *vel
        self.tipo = tipo

    # metodo responsavel pela movimentacao do inimigo na tela
    def atualizar(self, game):
        self.atualizacaoBasica()
        r = random.randrange(0, 75)
        if not r:
            game.tirosInimigo.append(Tiro(self.x-30, self.y, 'I', 10 + game.dvel))

        # Equações de Movimento
        dt = 1

        if self.tipo == '1':
            acc = 0.014*self.vel*self.vel

            # Atualizar velocidade e posição do inimigo
            self.velY += acc*dt
            self.y += self.velY*dt
            self.rect.top = self.y
            if self.y >= (Y_CHAO) - self.altura:
                self.y = (Y_CHAO) - self.altura
                self.velY = -2.5 * self.vel
        elif self.tipo == '3':
            # Atualizar velocidade e posição do inimigo
            if self.y < 380:
                self.velY = -self.vel
            elif self.y > Y_CHAO - self.altura:
                self.velY = self.vel

            self.y -= self.velY * dt
            self.rect.top = self.y

    # verifica as colisoes do personagem com o inimigo
    def checarColisoes(self, game):
        # lembrar que se o personagem tiver vidas e se chocar contra inimigos, ele nao deve morrer mas sim perder uma vida
        # lembrar que se a booleana game.ehInvencivel for verdadeira as colisoes com inimigos devem ser ignoradas
        if self.rect.colliderect(game.jogador):
            colisoes = pygame.sprite.spritecollide(game.jogador, game.inimigos, False)
            callback = pygame.sprite.collide_mask
            colisao = pygame.sprite.spritecollideany(game.jogador, colisoes, callback)
            if colisao:
                if game.ehInvencivel:
                    game.inimigos.pop(game.inimigos.index(self))
                else:
                    pygame.mixer.pause()
                    game.administradorDeAudio.tocarEfeitoSonoro(os.path.join('Musica', 'death.wav'), game)
                    pygame.time.wait(3100)
                    game.ultimaTela = 'Tela de Jogo'
                    game.telaAtual = 'Tela de Fim'