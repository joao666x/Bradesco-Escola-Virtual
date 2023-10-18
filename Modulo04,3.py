notaA = float(input("Nota A: "))
notaB =float(input("Nota B: "))

#calcular media
mediafinal = (notaA + notaB) /2

#verifica
if mediafinal >=7:
    print("Media: %.1f - APROVADO"% mediafinal)
else:
    print("Media: %.1f - REPROVADO"% mediafinal)
