def find_anagrams(lista):
    lista_tot = []
    for palabra in lista:
        lista_mismas_letras = []
        list_palabra = list(palabra)
        for palabra_2 in lista:
            añadir = True
            for letra in palabra_2:
                if letra not in list_palabra:
                    añadir = False
                    break
            if añadir and len(palabra_2) == len(palabra):
                lista_mismas_letras.append(palabra_2)
        if lista_mismas_letras not in lista_tot:
            lista_tot.append(lista_mismas_letras) 
    return lista_tot
            

if __name__ == "__main__":
    lista = []
    num_elementos = int(input("ingrese el numero de elementos de la lista: "))
    i = 0
    while i < num_elementos:
        num = input("Ingrese las palabras a añadir a la lista: ")
        lista.append(num)
        i+=1
    lista_listas = find_anagrams(lista)
    lista_primer = lista_listas[0]
    print(lista_primer)
