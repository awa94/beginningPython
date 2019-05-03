libros = {
    "name": "Libro1",
    "quantity": 3,
    "price": 23.45,
    "autor": {
        "nombre": "Pepita Perez",
        "apellito": "Perez"
    },
    "fec_publicacion": "23/24/94"
}

print(libros)

# Si solo quiero conocer las KEYS:
print(libros.keys())

# Si solo quiero conocer los items que contiene.
print(libros.items())

# Por ejemplo si tengo muchos libross, los puedo meter en una lista.
productos = [
    {"name": "Television","precio": 23.84},
    {"name": "Television","precio": 23.84}
]


print(productos)