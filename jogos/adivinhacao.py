def jogar():
    print('***********************')
    print('* Jogo da Adivinhação *')
    print('***********************')

    numero_secreto = 10

    tentativas = 3

    while tentativas > 0:
        chute = int(input('Digite um número: '))
        print('Você digitou {}\n'.format(chute))

        if chute > numero_secreto:
            print('O número digitado é maior que o número secreto')
            if tentativas == 1:
                tentativas = tentativas - 1
                print('\nPERDEU!\nVocê não tem mais tentativas')
            else:
                tentativas = tentativas - 1
                print('Você agora tem {} tentativas'.format(tentativas))
        elif chute < numero_secreto:
            print('O número digitado é menor que o número secreto')
            if tentativas == 1:
                tentativas = tentativas - 1
                print('\nPERDEU!\nVocê não tem mais tentativas')
            else:
                tentativas = tentativas - 1
                print('Você agora tem {} tentativas'.format(tentativas))
        else:
            print('\nPARABÉNS! VOCÊ ACERTOU!\nO número secreto é {}'.format(numero_secreto))
            break
