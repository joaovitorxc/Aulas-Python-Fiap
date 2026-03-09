# umm ano é bissexto se:
# é divisível por 400 ou
# é divisível por 4 e não é divisível por 100

ano = int(input("Digite um ano: "))

if ano % 400 == 0:
    print(f"{ano} é um ano bissexto!")
elif ano % 4 == 0 and ano % 100 != 0:
    print(f"{ano} é um ano bissexto!")
else:
    print(f"{ano} não é um ano bissexto!")
