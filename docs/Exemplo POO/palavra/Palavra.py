from os import system

class Palavra():
	def __init__(self):
		self.palavra = []
		self.pista1 = []
		self.pista2 = []
		self.pista3 = []
		self.pista4 = []
		self.pista5 = []
		self.pontos = 5;

	def receberPistas(self):
		self.palavra = input("Qual a palavra? ")
		self.pista1 = input("Pista 1: ")
		self.pista2 = input("Pista 2: ")
		self.pista3 = input("Pista 3: ")
		self.pista4 = input("Pista 4: ")
		self.pista5 = input("Pista 5: ")
		system('cls')

	def informarPistas(self):
		continuar = 'S'
		while continuar != 'N' and continuar != 'n':
			self.pontos -= 1
			aux = input("Qual pista você quer? (1-5) ")
			while(aux > '5' or aux < '1'):
				aux = input("Digite um número entre 1 e 5 ")
			
			if aux == '1':
				print(self.pista1)
			elif aux == '2':
				print(self.pista2)
			elif aux == '3':
				print(self.pista3)
			elif aux == '4':
				print(self.pista4)
			else:
				print(self.pista5)
			if self.pontos > 0:
				continuar = input ("Quer mais pistas? (S/N) ")
			else:
				continuar = 'N'
			
			while(continuar !='N' and continuar !='n' and continuar !='S' and continuar !='s'):
				continuar = input ("Digite S ou N ")