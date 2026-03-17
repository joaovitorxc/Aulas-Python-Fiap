# ex01 -menu com case: crie um programa que mostre um menu com tres opções: ver perfil, editar perfil, sair. o programa deve ler a opção case para mostrar a ação correspondente.
while True:
    print("menu: ")
    print("1 - ver perfil")
    print("2 - editar perfil")
    print("3 - sair")

    opção = int(input("escolha uma opção:"))
    match opção:
        case 1:
            print("ver perfil")
        case 2:
            print("editar perfil")
        case 3:
            print("sair")
            break
        case _:
            print("opção inválida")



#ex02 - crie um programa que receba um número de 1 a 7 representando um dia da semana

while True:
    dia = int(input("Digite um número de 1 a 7: "))
    match dia:
        case 1:
            print("domingo")
            break
        case 2:
            print("segunda-feira")
            break
        case 3:
            print("terça-feira")
            break
        case 4:
            print("quarta-feira")
            break
        case 5:
            print("quinta-feira")
            break
        case 6:
            print("sexta-feira")
            break
        case 7:
            print("sábado")
            break
        case _:
            print("número inválido, tente novamente")
            
#ex03 - crie um programa que receba um número de 1 a 12 representando um mês do ano. utilize match case com agrupamento para identificar a estação do ano correspondente

while True:
    mes = int(input("digite um número de 1 a 12: "))
    match mes:
        case 12 | 2 | 1:
            print ("verão")
            break
        case 3 | 4 | 5:
            print ("outono")
            break
        case 6 | 7 | 8:
            print ("inverno")
            break
        case 9 | 10 | 11: 
            print ("primavera")
            break
        case _:
            print ("número inválido, tente novamente")
            

#ex04 - crie um programa que receba a idade de uma pessoa. use match case com if para classificar

while True:
    idade = int(input("digite sua idade: "))
    match idade:
        case idade if idade <= 12:
            print ("criança")
            break
        case idade if idade == 13 and idade <= 17:
            print ("adolescente")
            break
        case idade if idade >= 18:
            print ("adulto")
            break
        case _:
            print ("idade inválida, tente novamente")
            

#ex05 - crie um programa que receba uma nota de 0 a 10. use match com if para classificar o desempenho

while True:
    nota = int(input("digite uma nota de 0 a 10: "))
    match nota:
        case nota if nota == 9 or nota == 10:
            print ("exelente")
            break
        case nota if nota == 7 or nota == 8:
            print ("bom")
            break
        case nota if nota == 5 or nota == 6:
            print ("regular")
            break
        case nota if nota < 5:
            print ("reprovado")
            break
        case _:
            print ("nota inválida, tente novamente")
