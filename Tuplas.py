frutas = ("maçã", "laranja", "uva", "pera",)
frutas[-1] # pera
frutas[-3] # laranja

# Exemplo

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

matriz[0]   #(1, "a", 2)
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-1] # "c"

# Exemplo

tupla = ("p", "y", "t", "h", "o", "n",)

tupla[2:] # ("t", "h", "o", "n")
tupla[:2] # ("p", "y")
tupla[1:3] # ("y", "t")
tupla[0:3:2] # ("p", "t")
tupla[::] # ("p", "y", "t", "h", "o", "n",)
tupla[:: -1] # ("n", "o", "h", "t", "y", "p")

