from time import sleep
import pickle
from pokemon import *
from pessoa import *


def escolher_pokemon_inicial(player):
    pikachu = PokemonEletrico('Pikachu', level=1)
    charmander = PokemonFogo('Charmander', level=1)
    squirtle = PokemonAgua('Squirtle', level=1)
    bulbasaur = PokemonGrama('Bulbasaur', level=1)

    loop = True
    while loop == True:
        print(f'Olá {player}, Você poderá escolher agora o Pokemon que irá lhe acompanhar nessa jornada!')
        print('Você possuí "3" escolhas')
        print()
        sleep(3)
        print(f'[1] {charmander}')
        sleep(0.2)
        print(f'[2] {squirtle}')
        sleep(0.2)
        print(f'[3] {bulbasaur}')
        sleep(0.2)
        print(f'[4] Nenhum desses!')
        sleep(0.2)
        escolha = str(input('Escolha seu Pokemon: '))
        if escolha == '1':
            player.capturar(charmander)
            break
        elif escolha == '2':
            player.capturar(squirtle)
            break
        elif escolha == '3':
            player.capturar(bulbasaur)
            break
        elif escolha == '4':
            while True:
                escolha1 = str(input('Bem... Temos um outro Pokemon, ele é meio rebelde!\nVocê tem certeza? [S/N]'))
                if escolha1 in 'nN':
                    break
                elif escolha1 in 'sS':
                    player.capturar(pikachu)
                    loop = False
                    break
                else:
                    print('Digite "S" para Sim ou "N" para Não!')
        else:
            print('Escolha inválida!')


def salvar_jogo(player):
    try:
        with open('database.db', 'wb') as arquivo:
            pickle.dump(player, arquivo)
            print('--------------------------------')
            print('\033[1;31mSALVANDO...\033[0;0m')
            print('--------------------------------')
            sleep(2)
            print('--------------------------------')
            print('\033[1;31mJogo salvo com sucesso\033[0;0m')
            print('--------------------------------')
            sleep(0.5)
    except Exception as error:
        print('--------------------------------')
        print('\033[1;31mErro ao salvar jogo\033[0;0m')
        print('--------------------------------')
        print(error)


def carregar_jogo():
    try:
        with open('database.db', 'rb') as arquivo:
            player = pickle.load(arquivo)
            print('--------------------------------')
            print('\033[1;31mCARREGANDO...\033[0;0m')
            print('--------------------------------')
            sleep(2)
            print('--------------------------------')
            print('\033[1;31mJogo carregado com sucesso!\033[0;0m')
            print('--------------------------------')
            sleep(0.5)
            return player
    except FileNotFoundError:
        pass
    except Exception as error:
        print('--------------------------------')
        print('\033[1;31mErro ao carregar jogo\033[0;0m')
        print('--------------------------------')
        print(error)


if __name__ == '__main__':
    print('--------------------------------')
    print('\033[1;31mBem-vindo ao mundo POKEMON!\033[0;0m')
    print('--------------------------------')
    sleep(0.5)
    player = carregar_jogo()

    if not player:
        nome = input('Qual é o seu nome? ')
        player = Player(nome)
        sleep(0.5)
        print('--------------------------------')
        print(f'Olá {nome}, esse mundo é habitado por Pokemons, a partir de agora sua '
              f'missão é se tornar um mestre pokemon!')
        print('Capture o máximo de pokemons que conseguir e batalhe com seus amigos!')
        print('--------------------------------')
        sleep(5)
        print('--------------------------------')
        print(f'\033[1;31mVocê ganhou {player.moedas} moedas para ajudar em sua jornada\033[0;0m')
        print('--------------------------------')
        sleep(0.5)
        if player.pokemons:
            print('Já vi que você tem alguns pokemons')
            player.mostrar_pokemons()
        else:
            escolher_pokemon_inicial(player)
            print('\033[1;36mGary: Oh... Então você também vai entrar nessa?!')
            print('Gary: Vamos ver do que você é capaz!!!\033[0;0m')
            gary = Pessoa(nome='Gary', pokemons=[PokemonAgua('Squirtle', level=1)])
            player.batalhar(gary)
            salvar_jogo(player)

    while True:
        print()
        print('O que deseja fazer?')
        print()
        print('[1] Explorar o mundo')
        print('[2] Batalhar com um Inimigo')
        print('[3] PokeDex')
        print('[0] Sair do jogo')
        escolha = input()
        if escolha == '0':
            salvar_jogo(player)
            print('--------------------------------')
            print('\033[1;31mFechando o jogo!\033[0;0m')
            print('--------------------------------')
            sleep(0.5)
            break
        elif escolha == '1':
            player.explorar()
            salvar_jogo(player)
        elif escolha == '2':
            print('--------------------------------')
            print('\033[1;31mBuscando adversário...\033[0;0m')
            print('--------------------------------')
            sleep(5)
            player.batalhar(Inimigo())
            salvar_jogo(player)
        elif escolha == '3':
            player.mostrar_pokemons()
        else:
            print('--------------------------------')
            print('\033[1;31mEscolha inválida!!!\033[0;0m')
            print('--------------------------------')
