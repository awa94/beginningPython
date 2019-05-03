

# CONDICIONALESSSS

x = input("Inserta tu edad")

if int(x)>18:
    x = input("Dime tu nombre")
    if x.lower() == "iris":
        print("Eres una genio!!")   
    else:
        print("Eres un simple humano normal") 
else:
    print("No puedes continuar por que no puedes consumir alcohol")

# SI quiero que realice mas de una accion para una condicion indicada, lo tengo que poner justo debajo de la condicion
# El propio entorno me va a indicar lo que se va a ejecutar y no... cualquiero cosa que quiero que se ejecute, la pongo debajo 
# y tabulada, para que entre dentro de la condicion

# Estos son los operadores logicos:
if int(x) > 2 and int(x) < 10:
     print("Eres muy chiquitin") 
    