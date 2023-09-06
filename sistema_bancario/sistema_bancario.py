import datetime

menu = """
[1] Depósito
[2] Saque
[3] Extrato
[4] Sair
"""
saldo = 0
limite = 500
extrato = []
numero_saques = 0
limite_saques = 3


while True:
    opcao = int(input(menu))

    if opcao == 1:
        data_hora_atual = datetime.datetime.now()
        data_formatada = data_hora_atual.strftime("%Y-%m-%d %H:%M:%S")
        valor_deposito= int(input("insira o valor a ser depositado: "))
        if valor_deposito <=0:
            print ("Valor inválido.") 
        else:
            saldo= saldo + valor_deposito
            extrato.append(f"{data_formatada} ---- Depósito de R$ {valor_deposito:.2f}")

    elif opcao == 2:
        data_hora_atual = datetime.datetime.now()
        data_formatada = data_hora_atual.strftime("%Y-%m-%d %H:%M:%S")
        
        valor_saque = int(input("Digite o valor a ser sacado: "))
        if valor_saque <=0:
            print ("Valor inválido. Informa um valor válido.") 
        elif valor_saque > saldo:
            print("Saldo insuficiente para a operação. Verifique seu extrato.")
        elif valor_saque > 500:
            print ("O valor máximo diário para saque é de R$500,00")
        elif numero_saques == 3:
            print ("Você já atingiu o limite de saques diário. Tente novamente amanhã. Obrigada!")
        else:
            saldo= saldo - valor_saque
            extrato.append(f"{data_formatada} ---- Saque de R$ {valor_saque:.2f}")
            numero_saques = numero_saques + 1

    
    elif opcao == 3: 
        if extrato ==[]:
            print ("Não foram realizadas movimentações.")
        else:
            print ("====================== EXTRATO ======================\n")
            for v in extrato:
                print(v)
            print (f"\nSaldo atual: R$ {saldo:.2f}")
            print ("\n=====================================================")
                  

    elif opcao == 4:
        print ("Obrigada por usar nossos serviços! Até mais!")
        break
    else:
        print("Opção inválida. Digite uma opção válida.")
