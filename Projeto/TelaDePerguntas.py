#coding: utf-8
from Configuracoes import *
from Tela import *
import random
import pygame
import os

class TelaDePerguntas(Tela):
    def __init__(self, game):
        super().__init__()
        self.name = 'Tela de Perguntas'
        self.altA = pygame.image.load(os.path.join('Imagens', 'alternativa_A.png'))
        self.altB = pygame.image.load(os.path.join('Imagens', 'alternativa_B.png'))
        self.altC = pygame.image.load(os.path.join('Imagens', 'alternativa_C.png'))
        self.altD = pygame.image.load(os.path.join('Imagens', 'alternativa_D.png'))
        self.pergunta = 0
        self.altATexto = 0
        self.altBTexto = 0
        self.altCTexto = 0
        self.altDTexto = 0

        self.fonte1 = pygame.font.Font(os.path.join('Fontes', 'TOONISH.ttf'), 40)
        self.fonte2 = self.font = pygame.font.Font(os.path.join('Fontes', 'TOONISH.ttf'), 40)
        self.pular = self.fonte2.render("Pular", True, AZULBB)


        game.administradorDeAudio.tocarMusicaDeFundo(os.path.join('Musica', 'music2.wav'), game)


    # metodo para carregar a pergunta da tela
    def carregarPergunta(self, game):
        pass


    # metodo para lidar com a escolha da alternativa A
    # se a escolha do usuário for igual à resposta correta, dá tudo certo
    # se não, aparece mensagem negativa na outra tela, a de resultado da pergunta
    def comportamentoBotaoAlternativaA(self, game, evento, pos):
        pass


    # metodo para lidar com a escolha da alternativa B
    def comportamentoBotaoAlternativaB(self, game, evento, pos):
        pass

    # metodo para lidar com a escolha da alternativa C
    def comportamentoBotaoAlternativaC(self, game, evento, pos):
        pass


    # metodo para lidar com a escolha da alternativa D
    def comportamentoBotaoAlternativaD(self, game, evento, pos):
        pass

    def comportamentoBotaoPular(self, game, evento, pos):
        pass


    def interpretarEventos(self, game):
        game.clock.tick(game.fps)

        for evento in pygame.event.get():
            pos = pygame.mouse.get_pos()

            # checa se o usuario quer sair do jogo
            self.comportamentoBotaoDeSair(game, evento)

            # checa se o usuario quer tirar o som
            self.comportamentoBotaoDeAudio(game, evento, pos)

            # checa se o usuario escolheu a alternativa A
            self.comportamentoBotaoAlternativaA(game, evento, pos)

            # checa se o usuario escolheu a alternativa B
            self.comportamentoBotaoAlternativaB(game, evento, pos)

            # checa se o usuario escolheu a alternativa C
            self.comportamentoBotaoAlternativaC(game, evento, pos)

            # checa se o usuario escolheu a alternativa D
            self.comportamentoBotaoAlternativaD(game, evento, pos)

            # checa se o usuario escolheu pular a alternativa
            self.comportamentoBotaoPular(game, evento, pos)


    # esse metodo deve desenhar tudo que tem na tela, exceto tela de fundo e botao de audio
    def desenharTela(self, game):
        game.janela.blit(self.pergunta, (100, 90))

        game.janela.blit(self.altA, (140, 200))
        game.janela.blit(self.altATexto, (210, 215))

        game.janela.blit(self.altB, (140, 320))
        game.janela.blit(self.altBTexto, (210, 335))

        game.janela.blit(self.altC, (140, 440))
        game.janela.blit(self.altCTexto, (210, 455))

        game.janela.blit(self.altD, (140, 560))
        game.janela.blit(self.altDTexto, (210, 575))

        game.janela.blit(self.pular, (1070, 650))


    def desenhar(self, game):
        self.desenharTelaBasica(game)
        self.desenharTela(game)
        pygame.display.flip()


    def run(self, game):

        self.carregarPergunta(game)

        while game.telaAtual == self.name and not game.usuarioSaiu:
            self.interpretarEventos(game)
            self.desenhar(game)


