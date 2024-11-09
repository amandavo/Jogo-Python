from Configuracoes import *
import pygame
import os

class Tela:
    def __init__(self):
        self.imagemDeFundo = pygame.image.load(os.path.join('Imagens', 'cenario_3_extendido.png'))
        self.imagemDeFundoX = 0
        self.imagemDeFundoX2 = self.imagemDeFundo.get_width()

    # metodo para lidar com interacoes com o botao de audio, pode ser utilizado em qualquer tela
    def comportamentoBotaoDeAudio(self, game, evento, pos):
        if pygame.key.get_pressed()[pygame.K_m] or evento.type == pygame.MOUSEBUTTONDOWN and pos[0]>1200 and pos[0]<1230 and pos[1]>20 and pos[1]<45:
            if game.comAudio:
                game.administradorDeAudio.deixarSomMudo(game)
            else:
                game.administradorDeAudio.deixarSomTocar(game)

    # metodo para lidar com interacoes com o botao de sair, pode ser utilizado em qualquer tela
    def comportamentoBotaoDeSair(self, game, evento):
        if evento.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            game.usuarioSaiu = True

    # desenha os elementos comuns a toda a tela, isto eh, a tela de fundo e o botao de audio
    def desenharTelaBasica(self, game):

        game.janela.blit(self.imagemDeFundo, (self.imagemDeFundoX, 0))
        game.janela.blit(self.imagemDeFundo, (self.imagemDeFundoX2, 0))

        # carrega a imagem do botao de audio de acordo com o status de audio do jogo
        if game.comAudio:
            self.botaoSom = pygame.image.load(os.path.join('Imagens', 'audio_ligado.png'))
        else:
            self.botaoSom = pygame.image.load(os.path.join('Imagens', 'audio_desligado.png'))
        game.janela.blit(self.botaoSom, (1200, 20))
