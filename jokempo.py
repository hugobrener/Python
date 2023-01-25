import random
from time import sleep

itens = ['papel', 'tesoura', 'pedra', 'lagarto', 'spock']
#computador = random.choice(itens)
vencedor = ''
opcao_de_jogo = 1


while opcao_de_jogo == 1:
    print('=-' * 20)
    print('=-' * 20)
    print('JOKEMPO PEDRA, PAPEL, TESOURA, LAGARTO SPOCK')
    sleep(1)
    jogador = str.lower(input('escolha sua opção: '))
    computador = random.choice(itens)
    print('=-' * 20)
    print('=-' * 20)
    sleep(1)
    print('o jogador escolheu {}'.format(jogador))
    sleep(0.5)
    print('o computador escolheu {}.\n'.format(computador))

    print('=-' * 20)
    print('=-' * 20)
    sleep(1)
    if jogador == 'papel':
        if (computador == 'pedra'):
            print('papel embrulha pedra')
            vencedor = 'jogador venceu'

        elif (computador == 'spock'):
            print('papel refuta spock')
            vencedor = 'jogador venceu'

        elif computador == 'papel':
            vencedor = 'empate'

        elif computador == 'tesoura':
            print('tesoura corta papel')
            vencedor = 'computador venceu'

        elif computador == 'lagarto':
            print('lagarto come papel')
            vencedor = 'computador venceu'

        print('Resultado da partida: {}\n'.format(vencedor))
        sleep(2)
        opcao_de_jogo = int(input('Para jogar novamente digite [1], para sair digite [0]'))

    elif jogador == 'tesoura':
        if computador == 'papel':
            print('tesoura corta papel')
            vencedor = 'jogador venceu'

        elif computador == 'lagarto':
            print('tesoura decapta lagarto')
            vencedor = 'jogador venceu'

        elif computador == 'tesoura':
            vencedor = 'empate'

        elif computador == 'pedra':
            print('pedra esmaga tesoura')
            vencedor = 'computador venceu'

        elif computador == 'spock':
            print('spock desintegra tesoura')
            print('Resultado da partida: {}\n'.format(vencedor))

        sleep(2)
        opcao_de_jogo = int(input('Para jogar novamente digite [1], para sair digite [0]'))

    elif jogador == 'pedra':
        if (computador == 'tesoura') :
            print('pedra esmaga tesoura')
            vencedor = 'jogador venceu'

        elif (computador == 'lagarto'):
            print('pedra esmaga cabeça do lagarto')
            vencedor = 'jogador venceu'
            
        elif computador == 'pedra':
            vencedor = 'empate'
        else:
            vencedor = 'computador venceu'
        print('Resultado da partida: {}\n'.format(vencedor))
        sleep(2)
        opcao_de_jogo = int(input('''Para jogar novamente digite [1],\n
        para sair digite [0]'''))

    elif jogador == 'spock':
        if (computador == 'pedra') | (computador == 'tesoura'):
            vencedor = 'jogador venceu'
        elif computador == 'spock':
            vencedor = 'empate'
        else:
            vencedor = 'computador venceu'
        print('Resultado da partida: {}\n'.format(vencedor))
        sleep(2)
        opcao_de_jogo = int(input('Para jogar novamente digite [1], para sair digite [0]'))

    elif jogador == 'lagarto':
        if (computador == 'papel') | (computador == 'spock'):
            vencedor = 'jogador venceu'
        elif computador == 'lagarto':
            vencedor = 'empate'
        else:
            vencedor = 'computador venceu'
        print('Resultado da partida: {} \n'.format(vencedor))
        sleep(2)
        opcao_de_jogo = int(input('Para jogar novamente digite [1], para sair digite [0]'))

    else:
        print('jogada inválida\n')
        sleep(2)
        opcao_de_jogo = int(input('Para jogar novamente digite [1], para sair digite [0]'))

    print('')
    print('==//' * 10)
    print('')
# spock > rock
# spock > tesoura
# lagarto > spock
# lagarto > papel
# papel > pedra
# papel > spock
# tesoura >papel
# tesoura > lagarto
# pedra > tesoura
# pedra > lagarto

# pedra
# papel
# tesoura
# lagarto
# spock