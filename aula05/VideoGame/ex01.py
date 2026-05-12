class VideoGame:
    def __init__(self, modelo, lote, marca, memoria):
        self.modelo = modelo
        self.lote = lote
        self.marca = marca
        self.memoria = memoria
    
    def descrever(self):
        print(f"ATRIBUTOS:\nModelo: {self.modelo}\nLote: {self.lote}\nMarca: {self.marca}\nMemoria: {self.memoria}\n")

playstation = VideoGame("play2", 1000, "sony", "8 mb")
playstation.descrever()