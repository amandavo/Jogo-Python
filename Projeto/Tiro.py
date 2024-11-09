from Cenario import *
from Configuracoes import *
import pygame
import math
import os

class Tiro(Cenario):
    def __init__(self, x, y, tipo, vel):
        self.carregarImagemTiro(tipo)
        super().__init__(x, y, self.imagem, vel)

    # carregar a imagem do tiro
    def carregarImagemTiro(self, tipo):
        self.imagem = pygame.image.load(os.path.join('Imagens', 'tiro.png'))

        #Inverter a imagem para o tiro do inimigo
        if tipo == 'I':
            self.imagem = pygame.transform.flip(self.imagem, 1, 0)

    # atualiza a posicao do tiro apos disparado
    def atualizar(self, tela):
        self.atualizacaoBasica()

    # verifica as colisoes do tiro com o inimigo
    def checarColisoes(self, game, tiro):
        # lembrar que se o personagem tiver vidas e se chocar contra os obstaculos, ele nao deve morrer mas sim perder uma vida
        # lembrar que se a booleana telaDeJogo.jogador.ehInvencivel for verdadeira as colisoes com obstaculos devem ser ignoradas
        #adicionar colisao do tiro do personagem com o tiro do inimigo

        for tiroInimigo in game.tirosInimigo:
            for tiros in game.tiros:
                if tiros.vel < 0 and tiros.rect.colliderect(tiroInimigo):
                    # fazer o tiro do jogador e do inimigo desaparecerem a cada colisao entre eles
                        game.tiros.pop(game.tiros.index(tiro))
                        game.tirosInimigo.pop(game.tirosInimigo.index(tiroInimigo))

        if self.vel > 0 and self.rect.colliderect(game.jogador):
            colisoes = pygame.sprite.spritecollide(game.jogador, game.tirosInimigo, False)
            callback = pygame.sprite.collide_mask
            colisao = pygame.sprite.spritecollideany(game.jogador, colisoes, callback)
            if colisao:
                if game.ehInvencivel:
                    game.tirosInimigo.pop(game.tirosInimigo.index(self))
                elif game.vidasExtras > 0:
                    game.tirosInimigo.pop(game.tirosInimigo.index(self))
                    game.vidasExtras = game.vidasExtras - 1
                else:
                    game.ultimaTela = 'Tela de Jogo'
                    game.telaAtual = 'Tela de Fim'


        for inimigo in game.inimigos:
            if self.vel < 0 and self.rect.colliderect(inimigo):
                colisoes = pygame.sprite.spritecollide(inimigo, game.tiros, False)
                callback = pygame.sprite.collide_mask
                colisao = pygame.sprite.spritecollideany(inimigo, colisoes, callback)
                if colisao:
                    if inimigo.vida > 0:
                        inimigo.vida = inimigo.vida - 1
                        game.inimigos.pop(game.inimigos.index(inimigo))
                        game.tiros.pop(game.tiros.index(self ))