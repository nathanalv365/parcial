class Carrito:
  def __init__(self):
      self.productos = []

  def agregar_producto(self, producto):
      self.productos.append(producto)

  def eliminar_producto(self, producto):
      if producto in self.productos:
          self.productos.remove(producto)

  def vaciar_carrito(self):
      self.productos = []

  def calcular_total(self):
      total = sum(producto.precio for producto in self.productos)
      return total

  def obtener_productos(self):
      return self.productos

class ProductoCarrito:
  def __init__(self, nombre, precio):
      self.nombre = nombre
      self.precio = precio

