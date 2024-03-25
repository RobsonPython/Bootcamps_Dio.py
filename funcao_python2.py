# Positional only

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
    
#criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

#criar_carro(modelo="palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")


# Keyword only

def criar_carro(modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
    
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="gasolina")

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

#Palio 1999 ABC-1234 Fiat 1.0 gasolina
#Palio 1999 ABC-1234 Fiat 1.0 Gasolina

# exemplo

salario = 2000

def salario_bonus(bonus, lista):
    global salario
   
    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista aux={lista_aux}")
    
    salario += bonus
    return salario

lista = [1]

salario_com_bonus = salario_bonus(500, lista)
print(salario_com_bonus)
print(lista)

#lista aux=[1, 2]
#2500
#[1]