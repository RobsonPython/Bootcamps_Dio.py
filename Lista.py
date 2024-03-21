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

# [].sort

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()   # ["c", "csharp", "java", "js", "python"]

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)   # ["python", "js", "java", "csharp", "c"]

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))   # ["c", "js", "java", "python", "csharp"]

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True) #  ["python", "csharp", "java", "js", "c"]

# len

linguagens = ["python", "js", "c", "java", "csharp"]

len(linguagens) # 5

# sortd

linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))    # ["c", "js", "java", "python", "csharp"]

print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]


