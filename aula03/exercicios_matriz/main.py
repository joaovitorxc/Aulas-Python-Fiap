#matriz inicial
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz[1][2])

#adicionando uma nova linha à matriz
nova_linha = [10, 11, 12]
matriz.append(nova_linha)

#imprimindo a matriz atualizada
for linha in matriz:
    print(linha)
    
#adicionando um elemento (100) à segunda linha na primeira posição
matriz[1].insert(0, 100)

#imprimindo a matriz atualizada
for linha in matriz:
    print(linha)
    
#usando 'del' para remover a segunda linha  
del matriz[1]

#imprimindo a matriz após a remoção da segunda linha
for linha in matriz:
    print(linha)
    
#usando 'pop' para remover e obter o elemento na terceira coluna da primeira linha 
elemento = matriz[0].pop(2)
print("\nElemento removido:", elemento)

#imprimindo a matriz após a remoção do elemento
print("\nMatriz após a remoção do elemento:")
for linha in matriz:
    print(linha)
    
#iterar sobre cada linha da matriz 
for linha in matriz:
    #iterar sobre cada linha da matriz
    for elemento in linha:
        print(elemento, end=' ')
    #imprimir uma nova linha após cada linha da matriz 
    print()