#metodo: append.py
inventario=[]
resposta="S"
while resposta=="S":
    inventario.append(input("equipamento: "))
    inventario.append(input("valor: "))
    inventario.append(input("numero de serie: "))
    resposta=input("digite 'S' para continuar: ").upper()
for elemento in inventario:
    print(elemento)