# productos.py

productos = {
    "Ropa": {"Camiseta": 10, "Pantalón": 20, "Vestido": 30},
    "Electrodomésticos": {"Nevera": 500, "Lavadora": 400, "Televisor": 300},
    "Hogar": {"Mesa": 50, "Silla": 25, "Sofá": 200}
}

promocion = {"Pantalón": 15, "Televisor": 250, "Mesa": 40}

def obtener_productos_disponibles():
    productos_disponibles = []
    for categoria, productos_categoria in productos.items():
        for producto, precio in productos_categoria.items():
            precio_final = precio
            if producto in promocion:
                precio_final = promocion[producto]
            productos_disponibles.append((categoria, producto, precio_final))  # Devuelve una tupla
    return productos_disponibles
