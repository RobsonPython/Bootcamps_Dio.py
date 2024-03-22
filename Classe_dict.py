# {}.clear
contatos = {
    "robson@gmail.com": {"nome": "Robson", "telefone": "4444-1020"},
    "elionai@gmail.com":{"nome": "Elionai", "telefone": "3523-6429"},
    "rodrigo@gmail.com":{"nome": "Rodrigo", "telefone": "3854-4023"},
    "bruno@gmail.com": {"nome": "Bruno", "telefone": "5555-2356"},
}

contatos.clear()
contatos # {}

# {}.copy

contatos = {
    "robson@gmail.com": {"nome": "Robson", "telefone": "4444-1020"},   
}

copia = contatos.copy()
copia["Robson@gmail.com"] = {"nome": "Rob"}
print(copia["Robson@gmail.com"])

contatos["robson@gmail.com"]
print(contatos["robson@gmail.com"])

print(copia["Robson@gmail.com"])

# {}.fromkeys

dict.fromkey(["nome", "telefone"])

# {}.get

contatos = {
    "robson@gmail.com": {"nome": "Robson", "telefone": "4444-1020"}
}

contatos["robson@gmail.com"]
contatos["robson@gmail.com"]

contatos = ("chave")




contatos.get("robson@gmail.com", {})

resultado = contatos.get(
    "robson@gmail.com", {}
) 
print(resultado)

resultado = contatos.setdefault()


# {}.del

contatos = {
    "robson@gmail.com": {"nome": "Robson", "telefone": "4444-1020"},
    "elionai@gmail.com":{"nome": "Elionai", "telefone": "3523-6429"},
    "rodrigo@gmail.com":{"nome": "Rodrigo", "telefone": "3854-4023"},
    "bruno@gmail.com": {"nome": "Bruno", "telefone": "5555-2356"},
}

del contatos["robson@gmail.com"]["telefone"]
