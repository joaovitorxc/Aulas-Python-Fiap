#crie funções para realizar operações basicas de uma calculadora(adição, subtração, multiplicação, divisão)com match case. a função deve receber dois números e retornar o resultado da operação

num1 = float(input("digite o primeiro numero: "))
num2 = float(input("digite o segundo numero: "))

def calculadora(num1, num2, operacao):
    match operacao:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            if num2 != 0:
                return num1 / num2
            else:
                return "erro: divisao por zero"
        case _:
            return "operacao invalida"


operacao = input("digite a operacao (+, -, *, /): ")
resultado = calculadora(num1, num2, operacao)

print("o resultado é:", resultado)

#crie uma função que recebe um número e verifica se ele é primo. a função deve retornar true se o número for primo e false caso contrario

num = int(input("digite um numero:"))
def primo(num):
    if num < 2:
        return False
    for i in range(2, int(num)):
        if num % i == 0:
            return False
    return True
if primo(num):
        print(num, "é primo")  
else:
        print(num, "não é primo")  
        
# crie uma função que recebe uma lista de numeros e retorna a media dos elementos
def media(lista):
    if lista:
        soma = 0
        quantidade = 0

        for numero in lista:
            soma = soma + numero
            quantidade = quantidade + 1

        return soma / quantidade
    else:
        return 0


numeros = []

for i in range(5):
    numero = float(input("digite um numero: "))
    numeros.append(numero)

resultado = media(numeros)
print("a media é:", resultado)


# crie uma funcao que recebe uma string e conta quantas vogais (a, e, i, o, u) ela possui . a funcao deve retornar o numero de vogais

def contar_vogal(palavra):
    contador = 0 
    
    for letra in "aeiouAEIOU":
        contador += 1
    
    return contador 

palavra = input("digite uma palavra: ")
resultado = contar_vogal(palavra)
print("quantidade de vogais: ", resultado)

# crie uma função que recebe um número e retorna o seu fatorial. o fatorial de um número n é o produto de todos os numeros inteiros menores ou iguais a n

def fatorial(n):
    resultado = 1
    
    for i in range(1, n + 1):
        resultado = resultado * i
    
    return resultado

numero = int(input("Digite um número: "))
print("Fatorial:", fatorial(numero))