lista = [1,0.4,True,"Todo esta permitido"]
colores = ["azul","verde","rojo","rosa"]
numeros = [1,2,3,4,5,"..."]

# Por ejemplo para crear una lista a partir de rango que yo le indique..
numeros = list(range(1,11))
print(numeros)

# Saber la longitud de una lista
print(len(numeros))

# Saber la posicion de un elemento...
print(colores[0])
# Me devuelve un booleano que dice si existe o no...sirve para buscar...
print('azul' in colores)
print('Azul' in colores)

# Para cambiar, osea ser, reemplazar.
colores[3] = "amarillo"
print(colores)

# Para añadir elementos al final de la lista...
colores.append("violeta")
#Para añadir mas de uno
colores.extend(("violeta","marron"))
#Para añadir elementos en la posicion que YO quiera
colores.insert(2,"naranja")
colores.insert(-2,"turquesa")
# o al final...
colores.insert(len(colores),"pistacho")

print(colores)

#Para eliminar elementos desde el final de la lista...
colores.pop()
#Si quiero eliminar un valor en especifico: 
#Si existe mas de una vez, entonces se eleminara solo la primera ocurrencia
colores.remove("violeta")
#Si quiero eliminar un valor a partir de un índice.
colores.pop(0)

print(colores)

# para dejar la lista VACIA
numeros.clear()
print(numeros)

# Para ordenar, se hace con sort
colores.sort()
print(colores)
# Para ordenar de forma invertida
colores.sort(reverse=True)
print(colores)

# Para saber el index de la posicion de un elemento
print(colores.index("naranja"))
# Para saber el numero de ocurrencias que tiene eese elemento
colores.append("violeta")
print(colores.count("violeta"))



















