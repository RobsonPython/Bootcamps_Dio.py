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

linguagens = ["python", "js", "c"]

print(linguagens)   #["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens)   # ["python", "js", "c", "java", "csharp"]

# [].Index
linguagens = ["python", "java", "c", "java", "csharp"]

print(linguagens.index("java")) # 3
print(linguagens.index("python"))   # 0

# [].Pop

linguagens  = ["python", "js", "c", "java", "csharp"]

linguagens.pop() # csharp
linguagens.pop() # java
linguagens.pop() # c
linguagens.pop(0) # python



