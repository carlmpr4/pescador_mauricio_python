fruits = {'platano':1.35, 'manzana':0.80, 'pera':0.85, 'naranja':0.70}
fruit = input('¿Qué fruta quieres? ').title()
kg = float(input('¿Cuántos kilos? '))
if fruit in fruits:
    print(kg, 'kilos de', fruit, 'valen', fruits[fruit]*kg )
else: 
    print("Lo siento, la fruta", fruit, "no está disponible.")