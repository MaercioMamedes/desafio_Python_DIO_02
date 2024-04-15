from datetime import datetime

# Menu inicial

menu = """

====================================
    DIGITAL INNOVATION BANK
====================================

Escolha uma opção:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# variáveis do sistema
saldo = 0
extrato = ""
saques_realizados = []
depositos_realizados = []
numero_saques_realizados = 0

# constantes do sistema
LIMITE_SAQUE = 500
QTD_SAQUES_LIMITE = 3

"""Looping de exibição do Menu"""
while True:
    # variável seletora do menu
    opcao = input(menu).lower()

    # opção de depósito
    if opcao == "d":

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

    # opção de saque
    elif opcao == "s":

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

    # opção para exibir extrato
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    # opção para encerrar aplicação
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")