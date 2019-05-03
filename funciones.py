def hello(name="humano"):
    print("Hello World "+name)


hello()
hello("pepa")
hello("juana")

def suma(numberOne,numberTwo):
    return numberOne+numberTwo

print(suma(5,5))


# Esto es otra forma de declarar funciones.
# Estas son las funciones lambda
resta = lambda numberOne, numberTwo : numberOne - numberTwo

print(resta(10,5))