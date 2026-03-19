#crie duas matrizes 3x3 e calcule a soma delas

matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matriz2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz3 = []

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(matriz1[i][j] + matriz2[i][j])
    matriz3.append(linha)

for linha in matriz3:
    print(linha)
    
    
    
# crie uma matriz 2x2 e um escalar. multiplique a matriz pelo escalar 

matriz = [
     [1, 2],
     [3, 4]
 ]
 
escalar = 2 
matriz_resultado = []
for i in range(2):
    linha = []
    for j in range(2):
         linha.append(matriz[i][j] * escalar)
    matriz_resultado.append(linha)
     
for linha in matriz_resultado:
    print(linha)
    

# crie uma matriz 3x2 e calcule sua transposta

matriz = [
    [1, 2],
    [3, 4],
    [5, 6]
]

transposta = []
for j in range(2):
    linha = []
    for i in range(3):
        linha.append(matriz[i][j])
    transposta.append(linha)
    for linha in transposta:
        print(linha)
        
        
#crie uma matriz 3x3 e verifique se ela é uma matriz identidade

matriz = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]
identidade = True
for i in range(3):
    for j in range(3):
        if (i == j and matriz[i][j] != 1) or (i != j and matriz[i][j] != 0):
            identidade = False
            break





#crie duas matrizes 2x3 e 3x2 e calcule o produto das duas matrizes

matriz1 = [
    [1, 2, 3],
    [4, 5, 6]
]

matriz2 = [
    [7, 8],
    [9, 10],
    [11, 12]
]
produto = []
for i in range(2):
    linha = []
    for j in range(2):
        elemento = 0
    