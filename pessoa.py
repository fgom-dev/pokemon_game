import random
from time import sleep
from pokemon import *

NOMES = ['Ash', 'Misty', 'Brock', 'Tracey', 'May', 'Max', 'Dawn', 'Íris', 'Cilan', 'Clemont', 'Bonnie', 'Serena',
         'Lílian', 'Kiawe', 'Lulú', 'Victória', 'Chris', 'Rotomdex']

POKEMONS = [PokemonFogo('Charmander'),
            PokemonFogo('Charmilion'),
            PokemonFogo('Charizard'),
            PokemonAgua('Squirtle'),
            PokemonAgua('Blastoize'),
            PokemonEletrico('Pikachu'),
            PokemonEletrico('Raichu'),
]


class Pessoa:
    def __init__(self, nome=None, pokemons=[], moedas=100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

        self.moedas = moedas

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        print('--------------------------------')
        print(f'\033[1;31mPOKEMONS DE {self}:\033[0;0m')
        print('--------------------------------')
        sleep(0.5)
        if self.pokemons:
            for i, pokemon in enumerate(self.pokemons):
                print(f'\033[1;36m[{i+1}] {pokemon}\033[0;0m')
                sleep(0.2)
        else:
            print('--------------------------------')
            print(f'\033[1;31m{self} NÃO TEM POKEMON!!\033[0;0m')
            print('--------------------------------')

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_ecolhido = random.choice(self.pokemons)
            print('--------------------------------')
            print(f'\033[1;31m{self} ESCOLHEU {pokemon_ecolhido}!!\033[0;0m')
            print('--------------------------------')
            sleep(1)
            return pokemon_ecolhido
        else:
            print('--------------------------------')
            print('\033[1;31mEsse jogador não possuí Pokemons!\033[0;0m')
            print('--------------------------------')


class Player(Pessoa):
    tipo = 'player'

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print('--------------------------------')
        print(f'\033[1;31m{self} CAPTUROU {pokemon}!!\033[0;0m')
        print('--------------------------------')
        sleep(0.5)

    def escolher_pokemon(self):
        if self.pokemons:
            while True:
                self.mostrar_pokemons()
                try:
                    escolha = int(input('Escolha o pokemon para batalha:'))
                    pokemon_escolhido = self.pokemons[escolha - 1]
                    print('--------------------------------')
                    print(f'\033[1;36m{pokemon_escolhido} EU ESCOLHO VOCÊ!!!\033[0;0m')
                    print('--------------------------------')
                    sleep(0.5)
                    return pokemon_escolhido
                except:
                    print('ESCOLHA INVÁLIDA!')
        else:
            print('--------------------------------')
            print('\033[1;31mEsse jogador não possuí Pokemons!\033[0;0m')
            print('--------------------------------')

    def mostrar_moedas(self):
        print('--------------------------------')
        print(f'\033[1;31mVocê possuí {self.moedas} moedas!\033[0;0m')
        print('--------------------------------')
        sleep(0.5)

    def ganhar_moedas(self, quantidade):
        self.moedas += quantidade
        print('--------------------------------')
        print(f'\033[1;31mVocê ganhou {quantidade} moedas!\033[0;0m')
        print('--------------------------------')
        sleep(0.5)
        self.mostrar_moedas()

    def batalhar(self, pessoa):
        print('--------------------------------')
        print(f'\033[1;31m{self} iniciou uma batalha com {pessoa}!\033[0;0m')
        print('--------------------------------')
        sleep(2)

        pokemon_inimigo = pessoa.escolher_pokemon()
        meu_pokemon = self.escolher_pokemon()

        if meu_pokemon and pokemon_inimigo:
            while True:
                vitoria = meu_pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print('--------------------------------')
                    print(f'\033[1;31m{pessoa} foi DERROTADO!')
                    print(f'{self} venceu a batalha!\033[0;0m')
                    print('--------------------------------')
                    sleep(0.5)
                    self.ganhar_moedas(pokemon_inimigo.level * 100)
                    break
                vitoria_inimiga = pokemon_inimigo.atacar(meu_pokemon)
                if vitoria_inimiga:
                    print('--------------------------------')
                    print(f'\033[1;31m{pessoa} venceu a batalha!\033[0;0m')
                    print('--------------------------------')
                    sleep(0.5)
                    break
        else:
            print('Essa batalha não pode ocorrer!')

    def explorar(self):
        while True:
            if random.random() <=0.3:
                pokemon = random.choice(POKEMONS)
                print('-------------------------------')
                print('\033[1;31mEXPLORANDO...\033[0;0m')
                print('-------------------------------')
                sleep(2)
                print('--------------------------------')
                print(f'\033[1;31mUm {pokemon} selvagem apareceu!\033[0;0m')
                print('--------------------------------')
                sleep(0.5)
                escolha = input('Deseja capturar esse pokemon? (s/n) ')
                if escolha == 's':
                    if random.random() >= 0.5:
                        print('------------------')
                        print('\033[1;31mCAPTURANDO...\033[0;0m')
                        print('------------------')
                        sleep(2)
                        self.capturar(pokemon)
                        sleep(0.5)
                    else:
                        print('------------------')
                        print('\033[1;31mCAPTURANDO...\033[0;0m')
                        print('------------------')
                        sleep(2)
                        print('------------------')
                        print('\033[1;31mO pokemon escapou!\033[0;0m')
                        print('------------------')
                        sleep(0.5)
                elif escolha == 'n':
                    print('OK, boa viagem!')
                    break
            else:
                print('-------------------------------')
                print('\033[1;31mEXPLORANDO...\033[0;0m')
                print('-------------------------------')
                sleep(2)
                print('-------------------------------')
                print('\033[1;31mNão encontramos nenhum pokemon!\033[0;0m')
                print('-------------------------------')
                escolha = input('Deseja continuar? [s/n]')
                if escolha == 's':
                    pass
                elif escolha == 'n':
                    break


class Inimigo(Pessoa):
    tipo = 'inimigo'

    def __init__(self, nome=None, pokemons=None):
        if not pokemons:
            pokemons_aleatorios = []
            for i in range(random.randint(1, 6)):
                pokemons_aleatorios.append(random.choice(POKEMONS))
            super().__init__(nome=nome, pokemons=pokemons_aleatorios)
        else:
            super().__init__(nome=nome, pokemons=pokemons)
