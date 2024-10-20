equipamentos = []
valores = []
series = []
depertamentos = []
resposta = "S"
while resposta == "S":
    equipamentos.append(input("Equipamentos> "))
    valores.append(float(input("Valor: ")))
    series.append(int(input("Numero serial: ")))
    depertamentos.append(input("Departamentos: "))
    resposta = input("DIgite 'S' para continuar: ").upper()

if resposta == "":
    print("não tem texto")
elif resposta == "n":
    print("ok")

for equipamento in equipamentos:
        print("Equipamentos: ", equipamento)
     
        