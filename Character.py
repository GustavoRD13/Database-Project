import random

class Raca:
    def __init__(self, nome, raca, vida_range, ataque_range, defesa_range, velocidade_range, inteligencia_range):
        self.nome = nome
        self.raca = raca
        self.vida = random.randint(*vida_range)
        self.ataque = random.randint(*ataque_range)
        self.defesa = random.randint(*defesa_range)
        self.velocidade = random.randint(*velocidade_range)
        self.inteligencia = random.randint(*inteligencia_range)

    def __str__(self):
        return (f"Nome: {self.nome}\nRaça: {self.raca}\n"
                f"Vida: {self.vida} | Ataque: {self.ataque} | Defesa: {self.defesa}\n"
                f"Velocidade: {self.velocidade} | Inteligência: {self.inteligencia}\n")

class Humano(Raca):
    def __init__(self, nome):
        super().__init__(nome, "Humano", (900, 1100), (140, 160), (90, 110), (90, 110), (90, 110))

class Orc(Raca):
    def __init__(self, nome):
        super().__init__(nome, "Orc", (1400, 1600), (40, 60), (190, 210), (40, 60), (40, 60))

class Elf(Raca):
    def __init__(self, nome):
        super().__init__(nome, "Elf", (1200, 1300), (90, 110), (40, 60), (120, 140), (110, 130))

def criar_instancia_personagem(nome, raca):
    return {"Humano": Humano, "Orc": Orc, "Elf": Elf}[raca](nome)

