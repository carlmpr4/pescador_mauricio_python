def length_words(frase):
    palabras = frase.split()
    largo = map(len, palabras)
    return dict(zip(palabras, largo))

print(length_words('Hola Mundo'))