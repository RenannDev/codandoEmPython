#for item in sequencia:
  # bloco de código a ser executado para cada item
#item: Uma variável que assume o valor de cada elemento da sequência em cada iteração.
#sequencia: A lista, tupla, string ou outro objeto iterável que você quer percorrer.

#range: cria uma sequência de números. range( 1inicio, 11stop, 1incremento)

""" enumerate(): Retorna um índice para cada elemento da sequência.

for indice, valor in enumerate(frutas):
  print(f"Na posição {indice}, temos a fruta {valor}")


zip(): Combina elementos de múltiplas sequências.

nomes = ["Alice", "Bob", "Charlie"]
idades = [25, 30, 28]
for nome, idade in zip(nomes, idades):
  print(f"{nome} tem {idade} anos.")

"""

tabuada=int(input("Digite um numero para a tabuada desejada: "))
print("Tabuada do numero: ", tabuada)
for valor in range(1, 11, 1):
    print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada*valor)))
