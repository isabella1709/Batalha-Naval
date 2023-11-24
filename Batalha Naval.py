import random

# variáveis
navios_jogador_humano = 5
navios_jogador_computador = 5
ataques = 5
win1 = 0
win2 = 0

# matrizes
matriz_jogador_coordenadas = [
    ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
]
matriz_computador_coordenadas = [
    ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
]
matriz_jogador_console = [
    ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
]
matriz_computador_console = [
    ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
]

print('\nBem-vindo ao Batalha Naval!\n')
# posicionamento das embarcações do jogador humano
for navio in range(navios_jogador_humano):
    linha_posicionamento = int(input("\nEscolha a linha que deseja posicionar sua embarcação: "))
    coluna_posicionamento = int(input("Escolha a coluna que deseja posicionar sua embarcação: "))

    matriz_jogador_coordenadas[linha_posicionamento - 1][coluna_posicionamento - 1] = 'X'
    for linha in range(5):
        print(" ".join(matriz_jogador_coordenadas[linha]))

# posicionamento das embarcações do jogador computador
for navio in range(navios_jogador_computador):
    linha_posicionamento = random.randint(0, 4)
    coluna_posicionamento = random.randint(0, 9)

    matriz_computador_coordenadas[linha_posicionamento][coluna_posicionamento] = 'X'
print("\nO computador já posicionou suas embarcações!\n")

# exibição dos tabuleiros

print("\n-Tabuleiro do Jogador-\n")
for linha in range(5):
    print(" ".join(matriz_jogador_console[linha]))
print("\n------------------------")
print(f'Embarcações restantes: {navios_jogador_humano}\n')
print("\n-Tabuleiro do Computador-\n")
for linha in range(5):
    print(" ".join(matriz_computador_console[linha]))
print("\n------------------------")
print(f'Embarcações restantes: {navios_jogador_computador}\n')

# Só pra testar se tava funcionando
for linha in range(5):
    print(" ".join(matriz_computador_coordenadas[linha]))

# o jogo irá rodar enquanto nenhum dos jogadores tiver derrubado todas as 5 embarcações
while win1 != 5 and win2 != 5:

    # ataques do jogador
    while ataques > 0 and ataques <= 5:
        linha_ataque = int(input("\n\nEscolha a linha que deseja atacar: "))
        coluna_ataque = int(input("Escolha a coluna que deseja atacar: "))

        # caso o jogador acerte uma embarcação
        if matriz_computador_coordenadas[linha_ataque - 1][coluna_ataque - 1] == 'X':
            matriz_computador_console[linha_ataque - 1][coluna_ataque - 1] = 'X'
            navios_jogador_computador -= 1
            win1 += 1
            print('Parabéns! Você acertou uma embarcação! ')
            print("\n------------------------")

        # caso o jogador não acerte nada
        else:
            matriz_computador_console[linha_ataque - 1][coluna_ataque - 1] = 'o'
            print('Ops, parece que não tem nada aqui ')
            print("\n------------------------")
        ataques -= 1

    ataques = 5

    # ataques do computador
    while ataques > 0 and ataques <= 5:
        linha_ataque = random.randint(0, 4)
        coluna_ataque = random.randint(0, 9)

        # caso o computador acerte uma embarcação
        if matriz_jogador_coordenadas[linha_ataque - 1][coluna_ataque - 1] == 'X':
            matriz_jogador_console[linha_ataque - 1][coluna_ataque - 1] = 'X'
            navios_jogador_humano -= 1
            win2 += 1
            print('- Jogada do computador -')
            print('Vish, o computador acertou uma embarcação sua!')
            print("\n------------------------\n\n")

        # caso o computador não acerte nada
        else:
            matriz_jogador_console[linha_ataque - 1][coluna_ataque - 1] = 'o'
            print('- Jogada do computador -')
            print('\n\nParece que o computador errou a jogada!')
            print("\n------------------------\n\n")
        ataques -= 1

    ataques = 5

    # exibição dos tabuleiros
    print("\n-Tabuleiro do Jogador-\n")
    for linha in range(5):
        print(" ".join(matriz_jogador_console[linha]))
    print("\n------------------------")
    print(f'Embarcações restantes do jogador: {navios_jogador_humano}\n')
    print("\n-Tabuleiro do Computador-\n")
    for linha in range(5):
        print(" ".join(matriz_computador_console[linha]))
    print("\n------------------------")
    print(f'Embarcações restantes do computador: {navios_jogador_computador}\n')

# vitória do jogador humano
if navios_jogador_computador == 0:
    print("\n------------------------\n\n")
    print('Parabéns! Você derrubou todas as embarcações inimigas e venceu o jogo!')

# vitória do computador
elif navios_jogador_humano == 0:
    print("\n------------------------\n\n")
    print('Poxa, parece que não foi dessa vez...')
    print('O computador ganhou o jogo.')

# agradecimentos
print('Obrigada por jogar o nosso batalha naval!')
print('Esperamos que tenha gostado da experiência.')
print('Jogo desenvolvido por: Ana Flávia e Isabella - BCC')




