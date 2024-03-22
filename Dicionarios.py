#  Exemplo 1

pessoa = {"nome": "Robson", "idade": 31}

pessoa = dict(nome="Robson", idade=31)

pessoa["telefone"] = "4444-1020" # {"nome": "Robson", "idade": 31, "telefone": "4444-1020"} 
print(pessoa["telefone"])

# Exemplo 2

dados = {"nome": "Robson", "idade": 31, "telefone": "4444-1020"}

print(dados["nome"])
print(dados["idade"])
print(dados["telefone"])

dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9955-1235"


# Exemplo 3

contatos = {
    "robson@gmail.com": {"nome": "Robson", "telefone": "4444-1020"},
    "elionai@gmail.com":{"nome": "Elionai", "telefone": "3523-6429", "extra": {"a": 1}},
    "rodrigo@gmail.com":{"nome": "Rodrigo", "telefone": "3854-4023"},
    "bruno@gmail.com": {"nome": "Bruno", "telefone": "5555-2356"},
}

extra =  contatos["elionai@gmail.com"]["extra"]
print(extra)

print(contatos["elionai@gmail.com"]["nome"])


# Exemplo 4

for chave in contatos:
    print(chave, contatos["elionai@gmail.com"])
    
# robson@gmail.com {'nome': 'Elionai', 'telefone': '3523-6429', 'extra': {'a': 1}}
# elionai@gmail.com {'nome': 'Elionai', 'telefone': '3523-6429', 'extra': {'a': 1}}
# rodrigo@gmail.com {'nome': 'Elionai', 'telefone': '3523-6429', 'extra': {'a': 1}}
# bruno@gmail.com {'nome': 'Elionai', 'telefone': '3523-6429', 'extra': {'a': 1}}
    
for chave, valor in contatos.items():
    print(chave, valor)

# robson@gmail.com {'nome': 'Robson', 'telefone': '4444-1020'}
# elionai@gmail.com {'nome': 'Elionai', 'telefone': '3523-6429', 'extra': {'a': 1}}
# rodrigo@gmail.com {'nome': 'Rodrigo', 'telefone': '3854-4023'}
# bruno@gmail.com {'nome': 'Bruno', 'telefone': '5555-2356'}