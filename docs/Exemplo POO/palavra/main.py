from Palavra import *
from os import system

class Jogo():
	def __init__(self):
		self.palavra = []
		self.resposta = []
		self.exit = 'S'

	def criarPalavra(self):
		self.palavra = Palavra()

	def jogar(self):
		self.palavra.receberPistas()
		self.palavra.informarPistas()
		self.resposta = input("Qual a palavra? ")
		if self.resposta == self.palavra.palavra:
			print("Parabéns você fez ", self.palavra.pontos, " pontos")
		else:
			print("Errado! Jogue novamente =D")

	def run(self):
		while self.exit != 'N' and self.exit != 'n':
			system('cls')
			self.palavra = []
			self.resposta = []
			self.criarPalavra()
			self.jogar()
			self.exit = input("Você quer jogar? (S/N) ")


game = Jogo()
game.run()