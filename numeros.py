# En las variables obviamente se puede sumar, etc...
# Para pedir datos hay una funcion...
edad = input("Dime tu edad: ")
nueva_edad = edad*23
print("Tu edad es: "+nueva_edad)
#Esto nos devuelve 23 veces el numero repetido... 
#TOSO LO QUE LE MANDAMOS AL PROGRAMA ES UN STRING. SI QUEREMOS REALIZAR OPERACIONES HAY QUE HACERLO convirtiendolo a string
nueva_edad = int(edad) *23

print("En realidad, tu edad en Júpiter es: "+ str(nueva_edad))