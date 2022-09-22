from random import randint
from time import sleep

print('=' * 30)
print('VAMOS JOGAR PAR OU IMPAR')
print('=' * 30)
soma = cont = 0
while True:
    computador = randint(0, 10)
    valor = int(input('Diga um valor: '))
    parImpar = input('Par ou Impar? [P/I]: ').upper().strip()[0]
    print('=' * 30)
    soma = valor + computador
    if soma % 2 == 0:
        print(f'\nVocê jogou {valor} e o computador {computador}. Total foi de {soma} e deu Par')
        print('=' * 30)
        if parImpar in 'P':
            print('=' * 30)
            print('Você VENCEU!!!')
            print('Vamos jogar novamente....')
            print('=' * 30)
            cont += 1
            sleep(1)
        else:
            print(f'GAMER OVER! voce venceu {cont} vezes.')
            break
    else:
        print(f'\nVocê jogou {valor} e o computador {computador}. Total foi de {soma} e deu Impar')
        print('=' * 30)
        if parImpar in 'I':
            print('=' * 30)
            print('Você VENCEU!!!')
            print('Vamos jogar novamente....')
            print('=' * 30)
            cont += 1
            sleep(1)
        else:
            print(f'GAMER OVER! voce venceu {cont} vezes.')
            break
