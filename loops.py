foods = ["manzanas", "queso", "leche", "avena"]

# Así se recorren las listas :D
for food in foods:
    if food == foods[0]:
        print("Tenemos que comprar "+food,end="")
    else:
        if food == foods[len(foods)-1]:
            print(" y "+food+".")
        else:
            print(", "+food,end="")


count = 4
while count<=10:
    print(count)
    count = count +1