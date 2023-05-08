from datetime import datetime

nombre =  input('Cual es tu nombre?\n')
numvocales = [nombre.count(x) for x in "aeiouAEIOU"]
apellido1 =  input('Cual es tu primer apellido?\n')
apellido2 =  input('Cual es tu segundo apellido?\n')
anio =  input('En que anio naciste?\n')
mesdia =  input('En que mes y dia naciste? (en el sgte formado "mm-dd")\n')
fechanac = mesdia+"-"+ anio 
#+ " 00:00:00"
print(fechanac)
fechanac2 = datetime.strptime(fechanac,"%m-%d-%Y")

print(fechanac2)
edad =  datetime.today().year - fechanac2.year
print (edad)
print('Este es tu nombre completo en mayusculas: ' + nombre.upper())
print('Este es tu nombre completo en mayusculas: ' + nombre.upper() + " " + apellido1.upper() + " " + apellido2.upper())
print('Este es tu nombre completo en minusculas: ' + nombre.lower() + " " + apellido1.lower() + " " + apellido2.lower())
#print('Esta es tu fecha de nacimiento:' )
print('Esta es tu edad: ' + str(edad) )
print('Tu nombre completo tiene: ' + str(sum(numvocales)) + ' vocales' )
print('Tu nombre completo tiene: ' + str(len(nombre)+len(apellido1)+len(apellido2)) + ' letras')
