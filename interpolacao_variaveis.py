nome = "Robson"
idade = 31
profissao = "Estudante de programaçao"
linguagem = "Python"


print("Olá, me chamo %s. Eu tenho %d anos de idade, Minha profissão como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

print("Olá, me chamo {}. Eu tenho {} anos de idade, Minha profissão como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, minha profissão como {1} e estou matriculado no curso de {0}.". format(linguagem, profissao, idade, nome))


# Formatação string com f-string

pi = 3.14159

print(f"Valor de PI: {pi:.2f}")

print(f"Valor de PI: {pi:.9f}")

print(f"Valor de PI: {pi:.5f}")