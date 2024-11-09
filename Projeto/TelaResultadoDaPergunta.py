#from Configuracoes import *
from Tela import *
import pygame
import os


class TelaResultadoDaPergunta(Tela):
   def __init__(self):
       super().__init__()
       self.name = 'Tela Resultado da Pergunta'
       self.fonte1 = pygame.font.Font(os.path.join('Fontes', 'TOONISH.ttf'), 95)
       self.fonte2 = pygame.font.Font(os.path.join('Fontes', 'TOONISH.ttf'), 60)
       self.fonte3 = pygame.font.Font(os.path.join('Fontes', 'TOONISH.ttf'), 50)
       self.respCorreta = self.fonte1.render('RESPOSTA CORRETA!', True, AMARELO)
       self.mensCorreta = self.fonte2.render('Desfrute de uma vida extra!', True, PRETO)
       self.respIncorreta = self.fonte1.render('RESPOSTA INCORRETA...', True, AMARELO)
       self.mensIncorreta = self.fonte2.render('Tente novamente...', True, PRETO)
       self.continuar = self.fonte3.render('CONTINUAR', True, AZULBB)
       self.jogador = pygame.image.load(os.path.join('Imagens', 'personagem_principal_FEC_1.png'))


   def comportamentoBotaoContinuar(self, game, evento, pos):
       pass


   def interpretarEventos(self, game):
       game.clock.tick(game.fps)

       for evento in pygame.event.get():
           pos = pygame.mouse.get_pos()

           # checa se o usuario quer sair do jogo
           self.comportamentoBotaoDeSair(game, evento)

           # checa se o usuario quer tirar o som
           self.comportamentoBotaoDeAudio(game, evento, pos)

           self.comportamentoBotaoContinuar(game, evento, pos)



   # esse metodo deve desenhar tudo que tem na tela, exceto tela de fundo e botao de audio
   def desenharTela(self, game):
       game.janela.blit(self.continuar, (940, 650))

       # se a resposta for a correta, desenhar o aviso de parabéns
       if game.respostaCorreta == game.respostaUsuario:
           game.janela.blit(self.respCorreta, (210, 200))
           game.janela.blit(self.mensCorreta, (230, 430))

       # caso contrário, desenhar o aviso de game over
       else:
           game.janela.blit(self.respIncorreta, (200, 200))
           game.janela.blit(self.mensIncorreta, (380, 430))


   def desenhar(self, game):
       self.desenharTelaBasica(game)
       self.desenharTela(game)
       pygame.display.flip()


   def run(self, game):
       if game.respostaCorreta == game.respostaUsuario:
           game.vidasExtras += 1

       while game.telaAtual == self.name and not game.usuarioSaiu:
           self.interpretarEventos(game)
           self.desenhar(game)