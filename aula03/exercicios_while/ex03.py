acerto = 3
tentativas = 3
num  = 0


while num != acerto and tentativas > 0:
    num = int(input("Digite um número de 1 a 10: "))
    print("número errado, tente novamente ")
    tentativas -=1
while num ==acerto:
    print("parabéns, você acertou!")
    break
print("fim do jogo")