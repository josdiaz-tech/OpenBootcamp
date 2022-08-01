peso = int(input("Por favor ingrese su peso en kg: "))
estatura = float(input("Por favor ingrese su estatura en metros (ejm: 1.82): "))

indice_de_masa = round(peso/estatura**2,2)

print("Tu indice de mas corporal es: " + str(indice_de_masa))

