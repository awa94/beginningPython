texto = "Esto es un texto que me va a decir todo lo que puedo hacer con los strings"

#Esta función devuelve una lista ordenada alfabéticamente de los métodos y propiedades de algún objeto
#En este caso de los strings:
print(dir(texto))

#Esto lo convierte a mayuscula, y se llaman de esta manera
print(texto.upper())
print(texto.lower())
#Esto convierte en contrario lo que antes estaba en mayus ahora en minus, etc...
print(texto.swapcase())
print(texto.capitalize())

# Para reemplazar: 
print(texto.replace("es un", "no es un"))
#Para contar numero de letras y se convierte en un numero
print(texto.count("a"))
print(texto.count(" "))

#Esto devuelve un booleano que nos dice si el string que tengo empieza con la palabra que le meta por parametro
print(texto.startswith("esto"))
print(texto.lower().startswith("esto"))

# Esto hace lo mismo que el anterior pero sabiendo si acaba con lo que le pase por parametro.
print(texto.endswith("STRINGS"))
print(texto.upper().endswith("STRINGS"))

#Para poder dividir el texto usamos split. Esto lo divide en una cadena de palabras, lo almacena en una lista 
print(texto.split())
#Si queremos que lo divida basado en algun parametro que yo quiera, por ejemplo una coma, en vez de por defecto que es un espacio
print(texto.split("o"))

#Si queremos saber si tenemos algo dentro de esa cadena o no, nos devuelve la primera posicion donde aparece esa ocurrencia.
print(texto.find("o"))

#Para saber el tamaño entero de esa cadena, que nos devuelva la longitud.
print(len(texto))

# Para saber el indice de la palabra e.
print(texto.index("e"))

#Para saber si es o no numerico:
print(texto.isnumeric())
print(texto.isalpha())

#Si por ejemplo quiero imprimir solo la posicion
print(texto[1])
# Para saber el que hay desde la cola al final:
print(texto[-2])

#Para concatenar: con el "+"
print("¿QUÉ es esto? "+texto)
#Otra forma de imprimirlo es asi
print(f"¿QUe es esto? {texto}")
# Y otra manera es con format
print("¿QUe es esto? {0}".format(texto))