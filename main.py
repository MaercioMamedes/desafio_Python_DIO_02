from datetime import datetime


def listar_usuarios():
    for usuario in LISTA_USUARIOS:
        print(usuario)


def criar_usuario():
    novo_usuario = {
        'nome': input("Informe o nome: "),
        'data_nascimento': input("Informe a data de nascimento: "),
        'cpf': input("Informe o CPF: "),
        'endereco': input("informe o endereço")
    }

    LISTA_USUARIOS.append(novo_usuario)


def exibir_extrato(*args, **kwargs):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def depositar(*args):
    # tratamento de erro para valores incorreto para depósito
    try:
        valor = float(input("Informe o valor para depósito: "))

        if valor > 0:
            saldo += valor
            # Obter a data e hora atual
            agora = datetime.now()

            # Formatar a data e hora
            data_hora_formatada = agora.strftime("%d-%m-%Y %H:%M")

            extrato += f"{data_hora_formatada} - Depósito: R$ {valor:.2f} \n"

        else:
            print("valor não pode ser negativo")

    except ValueError:
        print("Operação falhou! O valor informado é inválido.")


def sacar(**kwargs):
    try:

        valor = float(input("Informe o valor para o saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > LIMITE_SAQUE

        excedeu_saques = numero_saques_realizados >= QTD_SAQUES_LIMITE

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            agora = datetime.now()

            # Formatar a data e hora
            data_hora_formatada = agora.strftime("%d-%m-%Y %H:%M")

            extrato += f"{data_hora_formatada} - Saque: R$ {valor:.2f}\n"
            numero_saques_realizados += 1

        else:
            print("Operação falhou! O valor informado não pode ser negativo")

    except ValueError:
        print("Operação falhou! O valor informado é inválido.")


def menu_principal():
    menu = """
    
====================================
    DIGITAL INNOVATION BANK
====================================

Escolha uma opção:

[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar Usuário
[5] Criar Conta
[6] Listar Usuários
[7] Listar Contas
[8] Sair

=> """

    # variáveis do sistema
    saldo = 0
    extrato = ""
    saques_realizados = []
    depositos_realizados = []
    numero_saques_realizados = 0

    """Looping de exibição do Menu"""
    while True:
        # variável seletora do menu
        opcao = input(menu).lower()

        # opção de depósito
        if opcao == "1":
            depositar(saldo)

        # opção de saque
        elif opcao == "2":
            sacar(saldo=saldo)

        # opção para exibir extrato
        elif opcao == "3":
            exibir_extrato(extrato)

        elif opcao == "4":
            criar_usuario()

        elif opcao == "5":
            criar_conta()

        elif opcao == "6":
            listar_usuarios()

        elif opcao == "7":
            listar_contas()

            # opção para encerrar aplicação
        elif opcao == "8":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == '__main__':
    # constantes do sistema
    global LIMITE_SAQUE
    global QTD_SAQUES_LIMITE
    global LISTA_USUARIOS
    global LISTA_CONTAS

    LIMITE_SAQUE: int = 500
    QTD_SAQUES_LIMITE: int = 3
    LISTA_USUARIOS: list[dict] = []
    LISTA_CONTAS: list[dict] = []
    menu_principal()
