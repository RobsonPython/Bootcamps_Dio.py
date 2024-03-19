# Exemplo if and Else
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")
else:
    print("Saldo insuficiente!")
    
#exemplo de elif
opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
    #...
elif opcao == 2:
    print("Exibindo o extrato ... ")
else:
    sys.exit("Opção inválida")

# Praticando 
MAIOR_IDADE= 18

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
    
if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")
    

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
else:
    print("Ainda não pode tirar a CNH.")