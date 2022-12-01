def jogar():
    print('*****************')
    print('* Jogo da Forca *')
    print('*****************')

    palavra_secreta = 'futebol'
    segredo = []

    for palavra in palavra_secreta:
        segredo.append('_')

    erros = 0
    acertou = False
    enforcou = erros == 6


    while(not acertou and not enforcou):
        chute = input('Qual letra? ')

        if (chute in palavra_secreta):
            posicao = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    segredo[posicao] = letra
                posicao += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = '_' not in segredo
        print(segredo)

    if(acertou):
        print('Você	ganhou!!')
    else:
        print('Você	perdeu!!')
    print('Fim	do	jogo')