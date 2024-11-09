from Cenario import *
import pygame

class Impulsionador(Cenario):
    def __init__(self, x, y, imagem, vel):
        super().__init__(x, y, imagem, vel)

    def atualizar(self, game):
        self.atualizacaoBasica()

    # verifica as colisoes do personagem principal com o impulsionador
    def checarColisoes(self, game):
        # fazer a variavel game.ehInvencivel ser verdadeira caso ocorra a colisao entre o personagem principal e o impulsionador
        # fazer o impulsionador desaparecer depois da colisao
        if self.rect.colliderect(game.jogador):
            colisoes = pygame.sprite.spritecollide(game.jogador, game.impulsionadores, False)
            callback = pygame.sprite.collide_mask
            colisao = pygame.sprite.spritecollideany(game.jogador, colisoes, callback)
            if colisao:
                game.impulsionadores.pop(game.impulsionadores.index(self))
                game.ehInvencivel = True

                pygame.mixer.pause()
                game.administradorDeAudio.tocarEfeitoSonoro(os.path.join('Musica', 'laser.wav'), game)
                game.administradorDeAudio.tocarMusicaDeFundo(os.path.join('Musica', 'music3.wav'), game)
