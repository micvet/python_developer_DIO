import datetime

clientes = {}

def cadastro_cliente():
    cpf = input("Digite o CPF do cliente: ")
    nome = input("Digite o nome do cliente: ")
    saldo = float(input("Digite o saldo do cliente: "))

    cliente = {
        'CPF': cpf,
        'Nome': nome,
        'Saldo': saldo,
        'Saques_diarios': 0,
        'Transacoes': []
    }

    clientes[cpf] = cliente
    print("Cliente cadastrado com sucesso!")

def extrato(cpf):
    if cpf in clientes:
        cliente = clientes[cpf]
        print(f"Extrato para o cliente {cliente['Nome']} (CPF: {cliente['CPF']}):")
        for transacao in cliente['Transacoes']:
            print(transacao)
        print(f"Saldo atual: R$ {cliente['Saldo']:.2f}")
    else:
        print("Cliente não encontrado.")

def deposito(cpf):
    if cpf in clientes:
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        if valor_deposito <= 0:
            print("Valor inválido.")
        else:
            cliente = clientes[cpf]
            cliente['Saldo'] += valor_deposito
            data_hora_atual = datetime.datetime.now()
            data_formatada = data_hora_atual.strftime("%Y-%m-%d %H:%M:%S")
            transacao = f"{data_formatada} - Depósito de R$ {valor_deposito:.2f}"
            cliente['Transacoes'].append(transacao)
            print(f"Valor depositado com sucesso. Novo saldo: R$ {cliente['Saldo']:.2f}")
    else:
        print("Cliente não encontrado.")

def saque(cpf):
    if cpf in clientes:
        cliente = clientes[cpf]
        valor_saque = float(input("Digite o valor a ser sacado: "))
        if valor_saque <= 0:
            print("Valor inválido. Informe um valor válido.")
        elif valor_saque > cliente['Saldo']:
            print("Saldo insuficiente para a operação. Verifique seu extrato.")
        elif valor_saque > 500:
            print("O valor máximo diário para saque é de R$500,00.")
        elif cliente['Saques_diarios'] >= 3:
            print("Você atingiu o limite de saques diários. Tente novamente amanhã.")
        else:
            data_hora_atual = datetime.datetime.now()
            data_formatada = data_hora_atual.strftime("%Y-%m-%d %H:%M:%S")
            cliente['Saldo'] -= valor_saque
            transacao = f"{data_formatada} - Saque de R$ {valor_saque:.2f}"
            cliente['Transacoes'].append(transacao)
            cliente['Saques_diarios'] += 1
            print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso. Novo saldo: R$ {cliente['Saldo']:.2f}")
    else:
        print("Cliente não encontrado.")

def menu():
    print("\nMenu:\n"
    "1. Cadastrar Cliente\n"
    "2. Depositar\n"
    "3. Sacar\n"
    "4. Extrato\n"
    "5. Sair\n")
    opcao = input("Escolha uma opção: ")
    return opcao

def main():
    while True:
        opcao = menu()
        if opcao == '1':
            cadastro_cliente()
        elif opcao == '2':
            cpf = input("Digite o CPF do cliente: ")
            deposito(cpf)
        elif opcao == '3':
            cpf = input("Digite o CPF do cliente: ")
            saque(cpf)
        elif opcao == '4':
            cpf = input("Digite o CPF do cliente: ")
            extrato(cpf)
        elif opcao == '5':
            print("Obrigado por usar nossos serviços! Até mais!")
            break
        else:
            print("Opção inválida. Digite uma opção válida.")

if __name__ == "__main__":
    main()
