import random
from time import sleep


class Pokemon:
    def __init__(self, especie, level=None, nome=None):
        self.especie = especie
        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)
        if nome:
            self.nome = nome
        else:
            self.nome = especie

        self.ataque = self.level * 5
        self.hp = self.level * 10

    def __str__(self):
        return f'{self.nome}({self.level})'

    def atacar(self, pokemon):
        ataque_efetivo = int(self.ataque * random.random() * 1.3)
        pokemon.hp -= ataque_efetivo
        print('--------------------------------')
        print(f'\033[1;31m{ataque_efetivo} de dano em {pokemon}')
        print(f'{pokemon} possuí {pokemon.hp} de Vida!\033[0;0m')
        print('--------------------------------')
        sleep(2)

        if pokemon.hp <= 0:
            return True
        else:
            return False


class PokemonEletrico(Pokemon):
    tipo = 'eletrico'

    def atacar(self, pokemon):
        print('--------------------------------')
        print(f'\033[1;31m{self} lançou Raio do Trovão em {pokemon}!\033[0;0m')
        print('--------------------------------')
        sleep(2)
        return super().atacar(pokemon)


class PokemonFogo(Pokemon):
    tipo = 'fogo'

    def atacar(self, pokemon):
        print('--------------------------------')
        print(f'\033[1;31m{self} lançou Bola de fogo em {pokemon}!\033[0;0m')
        print('--------------------------------')
        sleep(2)
        return super().atacar(pokemon)


class PokemonAgua(Pokemon):
    tipo = 'água'

    def atacar(self, pokemon):
        print('--------------------------------')
        print(f"\033[1;31m{self} lançou Canhão d'água em {pokemon}!\033[0;0m")
        print('--------------------------------')
        sleep(2)
        return super().atacar(pokemon)


class PokemonGrama(Pokemon):
    tipo = 'grama'

    def atacar(self, pokemon):
        print('--------------------------------')
        print(f"\033[1;31m{self} lançou Sipó poderoso em {pokemon}!\033[100m")
        print('--------------------------------')
        sleep(2)
        return super().atacar(pokemon)
