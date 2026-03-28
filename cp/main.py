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


# ====================================== EX04 ======================================
# Crie um programa em Python que registre 5 produtos comprados em um mercado. 
# Use Listas, laço for e inputs.

produtos = []
for i in range(5):
    produto = input("digite o nome do produto: ")
    produtos.append(produto)
    print("Produto adicionado com sucesso ")
           
# ==================================== FIM EX04 ====================================

# ====================================== EX05 ======================================
# Crie um programa em Python que registre 5 números digitados pelo usuário e 
# depois mostre algumas informações sobre eles, use laço For.
# 1 - A lista completa de números
# 2 - O maior número
# 3 - O menor número
# 4 - A soma de todos os números

numeros = []

for i in range(5):
    numeros.append(int(input("Digite um número: ")))

print("Lista:", numeros)

maior = numeros[0]
menor = numeros[0]
soma = 0

for i in range(5):
    if numeros[i] > maior:
        maior = numeros[i]
    if numeros[i] < menor:
        menor = numeros[i]
    soma = soma + numeros[i]

print("Maior:", maior)
print("Menor:", menor)
print("Soma:", soma)
# ==================================== FIM EX05 ====================================

# ====================================== EX06 ======================================
# Crie um programa em Python que peça números ao usuário e some todos eles.
# Use o laço while e receba numeros ate que uma condição seja atendida.

soma = 0
num = 0

while num != -1:
    num = int(input("Digite um número (-1 para parar): "))
    if num != -1:
        soma += num

print("Soma total:", soma)

# ==================================== FIM EX06 ====================================

# ====================================== EX07 ======================================
# Crie um programa em Python que simule um sistema simples de login.
# Usar um primeiro laço while para pedir o nome de usuário até que 
# o usuário digite o valor correto, faça o mesmo para a senha.
usuario_correto = "joao"
senha_correta = "333"

usuario = ""

while usuario != usuario_correto:
    usuario = input("Digite o usuário: ")

senha = ""

while senha != senha_correta:
    senha = input("Digite a senha: ")

print("Login realizado com sucesso!")

# ==================================== FIM EX07 ====================================

# ====================================== EX08 ======================================
# Crie um programa em Python que registre 3 notas de alunos, garantindo que 
# cada nota seja válida, use as estruturas de laço for e while.

notas = []

for i in range(3):
    nota = -1
    while nota < 0 or nota > 10:
        nota = float(input("Digite uma nota (0 a 10): "))
    notas.append(nota)

print("Notas:", notas)

# ==================================== FIM EX08 ====================================

# ====================================== EX09 ======================================
# Crie um programa em Python que registre números digitados pelo usuário e 
# conte quantos são positivos. Use o laço while para registrar todas as entradas
# depois use o laço for para percorrer toda a lista e fazer a contagem.
numeros = []
num = 0

while num != -1:
    num = int(input("Digite um número (-1 para parar): "))
    if num != -1:
        numeros.append(num)

positivos = 0

for n in numeros:
    if n > 0:
        positivos += 1

print("Quantidade de positivos:", positivos)

# ==================================== FIM EX09 ====================================

# ====================================== EX10 ======================================
# Crie um programa em Python que registre as notas de 3 alunos em 4 provas usando
# uma matriz (lista de listas), calcule a media de cada aluno.
# Use seu conhecimento de laços para cumprir a tarefa.

notas = []

for i in range(3):
    aluno = []
    for j in range(4):
        nota = float(input("Digite a nota: "))
        aluno.append(nota)
    notas.append(aluno)

for i in range(3):
    soma = 0
    for j in range(4):
        soma += notas[i][j]
    media = soma / 4
    print("Média do aluno", i+1, ":", media)notas = []

for i in range(3):
    aluno = []
    for j in range(4):
        nota = float(input("Digite a nota: "))
        aluno.append(nota)
    notas.append(aluno)

for i in range(3):
    soma = 0
    for j in range(4):
        soma += notas[i][j]
    media = soma / 4
    print("Média do aluno", i+1, ":", media)

# ==================================== FIM EX10 ====================================