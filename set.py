# Los sets sonserie de valores, conjuntos de datos, son colecciones desordenadas que no tienen indices...
sets = {"rojo", "verde","rosa"}
print(sets)

print(dir(sets))
# Como no tiene indice, al agregar algo, lo agrega al principio.
sets.add("violeta")
print(sets)

# Si un set no tiene ningun valor dentro pero sin embargo está declarado, entonces, se queda como un set.

sets.clear()
print(sets)

