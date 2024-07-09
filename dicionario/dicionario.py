'''# Lista vazia
usuarios = {}
print(usuarios)

# Lista cheia
usuarios = {"chaves":["Chaves do 8", " 24/12/1017", "Recep_01"],
            "quico" : ["Quico das Flores", "20/12/2017", "Raiox_03"]
            }
print(usuarios)

# Lista colocando novos objetos
usuarios["florinda"] = ["Dona Florinda", "24/12/2017", "Raiox_01"]
print(usuarios)

#Buscando informacoes no dicionario
print("####----####")
print(usuarios.get("quico"))
'''

def perguntar():
   return input("O que deseja realizar?\n" +
                  "<I> - Para inserir um usuario\n" +
                  "<P> - Para pesquisar um usuario\n" +
                  "<E> - Para excluir um usuario\n" +
                  "<L> - Para listar um usuario: ").upper()


def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                   input("Digite a ultima data de acesso: "),
                                                   input("Qual a ultima estacao acessada: ").upper()]
    salvar(dicionario)

def salvar(dicionario):
    with open("bd.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor))




usuarios = {}
opcao = perguntar()
while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(usuarios)
    opcao = perguntar()
