numeros = [1, 2, 3]

numeros.append(4)

numeros2 = [5, 6, 7]

print (numeros)

numeros.extend(numeros2)

print(numeros)

numeros.insert(4, 10)
numeros.insert(6, 10)

print(numeros)

numeros.remove(10)
print(numeros)

print(numeros.pop(2))
print(numeros)

print(numeros2)
numeros2.clear()
print(numeros2)

index = numeros.index(10)
print(index)

vezes = numeros.count(5)
print(vezes)

numeros.sort()
print(numeros)

numeros.reverse()
print(numeros)

