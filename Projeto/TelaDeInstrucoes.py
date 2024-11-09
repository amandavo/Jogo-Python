from Configuracoes import *
from Tela import *
import pygame
import os

class TelaDeInstrucoes(Tela):
   def __init__(self,game):
       super().__init__()
       self.name = "Tela de Instrucoes"
       fonte1 = self.font = pygame.font.Font(os.path.join('Fontes', 'TOONISH.ttf'), 70)
       self.title = fonte1.render('INSTRUCOES', True, AMARELO)
       self.fonte2 = self.font = pygame.font.Font(os.path.join('Fontes', 'TOONISH.ttf'), 30)
       self.voltar = self.fonte2.render('VOLTAR', True, AZULBB)
       self.botaoPlay = self.play = pygame.image.load(os.path.join('Imagens', 'play_1.png'))
       self.jogador = pygame.image.load(os.path.join('Imagens', 'personagem_principal_FEC_1.png'))

   # metodo para lidar com interacoes com o botao de jogar
   def comportamentoBotaoDeJogar(self, game, evento, pos):
       # verifica se o usuario esta com o cursor em cima da imagem do botao
       if pos[0] > 980 and pos[0] < 1041 and pos[1] > 599 and pos[1] < 661:
           if evento.type == pygame.MOUSEBUTTONDOWN:
               game.ultimaTela = 'Tela de Fim'
               game.telaAtual = 'Tela de Inicio'
           else:
               self.botaoPlay = self.play = pygame.image.load(os.path.join('Imagens', 'play_brilho_3.png'))
       else:
           self.botaoPlay = self.play = pygame.image.load(os.path.join('Imagens', 'play_3.png'))

   # metodo para lidar com interacoes com o botao que redireciona para a tela de inicio
   def comportamentoBotaoVoltarTelaInicio(self, game, evento, pos):
       if pos[0] > 30 and pos[0] < 129 and pos[1] > 30 and pos[1] < 54:
           if evento.type == pygame.MOUSEBUTTONDOWN:
               game.ultimaTela = 'Tela de Inicio'
               game.telaAtual = 'Tela de Instrucoes'
           else:
               self.voltar = self.fonte2.render('VOLTAR', True, BRANCO)
       else:
           self.voltar = self.fonte2.render('VOLTAR', True, AZULBB)

   def interpretarEventos(self, game):
       game.clock.tick(game.fps)

       for evento in pygame.event.get():
           pos = pygame.mouse.get_pos()

           # checa se o usuario quer sair do jogo
           self.comportamentoBotaoDeSair(game, evento)

           # checa se o usuario quer tirar o som
           self.comportamentoBotaoDeAudio(game, evento, pos)

           # checa se o usuario quer jogar
           self.comportamentoBotaoDeJogar(game, evento, pos)

           # checa se o usuario quer voltar para a tela de inicio
           self.comportamentoBotaoVoltarTelaInicio(game, evento, pos)

           print("pos0: ", pos[0], " pos1: ", pos[1])

   def imprimirInstrucoes(self, game, num, text):
       # carrega a instrucao com a fonte 2 e a cor azul bebe
       instrucao = self.fonte2.render(text, True, AZULBB)

       # posiciona a instrucao na tela
       game.janela.blit(instrucao, (70, 170 + 100 * (num - 1)))

   # esse metodo deve desenhar tudo que tem na tela, exceto tela de fundo e botao de audio
   def desenharTela(self, game):
       # imprimindo a primeira instrucao do jogo com o auxilio do metodo imprimirInstrucoes
       self.imprimirInstrucoes(game, 1, '- Evite os obstaculos clicando na seta para cima para pular.')
       self.imprimirInstrucoes(game, 2, '- Pressione a barra de espaco para atirar nos inimigos.')
       self.imprimirInstrucoes(game, 3, '- Colete coracoes para ter a possibilidade de ganhar vidas extras.')
       self.imprimirInstrucoes(game, 4, '- Colete boosters para ficar invencivel por 15s.')
       self.imprimirInstrucoes(game, 5, '- Clique no icone de som para desliga-lo.')
       game.janela.blit(self.title, (460, 50))
       game.janela.blit(self.botaoPlay, (980, 600))
       game.janela.blit(self.voltar, (30, 30))

   def desenhar(self, game):
       self.desenharTelaBasica(game)
       self.desenharTela(game)
       pygame.display.flip()


   def run(self, game):
       while game.telaAtual == self.name and not game.usuarioSaiu:
           self.interpretarEventos(game)
           self.desenhar(game)


