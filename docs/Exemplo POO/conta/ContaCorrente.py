class ContaCorrente(object):
	#Construtor
	def __init__(self):
		#Atributos
		self.numeroDaConta = []
		self.nomeDoCorrentista = []
		self.saldo = 0

	#Métodos	
	def alterarNome(self, novoNome):
		self.nomeDoCorrentista = novoNome

	def alterarNumero(self, novoNumero):
		self.numeroDaConta = novoNumero

	def deposito(self, valorDoDeposito):
		self.saldo += valorDoDeposito

	def saque(self, valorDoSaque):
		self.saldo -= valorDoSaque

	def consultarSaldo(self):
		print("Saldo da conta:", self.saldo)

		