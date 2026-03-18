"""
Módulo de interface com o usuário (CLI).

Responsável pela interação via terminal, incluindo:
- Exibição de menus
- Entrada de dados
- Navegação entre funcionalidades
- Validação básica de entrada
"""

from farmtech import storage
from farmtech import calculos
from farmtech import service
import os


def limparTela():
    """
    Limpa o terminal do usuário.

    Compatível com:
    - Windows (cls)
    - Linux/Mac (clear)
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def pausar():
    """
    Pausa a execução até o usuário pressionar ENTER.
    """
    input("\nPressione ENTER para continuar...")


def sair(entrada):
    """
    Verifica se o usuário deseja sair da operação atual.

    Caso a entrada esteja vazia, solicita confirmação.

    Args:
        entrada (str): Entrada fornecida pelo usuário.

    Returns:
        bool: True se o usuário desejar sair, False caso contrário.
    """
    if entrada == "":
        match input("Deseja sair desta operação? (S/N): ").lower().strip():
            case "s":
                return True
            case "n":
                return False
            case _:
                return False


def continuar():
    """
    Pergunta ao usuário se deseja continuar realizando atualizações.

    Returns:
        bool:
            True se o usuário quiser continuar.
            False se quiser voltar ao menu principal.
    """
    match input("Deseja Continuar atualizando os dados?(S/N)").lower().strip():
        case "s":
            pausar()
            return True
        case "n":
            pausar()
            menu()
            return False
        case _:
            return False


def menu():
    """
    Exibe o menu principal do sistema e gerencia o fluxo de navegação.

    Permite acesso às funcionalidades:
    - Cadastro
    - Listagem
    - Atualização
    - Remoção
    - Exportação de dados
    """
    while True:

        limparTela()

        print("""
╔══════════════════════════════╗
║        FARMTECH SYSTEM       ║
╚══════════════════════════════╝

[1] Cadastrar Talhão
[2] Listar Talhões
[3] Atualizar Talhão
[4] Remover Talhão
[0] Sair

--------------------------------
""")

        match input("Escolha: "):
            case "1":
                adicionar_talhao()
            case "2":
                mostrar_talhoes()
            case "3":
                alterar_talhao()
            case "4":
                apagar_talhao()

            case "0":
                # Exporta os dados antes de encerrar o sistema
                service.export_csv()
                print("CSV exportado!")
                break

            case _:
                print("opçao invalida")

        pausar()


def mostrar_talhoes() -> bool:
    """
    Exibe todos os talhões cadastrados no sistema.

    Returns:
        bool:
            True se houver talhões cadastrados.
            False caso a lista esteja vazia.
    """
    limparTela()
    lista_de_talhoes = service.listar_talhoes()

    if not lista_de_talhoes:
        print("⚠ Nenhum talhão cadastrado no sistema.")
        return False

    for i, talhao in enumerate(lista_de_talhoes):
        print("────────────────────────────────")
        print(f"ID:{i}")
        print(talhao)

    return True


def adicionar_talhao():
    """
    Realiza o cadastro de um novo talhão.

    O usuário deve:
    - Informar o nome
    - Escolher a cultura
    - Informar as dimensões do terreno

    A área é calculada automaticamente conforme o tipo de cultura.
    """
    while True:
        limparTela()
        print("=== Cadastro de Talhão ===")

        nome = input("Nome do talhão: ")

        print("Selecione o tipo de cultura:")
        print("[1] Cana de açúcar\n"
              "[2] Café Arabica")

        opcao = input("Escolha: ")

        if opcao == "1":
            cultura = "Cana-de-açúcar"
            area = imprimir_calculo_retangulo()
            service.cadastrar_talhao(nome, cultura, area)
            break

        elif opcao == "2":
            cultura = "Café Arabica"
            area = imprimir_calculo_trapezio()
            service.cadastrar_talhao(nome, cultura, area)
            break

        else:
            print("Opção inválida")
            continue

    print("Talhão Cadastrado com sucesso!")


def alterar_talhao():
    """
    Permite atualizar os dados de um talhão existente.

    O usuário pode alterar:
    - Nome
    - Cultura (com recálculo de área e insumos)
    - Área (com recálculo de insumos)
    """
    if mostrar_talhoes():
        while True:
            entrada = input("Informe o ID do talhão que deseja atualizar: ")

            if sair(entrada):
                break

            if not entrada.isdigit():
                print("❌ ID inválido. Tente novamente.")
                continue

            indice = int(entrada)

            if indice not in [x for x in range(len(service.listar_talhoes()))]:
                print("❌ ID inválido. Tente novamente.")
                continue

            while True:
                limparTela()
                print("Selecione o que deseja alterar:")
                print("[1] Nome \n"
                      "[2] Cultura\n"
                      "[3] Area\n"
                      "[0] Sair\n")

                match input("Escolha: "):
                    case "1":
                        novo_nome = input("Digite o novo nome do talhão: ")

                        if service.atualizar_talhao(indice, novo_nome=novo_nome):
                            print("✅ Talhão atualizado com sucesso!")
                            if continuar():
                                continue
                        else:
                            print("❌ Não foi possível atualizar o talhão.")
                            pausar()

                    case "2":
                        while True:
                            print("Selecione o tipo de cultura:")
                            print("[1] Cana de açúcar\n"
                                  "[2] Café Arabica")

                            escolha = input("Escolha: ")

                            if escolha not in ["1", "2"]:
                                print("Opção inválida")
                                continue
                            break

                        # Recalcula área conforme o tipo de cultura
                        if escolha == "1":
                            area = imprimir_calculo_retangulo()
                        else:
                            area = imprimir_calculo_trapezio()

                        if service.atualizar_talhao(indice, nova_cultura=escolha, nova_area=area):
                            print("✅ Talhão atualizado com sucesso!")
                            if continuar():
                                continue
                        else:
                            print("❌ Não foi possível atualizar o talhão.")
                            pausar()

                    case "3":
                        # Mantém a cultura atual e recalcula área
                        if storage.talhoes[indice].cultura == "Cana-de-açúcar":
                            nova_area = imprimir_calculo_retangulo()
                        else:
                            nova_area = imprimir_calculo_trapezio()

                        if service.atualizar_talhao(indice, nova_area=nova_area):
                            print("✅ Talhão atualizado com sucesso!")
                            if continuar():
                                continue
                        else:
                            print("❌ Não foi possível atualizar o talhão.")
                            pausar()

                    case "0":
                        return

                    case _:
                        print("opçao invalida")
                        pausar()


def apagar_talhao():
    """
    Remove um talhão do sistema com base no ID informado pelo usuário.
    """
    if mostrar_talhoes():
        while True:
            entrada = input("Digite o ID do talhão para deletar: ")

            if sair(entrada):
                return

            if not entrada.isdigit():
                print("❌ ID inválido.")
                continue

            indice = int(entrada)

            if indice not in [x for x in range(len(service.listar_talhoes()))]:
                print("❌ ID inválido.")
                continue

            if service.deletar_talhao(indice):
                print("🗑 Talhão removido com sucesso!")
            else:
                print("❌ ID inválido.")

            return


def imprimir_calculo_retangulo():
    """
    Solicita ao usuário as dimensões de um terreno retangular
    e retorna a área calculada em hectares.

    Returns:
        float: Área calculada.
    """
    print("Cálculo da área (retângulo)")
    print("Informe as dimensões do terreno:")

    while True:
        try:
            base = float(input("Base: "))
            altura = float(input("Altura: "))
            return calculos.calculo_retangulo(base, altura)
        except ValueError:
            print("Por favor insira somente números")


def imprimir_calculo_trapezio():
    """
    Solicita ao usuário as dimensões de um terreno em formato de trapézio
    e retorna a área calculada em hectares.

    Garante que:
    - A base menor seja menor que a base maior

    Returns:
        float: Área calculada.
    """
    print("Cálculo da área (trapézio)")
    print("Informe as dimensões do terreno:")

    while True:
        try:
            base_maior = float(input("Base Maior: "))
            base_menor = float(input("Base Menor: "))

            # Validação da regra geométrica
            while base_menor > base_maior:
                print("A base menor deve ser menor que a base maior")
                base_menor = float(input("Base Menor: "))

            altura = float(input("Altura: "))
            return calculos.calculo_trapezio(base_maior, base_menor, altura)

        except ValueError:
            print("❌ Valor inválido. Digite apenas números.")