andar = 0

while True:
    print(f'\n-* Você está no andar {andar}*-')
    print('Para qual andar, meu rei? ')
    andarDesejado = int(input())

    if andarDesejado > andar:
        print('Subindo')
        andar+=1

    elif andarDesejado < andar:
        print('Descendo')
        andar-=1

    elif andarDesejado == andar:
        print('Parado')
