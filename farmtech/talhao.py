from farmtech.storage import talhoes, culturas, areas, custos


def cadastrar_talhao():

    nome = input("Nome do talhao: ")

    print("Escolha a cultura")
    print("1 - Cana de acucar")
    print("2 - Cafe Arabica")

    opcao = input("Opcao: ")

    if opcao == "1":
        cultura = "Cana-de-acucar"
    elif opcao == "2":
        cultura = "Cafe Arabica"
    else:
        print("Opcao invalida")
        return

    # área à ser calculada 
    area = 0

    # custo também
    custo = 0

    talhoes.append(nome)
    culturas.append(cultura)
    areas.append(area)
    custos.append(custo)

    print("Talhao cadastrado com sucesso!")

def listar_talhoes():

    if len(talhoes) == 0:
        print("Nenhum talhao cadastrado")
        return

    for i in range(len(talhoes)):

        print(f"""
ID: {i}
Nome: {talhoes[i]}
Cultura: {culturas[i]}
Area: {areas[i]}
Custo: {custos[i]}
""")
        
def deletar_talhao():

    listar_talhoes()

    indice = int(input("Digite o ID do talhao para deletar: "))

    talhoes.pop(indice)
    culturas.pop(indice)
    areas.pop(indice)
    custos.pop(indice)

    print("Talhao removido")

def atualizar_talhao():

    listar_talhoes()

    indice = int(input("Digite o ID para atualizar: "))

    novo_nome = input("Novo nome do talhao: ")

    talhoes[indice] = novo_nome

    print("Talhao atualizado")