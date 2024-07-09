def linha(tam=42):
     return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\n\033[31mERRO! Por favor digite um numero inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[31mEntrada de dados interrompida pelo usuario!\033[m')
            return 0
        else:
            return n


def menu(lista):
    cabeçalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc
