# crie uma função que recebe um número n e retorna o n-ésimo número da sequência de Fibonacci. a sequência de Fibonacci

n = int(input("digite um número: "))
a = 0
b = 1

for i in range(n-1):
    a, b = b, a + b

print("O", n, "número da sequência de Fibonacci é:", a)

#crie uma função que recebe tres números e retorna o maior deles

def maior (n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3
a = int(input("digite o primeiro número: "))
b = int(input("digite o segundo número: "))
c = int(input("digite o terceiro número: "))

print("o maior número é:", maior(a, b, c))

#crie uma função que recebe um número inteiro e retorna a soma de seus dígitos

digito = int(input("digite um número: "))
def digitos(num):
    soma = 0 
    for digito in str(num):
        soma += int(digito)
    return soma
print("a soma é:",digitos(digito))

#crie uma função que recebe um número n e retorna o seu fatorial

def fatorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fatorial(num - 1)

num = int(input("digite um número: "))
print("o fatorial é: ", fatorial(num))

#crie uma função que recebe uma string e verifica se ela é um palíndromo. (ou seja, se ela pode ser lida da mesma forma de trás para frente)

def palindromo(palavra):
    text = list(palavra)
        
    for i in reversed(text):
        
        text2 = list(reversed(text))
        
    if text == text2:
        return True
    else:
        return False
palavra = input("digite uma palavra: ")

        