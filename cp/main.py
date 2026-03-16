# ====================================== EX01 ======================================
# Crie um programa em Python que verifique se uma pessoa pode entrar em um evento 
# se for maior de 18 anos.

entrada = 18
idade = int(input("Digite sua idade: "))

if idade >= entrada:
    print ("Você pode entrar no evento!")
else:
    print ("Você não pode entrar no evento")

# ==================================== FIM EX01 ====================================


# ====================================== EX02 ======================================
# Crie um programa em Python que compare dois números, peça ao usuario os numeros e
# compare se eles são iguais.


num1 = int(input("Digite um número:"))
num2 = int(input("Digite outro número: "))

if num1 == num2:
    print("Os números são iguais ")
else:
    print("Os números são diferentes ")

# ==================================== FIM EX02 ====================================

# ====================================== EX03 ======================================
# Crie um programa em Python que registre 3 notas de um aluno e determine 
# sua situação na disciplina, peça ao usuario as 3 notas e salve em uma lista, tire 
# a media e se for 7 ou maior ele passou na materia.

aprovado = 7
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))


notas = [nota1, nota2, nota3]
media = (notas[0] + notas[1] + notas[2]) / 3

if media >= aprovado:
        print("Você está aprovado ")
else:
        print("Reprovado! ")


# ==================================== FIM EX03 ====================================