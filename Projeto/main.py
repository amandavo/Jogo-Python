from TelaDeInicio import *
from TelaDeInstrucoes import *
from TelaDeJogo import *
from TelaDePerguntas import *
from TelaResultadoDaPergunta import *
from TelaDeFim import *
from Configuracoes import *
from AdministradorDeAudio import *
from Jogador import *
import pygame
import random

class AdministradorDoJogo:
    def __init__(self):
        # inicializando pygame
        pygame.init()

        # criando a janela do jogo
        self.janela = pygame.display.set_mode((LARGURA_DA_TELA, ALTURA_DA_TELA))
        pygame.display.set_caption(TITULO)

        # criando o relogio do jogo
        self.clock = pygame.time.Clock()
        self.fps = FPS

        # inicializando constantes do jogo
        self.telaAtual = 'Tela de Inicio'
        self.ultimaTela = 'Tela de Fim'
        self.tela = 0
        self.usuarioSaiu = False
        self.comAudio = True
        self.melhorPontuacao = 0

        self.administradorDeAudio = AdministradorDeAudio()

        self.obstaculos = []
        self.inimigos = []
        self.vidas = []
        self.impulsionadores = []
        self.tiros = []
        self.tirosInimigo = []

        self.perguntas = []
        self.alternativaA = []
        self.alternativaB = []
        self.alternativaC = []
        self.alternativaD = []
        self.respostas = []
        self.i = 0

        self.inserirPerguntas()

        self.novoJogo()

    def tocarMusicaDeFundo(self, musica, game):
        # lembrar de checar se o jogo esta com audio ou nao
        # usar 1 canal para a musica de fundo e outro para os efeitos sonoros
        if (game.comAudio):
            pygame.mixer.Channel(0).play(pygame.mixer.Sound(musica), -1)
            pygame.mixer.Channel(0).set_volume(1)

    # metodo para declarar todas as perguntas do jogo
    def inserirPerguntas(self):
        pass

    def retirarPergunta(self):
        pass

    # esse metodo inicializa as constantes do jogo a cada novo jogo
    def novoJogo(self):
        self.pontuacao = 0
        self.aparecimentoElementos = 50
        self.vidasExtras = 3
        self.ehInvencivel = False
        self.respostaCorreta = 0
        self.respostaUsuario = 0
        self.tempoDeInvencibilidade = 15
        self.dvel = 0
        self.jogador = Jogador(self)
        self.obstaculos.clear()
        self.inimigos.clear()
        self.vidas.clear()
        self.impulsionadores.clear()
        self.tiros.clear()
        self.tirosInimigo.clear()


    # metodo que executa o jogo, alternando entre as telas do jogo, de acordo com os comandos do usuario
    def run(self):
        while not self.usuarioSaiu:
            if self.telaAtual == 'Tela de Inicio':
                self.tela = TelaDeInicio(self)
            elif self.telaAtual == 'Tela de Instrucoes':
                self.tela = TelaDeInstrucoes(self)
            elif self.telaAtual == 'Tela de Jogo':
                self.tela = TelaDeJogo(self)
            elif self.telaAtual == 'Tela de Perguntas':
                self.tela = TelaDePerguntas(self)
            elif self.telaAtual == 'Tela Resultado da Pergunta':
                self.tela = TelaResultadoDaPergunta()
            else:
                self.tela = TelaDeFim(self)

            self.tela.run(self)

        pygame.quit()


game = AdministradorDoJogo()
game.run()