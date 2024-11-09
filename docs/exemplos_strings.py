palavra = input()
tamanho = len(palavra)
tamanhoMetade = int(tamanho/2)
palindromo = True
cont = 0
while (cont < tamanhoMetade and palindromo):
    if(palavra[cont] != palavra[tamanho-cont-1]):
        palindromo = False
    cont = cont + 1
if(palindromo):
    print('Palavra eh palindromo')
else:
    print('Palavra nao eh palindromo')

nome = input()
tamanho = len(nome)
for i in range(1,tamanho+1):
    print(nome[0:i])







