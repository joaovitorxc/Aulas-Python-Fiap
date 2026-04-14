# abrir um arquivo para escrita
with open('arquivo.text', 'w', encoding='UTF-8') as file:
    file.write('olá, mundo!')
    
# abrir um arquivo para leitura e escrita
with open('arquivo.text', 'r+', encoding='UTF-8') as file:
    conteudo = file.read()
    file.write('\nAdicionando mais conteudo.')

#abrir um arquivo para anexo
with open('arquivo.text', 'a', encoding='UTF-8') as file:
    file.write('\nMais uma linha no final do arquivo.')
    
with open('arquivo.text', 'w') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')
    