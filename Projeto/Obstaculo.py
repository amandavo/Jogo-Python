from Cenario import *
import pygame

class Obstaculo(Cenario):
    def __init__(self, x, y, imagem, vel):
        super().__init__(x, y, imagem, vel)
        self.x = x
        self.y = y
        self.image = imagem
        self.largura = imagem.get_width()
        self.altura = imagem.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)  # retangulo de colisoes
        self.vel = vel  # velocidade de atualizacao horizontal na tela

    def atualizar(self, game):
        self.atualizacaoBasica()

    # desenha o item do cenario na tela
    def desenhar(self, game):
        game.janela.blit(self.image, (self.x, self.y))
        #pygame.draw.rect(game.janela, (255, 0, 0), self.rect, 2)

    # verifica as colisoes do personagem principal com obstaculos do cenario
    def checarColisoes(self, game):
        # lembrar que se o personagem tiver vidas e se chocar contra os obstaculos, ele nao deve morrer mas sim perder uma vida
        # lembrar que se a booleana telaDeJogo.jogador.ehInvencivel for verdadeira as colisoes com obstaculos devem ser ignoradas
        if self.rect.colliderect(game.jogador):
            colisoes = pygame.sprite.spritecollide(game.jogador, game.obstaculos, False)
            callback = pygame.sprite.collide_mask
            colisao = pygame.sprite.spritecollideany(game.jogador, colisoes, callback)
            if colisao:
                if game.ehInvencivel:
                    game.obstaculos.pop(game.obstaculos.index(self))
                else:
                    if game.vidasExtras > 0:
                        game.obstaculos.pop(game.obstaculos.index(self))
                        game.vidasExtras = game.vidasExtras - 1
                    else:
                        game.ultimaTela = 'Tela de Jogo'
                        game.telaAtual = 'Tela de Fim'