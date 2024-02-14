def filtrar_mismas_letras(lista):
    lista_listas = []
    lista_num_letras = []
    for palabra in lista:
        lista_num_letras.append(len(palabra))
    set_num_letras = set(lista_num_letras)
    for num in set_num_letras:
        lista_palabras = []
        for palabra in lista:
            if len(palabra) == num:
                lista_palabras.append(palabra)
        lista_listas.append(lista_palabras)
    return lista_listas


if __name__ == "__main__":
    lista = []
    num_elementos = int(input("ingrese el numero de elementos de la lista: "))
    i = 0
    while i < num_elementos:
        num = input("Ingrese las palabras a añadir a la lista: ")
        lista.append(num)
        i+=1
    lista_listas = filtrar_mismas_letras(lista)
    for lista in lista_listas:
        print(lista)