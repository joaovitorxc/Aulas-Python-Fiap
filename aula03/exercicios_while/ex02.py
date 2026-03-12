num = int(input("digite um número par:"))

while num % 2 != 0:
    num = int(input("tente novamente, digite um número par: "))
else:
    print(f"o número escolhido foi: {num}")
