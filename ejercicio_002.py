nombre = input("Como te llamas? ")

sexo = input("Cual es tu sexo? M para mujer o H para hombre")

if (sexo == "M" and nombre.lower()< 'm') or (sexo == "H" and nombre.lower()> 'n'):
    grupo = "A"
else:
    grupo = "B"
print("Tu grupo es: "+ grupo)