# Crie um programa que tenha uma dupla
# totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

cont = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez',
        'onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')
while True:
    while True:
        num = int(input("Digite um número entre 0 e 20: "))
        if 0 <= num <= 20:
            break
        print('Tente Novamente! Número Inválido!')
    print(f'Voce digitou o numero {num}, que por extenso fica {cont[num]}')
    print('-=' * 30)
    continuar = input("Deseja continuar? (S/N) ").strip().upper()[0]
    print('-=' * 30)
    if continuar == 'N':
        print(f'Obrigado por utilizar o programa!')
        break
