#Importar classe ContaCorrente do arquivo ContaCorrente
from ContaCorrente import *

#Criar novo objeto ContaCorrete guardado na variável conta
conta = ContaCorrente()

#Testas método alterarNome
conta.alterarNome("Maria")
print(conta.nomeDoCorrentista)

#Testas método alterarNumero
conta.alterarNumero(12345)
print(conta.numeroDaConta)

#Testas método deposito
conta.deposito(500)
print(conta.saldo)

#Testas método saque
conta.saque(100)
print(conta.saldo)

#Testas método consultarSaldo
conta.consultarSaldo

conta.deposito(1000)
print(conta.saldo)

conta.saque(300)
print(conta.saldo)