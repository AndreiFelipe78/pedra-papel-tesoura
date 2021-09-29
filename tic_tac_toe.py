import random


def tic_tac():
    print('Seja muito bem-vindx ao jogo!\n')
    while True:
        try:
            resposta = int(input('''
                    1 - pedra
                    2 - papel
                    3 - tesoura\n
                    digite o numero da sua opção: '''))
            if resposta >3 or resposta <1:
                raise ValueError
            
        except ValueError:
            print('\nOpção inválida! Favor digitar o numero de uma das posições abaixo: ')
        else:
            lista = ['pedra', 'papel', 'tesoura']
            random.shuffle(lista)
            p = lista[0]
            pp = lista[1]
            t = lista[2]
            robot = random.sample(lista,1)
            if robot == ['pedra'] and resposta == 1:
                print('\nParece que empataram...')
            elif robot == ['pedra'] and resposta == 2:
                print(' O robô escolheu {} e voce escolheu {}.'.format(p, pp))
                print('Você ganhou!')
            elif robot == ['pedra'] and resposta == 3:
                print('\n O robô escolheu {} e voce escolheu {}.'.format(p, t))
                print('O robo ganhou!')
            elif robot == ['papel'] and resposta == 2:
                print('\nParece que empataram...')
            elif robot == ['papel'] and resposta == 1:
                print(' O robô escolheu {} e voce escolheu {}.'.format(pp, p))
                print('O robo ganhou')
            elif robot == ['papel'] and resposta == 3:
                print('O robô escolheu {} e voce escolheu {}.'.format(pp, t))
                print('Você ganhou!')        
            elif robot == ['tesoura'] and resposta == 3:
                print('Parece que empataram...')
            elif robot == ['tesoura'] and resposta == 2:
                print('O robô escolheu {} e voce escolheu {}.'.format(t, pp))
                print('O robo ganhou')
            elif robot == ['tesoura'] and resposta == 1:
                print('O robô escolheu {} e voce escolheu {}.'.format(t, p))
                print('Você ganhou!')
            dnovo = input('\n\nQuer jogar novamente? digite "S" para sim ou "N" para não: ')
            if dnovo == 'N' or dnovo == 'n':
                print('\nAté a próxima!')
                break 
            else:
                print('\ngosta de perder? Então, vamos outra vez!\n')
    
tic_tac()