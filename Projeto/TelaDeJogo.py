from Configuracoes import *
from Tela import *
from Jogador import *
from Obstaculo import *
from Vida import *
from Impulsionador import *
from Inimigo import *
from Tiro import *
import pygame
import random
import os
from pygame.locals import *

class TelaDeJogo(Tela):
    def __init__(self, game):

        super().__init__()
        self.name = "Tela de Jogo"
        self.fonte1 = pygame.font.Font(os.path.join('Fontes', 'TOONISH.ttf'), 35)
        self.fonte2 = pygame.font.Font(os.path.join('Fontes', 'TOONISH.ttf'), 160)
        self.batalha = False
        game.novoJogo()

        # inicializando jogador e vetor para armazenar outros elementos do jogo
        self.tolerancia = game.jogador.largura*2.1
        game.administradorDeAudio.tocarMusicaDeFundo(os.path.join('Musica', 'music3.wav'), game)

    def computarPontuacao(self, game):
        game.pontuacao += 1

    def imprimirPontuacao(self, game):
        if game.pontuacao:
            self.pontuacao = self.fonte1.render("SCORE: ", True, AZULBB)
            self.pontuacaoNum = self.fonte1.render(str(game.pontuacao), True, AZULBB)
            game.janela.blit(self.pontuacao, (LARGURA_DA_TELA - 335, ALTURA_DA_TELA - 700))
            game.janela.blit(self.pontuacaoNum, (LARGURA_DA_TELA - 215, ALTURA_DA_TELA - 700))

    # imprime barra de vidas
    def imprimirBarraDeVidas(self, game):
        if game.vidasExtras > 0:
            for i in range(game.vidasExtras):
                game.janela.blit(pygame.image.load(os.path.join('Imagens', 'vida.png')), (70*i + 20, 20))

    def computarTempoDeInvencibilidade(self, game):
        if game.ehInvencivel:
            if game.tempoDeInvencibilidade > 0:
                game.tempoDeInvencibilidade -= 1
            else:
                game.ehInvencivel = False
                game.tempoDeInvencibilidade = 15

    # imprime tempo de invencibilidade na Tela a partir do momento em que a varivel game.ehInvencivel se tornar verdadeira, por x segundos
    def imprimirTempoDeInvencibilidade(self, game):
        if game.ehInvencivel:
            self.invencibilidade = self.fonte1.render("INVENCIBILIDADE: ", True, AZULBB)
            self.invencibilidadeNum = self.fonte1.render(str(game.tempoDeInvencibilidade), True, AZULBB)
            game.janela.blit(self.invencibilidade, (LARGURA_DA_TELA - 335, ALTURA_DA_TELA - 50))
            game.janela.blit(self.invencibilidadeNum, (LARGURA_DA_TELA - 60, ALTURA_DA_TELA - 50))

    # cria itens do cenario na tela
    def criarCenario(self, game):
        # geracao de numero aleatorio
        # game.aparecimentoElementos eh uma constante que vale, inicialmente, 50
        r = random.randrange(0, game.aparecimentoElementos)
        # se o numero gerado for menor que 8
        if r < 12:
            if len(game.obstaculos) == 0 or (len(game.obstaculos) != 0 and game.obstaculos[-1].x +
                                             game.obstaculos[-1].largura + self.tolerancia < LARGURA_DA_TELA):
                # adiciona um obstaculo no jogo, na posicao (LARGURA_DA_TELA, 562) com velocidade 5
                game.obstaculos.append(Obstaculo(LARGURA_DA_TELA, 562, pygame.image.load(os.path.join('Imagens','obstaculo_1_1.png')), 12 + game.dvel))
        elif r < 16:
            if len(game.obstaculos) == 0 or (len(game.obstaculos) != 0 and game.obstaculos[-1].x +
                                             game.obstaculos[-1].largura + self.tolerancia < LARGURA_DA_TELA):
                # adiciona um obstaculo no jogo, na posicao (LARGURA_DA_TELA, 562) com velocidade 5
                game.obstaculos.append(Obstaculo(LARGURA_DA_TELA, 562, pygame.image.load(os.path.join('Imagens','obstaculo_1_2.png')), 12 + game.dvel))

        elif r > 47:
            if len(game.vidas) == 0 or (len(game.vidas) != 0 and game.vidas[-1].x +
                                             game.vidas[-1].largura + self.tolerancia < LARGURA_DA_TELA):
                # adiciona um obstaculo no jogo, na posicao (LARGURA_DA_TELA, 562) com velocidade 5
                game.vidas.append(Vida(LARGURA_DA_TELA, 562, pygame.image.load(os.path.join('Imagens','vida.png')), 12))

        elif r > 45:
            if len(game.impulsionadores) == 0 or (len(game.impulsionadores) != 0 and game.impulsionadores[-1].x +
                                             game.impulsionadores[-1].largura + self.tolerancia < LARGURA_DA_TELA):
                # adiciona um obstaculo no jogo, na posicao (LARGURA_DA_TELA, 562) com velocidade 5
                game.impulsionadores.append(Impulsionador(LARGURA_DA_TELA, 562, pygame.image.load(os.path.join('Imagens','impulsionador_2.png')), 12))

        elif r < 20:
            if len(game.obstaculos) == 0 or (len(game.obstaculos) != 0 and game.obstaculos[-1].x +
                                             game.obstaculos[-1].largura + self.tolerancia < LARGURA_DA_TELA):
                # adiciona um obstaculo no jogo, na posicao (LARGURA_DA_TELA, 562) com velocidade 5
                game.obstaculos.append(
                    Obstaculo(LARGURA_DA_TELA, 562, pygame.image.load(os.path.join('Imagens', 'obstaculo_3_1.png')),
                              12 + game.dvel))
        elif r < 25:
            if len(game.obstaculos) == 0 or (len(game.obstaculos) != 0 and game.obstaculos[-1].x +
                                             game.obstaculos[-1].largura + self.tolerancia < LARGURA_DA_TELA):
                # adiciona um obstaculo no jogo, na posicao (LARGURA_DA_TELA, 562) com velocidade 5
                game.obstaculos.append(
                    Obstaculo(LARGURA_DA_TELA, 562, pygame.image.load(os.path.join('Imagens', 'obstaculo_3_2.png')),
                              12 + game.dvel))

    def aparecimentoInimigos(self, game):
        if len(game.obstaculos) == 0 or game.obstaculos[-1].x + game.obstaculos[-1].largura + self.tolerancia < LARGURA_DA_TELA:
            game.inimigos.append(Inimigo(LARGURA_DA_TELA, 563, pygame.image.load(os.path.join('Imagens', 'inimigo_3.png')), 5 + game.dvel,
                    int(game.pontuacao / 25), '1'))

    def checarComportamentoJogador(self, game, evento):
        # verificar se o usuario pediu para o jogador fazer algum comando (atirar ou pular)
        if evento != [] and evento.type == pygame.KEYDOWN: #verificar se há algo na fila de eventos e se há teclas precionadas
            if evento.key == pygame.K_UP:
                game.jogador.pular(game)
            elif evento.key == pygame.K_SPACE:
                game.jogador.atirar(game)


    def checarColisoes(self, game):
        for obstaculo in game.obstaculos:
            obstaculo.checarColisoes(game)

        for vida in game.vidas:
            vida.checarColisoes(game)

        for impulsionador in game.impulsionadores:
            impulsionador.checarColisoes(game)

        for inimigo in game.inimigos:
            inimigo.checarColisoes(game)

        for tiro in game.tiros:
            tiro.checarColisoes(game, tiro)

        for tiroInimigo in game.tirosInimigo:
            tiroInimigo.checarColisoes(game, tiroInimigo)

    def atualizar(self, game):
        game.jogador.atualizar(game)

        for obstaculo in game.obstaculos:
            obstaculo.atualizar(game)
            if obstaculo.x < - obstaculo.largura - 20:
                game.obstaculos.pop(game.obstaculos.index(obstaculo))

        for vida in game.vidas:
            vida.atualizar(game)
            if vida.x < - vida.largura - 20:
                game.vidas.pop(game.vidas.index(vida))

        for impulsionador in game.impulsionadores:
            impulsionador.atualizar(game)
            if impulsionador.x < - impulsionador.largura - 20:
                game.impulsionadores.pop(game.impulsionadores.index(impulsionador))

        for inimigo in game.inimigos:
            inimigo.atualizar(game)
            if inimigo.x < - inimigo.largura - 20:
                game.inimigos.pop(game.inimigos.index(inimigo))

        for tiro in game.tiros:
            tiro.atualizar(game)
            if tiro.x < - tiro.largura - 20:
                game.tiros.pop(game.tiros.index(tiro))
        for tiroInimigo in game.tirosInimigo:
            tiroInimigo.atualizar(game)
            if tiroInimigo.x < - tiroInimigo.largura - 20:
                game.tirosInimigo.pop(game.tirosInimigo.index(tiroInimigo))

        # making background move
        self.imagemDeFundoX -= 2
        if self.imagemDeFundoX < self.imagemDeFundo.get_width() * -1:
            self.imagemDeFundoX = self.imagemDeFundo.get_width()

        self.imagemDeFundoX2 -= 2
        if self.imagemDeFundoX2 < self.imagemDeFundo.get_width() * -1:
            self.imagemDeFundoX2 = self.imagemDeFundo.get_width()

    def interpretarEventos(self, game):
        game.clock.tick(game.fps)

        for evento in pygame.event.get():
            pos = pygame.mouse.get_pos()

            # checa se o usuario quer sair do jogo
            self.comportamentoBotaoDeSair(game, evento)

            # checa se o usuario quer mover o jogador
            self.checarComportamentoJogador(game, evento)

            # checa se o usuario quer tirar o som
            self.comportamentoBotaoDeAudio(game, evento, pos)
            # print('pos 0: ', pos[0], ' pos1: ', pos[1] )

    def desenhar(self, game):
        self.desenharTelaBasica(game)

        for obstaculo in game.obstaculos:
            obstaculo.desenhar(game)

        for vida in game.vidas:
            vida.desenhar(game)

        for impulsionador in game.impulsionadores:
            impulsionador.desenhar(game)

        for inimigo in game.inimigos:
            inimigo.desenhar(game)

        for tiro in game.tiros:
            tiro.desenhar(game)

        for tiroInimigo in game.tirosInimigo:
            tiroInimigo.desenhar(game)

        game.jogador.desenhar(game, self)

        self.imprimirPontuacao(game)

        self.imprimirTempoDeInvencibilidade(game)

        self.imprimirBarraDeVidas(game)

        pygame.display.flip()

    def telaBatalha(self, game):
        pass

    def telaBomTrabalho(self, game):
        pass

    def computarTempoDeBatalha(self, game):
        pass

    def run(self, game):
        self.tempo = 1

        while game.telaAtual == self.name and not game.usuarioSaiu:
            # aumentar a taxa de aparecimento de elementos do cenario
            if game.aparecimentoElementos > 25 and self.tempo % 300 == 0:
                game.aparecimentoElementos -= 1

            # aumentar a velocidade com a qual os elementos do cenario sao inicializados
            if self.tempo % 1200 == 0:
                game.dvel += 1

            if self.tempo % 30 == 0:
                self.criarCenario(game)
                self.computarPontuacao(game)

            # Aparecimento dos inimigos
            if self.tempo % 400 == 0:
                self.aparecimentoInimigos(game)

            self.interpretarEventos(game)
            self.checarColisoes(game)
            self.atualizar(game)
            self.desenhar(game)
            self.tempo += 1

            if game.ehInvencivel and self.tempo % 60 == 0:
                self.computarTempoDeInvencibilidade(game)


