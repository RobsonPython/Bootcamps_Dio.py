lista = []

lista.append(1)
lista.append("python")
lista.append([40,30, 20])

print(lista)  # [1,  "python", [40,30, 20]]

# [].clear

lista = [1,  "python", [40, 30,  20]]

print(lista)    #[1,  "python", [40, 30,  20]]

lista.clear()

print(lista)    # []

lista.copy()
print(lista)