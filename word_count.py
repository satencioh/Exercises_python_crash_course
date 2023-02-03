def count_words(filename, word):
    """cuenta el numero aproximado de palabras en un archivo"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        #print(f"Perdon, el archivo {filename} no existe")
        #podemos colocar pass para indicarle a python que no muestre nada al usuario pero que aun asi capture la excepcion
        pass
    else:
        word_count = contents.lower().count(word)
        words = contents.split()
        num_words = len(words)
        print(f"el archivo {filename} tiene aproximadament {num_words} palabras y el articulo {word} aparece {word_count} veces")