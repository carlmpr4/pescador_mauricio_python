datos = {'nombres':'Carlos Mauricio', 'primer_apellido':'Pescador', 'segundo_apellido':'Rosas', 'fecha_nacimiento':'30-Dic-1987', 'celular': 3314395799, 'correo':'carlmpr4@gmail.com', 'domicilio':'Mazatlan', 'genero':'Masculino', 'objetivo': 'Aprender Python', 'salario_esperado': 1000000}
skills = list(('SQL', 'PLSQL','OBIEE','Python Basico' ))
trabajo1 = {'lugar_trabajo':'TCS',
             'anio_inicio': 2010, 
             'anio_fin': 2012,
             'puesto': 'Trainee'}

trabajo2 = {'lugar_trabajo':'Oracle',
             'anio_inicio': 2012, 
             'anio_fin': 2023 ,
             'puesto': 'Developer'}

mistrabajos = {
    "PrimerTrabajo" : trabajo1,
    "SegundoTrabajo" : trabajo2
}

trabajo = {'lugar_trabajo': ['TCS','Oracle'], 'anio_inicio': [2010, 2012], 'anio_fin': [2012, 2023], 'puesto': ['Trainee','Developer'] }

print(f'Los datos personales de este muchacho son: \n -------- \nNombre: {datos["nombres"]} \nApellidos: {datos["primer_apellido"]} {datos["segundo_apellido"]} \nNacio en: {datos["fecha_nacimiento"]} \nTel de contacto: {datos["celular"]} \nCorreo: {datos["correo"]} \nGenero: {datos["genero"]} \nObjetivo: {datos["objetivo"]} \nSalario Esperado: {datos["salario_esperado"]} ')
print(f'Las habilidades que esta persona tiene son: {skills} \n-------')
claves = datos.values()
nombre = datos.get("nombres")
#print (trabajos)
print(f'Trabajo anterior 1: \n- Empresa:{trabajo["lugar_trabajo"][0]} \n- Fecha Inicio: {trabajo["anio_inicio"][0]} \n- Fecha Fin: {trabajo["anio_fin"][0]} \n- Puesto: {trabajo["puesto"][0]} ')
print('--------')
print(f'Trabajo anterior 2: \n- Empresa:{trabajo["lugar_trabajo"][1]} \n- Fecha Inicio: {trabajo["anio_inicio"][1]} \n- Fecha Fin: {trabajo["anio_fin"][1]} \n- Puesto: {trabajo["puesto"][1]} ')