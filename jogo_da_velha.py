# ------- Importações -------

import random
from time import sleep

# ------- Funções -------

def jogada_player(j1):
    while True:
        n = int(input(f'qual casa você irá colocar seu {j1}?  '))
        if 1 < n > 9:
            print('faça uma jogada válida!')
        elif n is type(str):
            print('faça uma jogada válida!')
        else:
            return n

def alguem_ganhou():
    while True:
            if board[0] == board[1] == board[2] == j1 or board[3] == board[4] == board[5] == j1 or board[6] == board[7] == board[8] == j1 or board[0] == board[3] == board[6] == j1 or board[1] == board[4] == board[7] == j1 or board[2] == board[5] == board[8] == j1 or board[0] == board[4] == board[8] == j1 or board[2] == board[4] == board[6] == j1:
                return 1
            elif board[0] == board[1] == board[2] == m2 or board[3] == board[4] == board[5] == m2 or board[6] == board[7] == board[8] == m2 or board[0] == board[3] == board[6] == m2 or board[1] == board[4] == board[7] == m2 or board[2] == board[5] == board[8] == m2 or board[0] == board[4] == board[8] == m2 or board[2] == board[4] == board[6] == m2:
                return 2
            elif '-' not in board:
                return 3
            else:
                return 0

def print_board():
    print(f"""
    {board[0]}|{board[1]}|{board[2]}
    {board[3]}|{board[4]}|{board[5]}
    {board[6]}|{board[7]}|{board[8]}
                """)
    return

def resultado_jogo():
    while True:
        w = alguem_ganhou()
        if w == 1:
            print('O jogador vence!')
            exit()
        elif w == 2:
            print('A máquina vence!')
            exit()
        elif w == 3:
            print('Há um empate!')
            exit()
        elif w == 0:
            break

# ------- Código -------

print(f"""
Esse script é um jogo da velha clássico,
porém cada posição é numerada,
segue a ordem das casas:

    1|2|3
    4|5|6
    7|8|9

""")

j1 = ''
m2 = ''
opcao_jogador = input('você quer ser  X ou O?   ').strip().upper()
if opcao_jogador == 'O':
    j1 = 'O'
    m2 = 'X'
else:
    j1 = 'X'
    m2 = 'O'

board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
jogadas_ja_feitas = []
while True:

    print_board()

    resultado_jogo()

    p = jogada_player(j1) - 1

    if p in jogadas_ja_feitas:
        print('jogada já realizada')
        continue
    else:
        del board[p]
        board.insert(p, f'{j1}')
        jogadas_ja_feitas.append(p)

        resultado_jogo()

        while True:
            

            d = random.randint(0, 8)

            if d in jogadas_ja_feitas:
                continue
            else:
                del board[d]
                board.insert(d, f'{m2}')
                jogadas_ja_feitas.append(d)
                break