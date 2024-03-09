import tkinter as tk
from tkinter import ttk, messagebox
from autenticacion import validar_credenciales, registrar_usuario
from productos import obtener_productos_disponibles
from perfiles import abrir_ventana_perfil, obtener_descuento_financiero
from carrito import Carrito, ProductoCarrito

class AuthWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_usuario = ttk.Label(self, text="Usuario:")
        self.label_usuario.grid(row=0, column=0, padx=5, pady=5)
        self.entry_usuario = ttk.Entry(self)
        self.entry_usuario.grid(row=0, column=1, padx=5, pady=5)

        self.label_contrasena = ttk.Label(self, text="Contraseña:")
        self.label_contrasena.grid(row=1, column=0, padx=5, pady=5)
        self.entry_contrasena = ttk.Entry(self, show="*")
        self.entry_contrasena.grid(row=1, column=1, padx=5, pady=5)

        self.boton_inicio_sesion = ttk.Button(self, text="Iniciar Sesión", command=self.iniciar_sesion)
        self.boton_inicio_sesion.grid(row=2, column=0, padx=5, pady=5)

        self.boton_registro = ttk.Button(self, text="Registrarse", command=self.registrar)
        self.boton_registro.grid(row=2, column=1, padx=5, pady=5)

    def iniciar_sesion(self):
        usuario = self.entry_usuario.get()
        contrasena = self.entry_contrasena.get()
        if validar_credenciales(usuario, contrasena):
            messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso.")
            self.master.destroy()  # Cerrar la ventana de inicio de sesión
            open_store_window(usuario)  # Pasar el usuario como argumento
        else:
            messagebox.showerror("Error", "Credenciales inválidas.")

    def registrar(self):
        usuario = self.entry_usuario.get()
        contrasena = self.entry_contrasena.get()
        if registrar_usuario(usuario, contrasena):
            messagebox.showinfo("Registro", "Usuario registrado correctamente.")
        else:
            messagebox.showerror("Error", "El usuario ya está registrado.")

class StoreWindow(tk.Toplevel):
    def __init__(self, master, usuario):
        super().__init__(master)
        self.usuario = usuario
        self.carrito = Carrito()
        self.title("Tienda")
        self.geometry("800x600")

        label_tienda = ttk.Label(self, text="¡Bienvenido a la Tienda!", font=("Helvetica", 16, "bold"))
        label_tienda.pack(pady=10)

        # Botón para abrir la ventana de perfil
        boton_perfil = ttk.Button(self, text="Perfil", command=self.abrir_ventana_perfil)
        boton_perfil.pack(pady=5)

        # Botón para abrir el carrito de compras
        self.boton_carrito = ttk.Button(self, text="Ver Carrito", command=self.abrir_ventana_carrito)
        self.boton_carrito.pack(pady=5)

        self.frame_productos = ttk.Frame(self)
        self.frame_productos.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        self.mostrar_productos()  # Llama al método después de que esté definido

    def abrir_ventana_perfil(self):
        abrir_ventana_perfil(self)

    def mostrar_productos(self):
        productos_disponibles = obtener_productos_disponibles()
        contenedor_columnas = ttk.Frame(self.frame_productos)  # Contenedor maestro para las columnas
        contenedor_columnas.pack(fill=tk.BOTH, expand=True)
        columnas = {}  # Diccionario para almacenar las columnas por categoría
        for categoria, producto, precio in productos_disponibles:
            if categoria not in columnas:
                columnas[categoria] = ttk.Frame(contenedor_columnas)
                columnas[categoria].pack(side=tk.LEFT, padx=10, pady=10, fill=tk.Y)
                ttk.Label(columnas[categoria], text=categoria, font=("Helvetica", 12, "bold")).pack(anchor="w")
            ttk.Label(columnas[categoria], text=f"{producto} - ${precio}").pack(anchor="w")
            boton_agregar = ttk.Button(columnas[categoria], text="Agregar al Carrito", command=lambda cat=categoria, prod=producto, prec=precio: self.agregar_producto_al_carrito(cat, prod, prec))
            boton_agregar.pack(anchor="w")

    def abrir_ventana_carrito(self):
        ventana_carrito = tk.Toplevel(self)
        ventana_carrito.title("Carrito de Compras")
        self.mostrar_carrito(ventana_carrito)  # Llama al método para mostrar el carrito

    def mostrar_carrito(self, ventana_carrito):
        ttk.Label(ventana_carrito, text="Carrito de Compras").pack()
        productos_en_carrito = self.carrito.obtener_productos()
        for producto in productos_en_carrito:
            ttk.Label(ventana_carrito, text=f"{producto.nombre} - ${producto.precio}").pack()
        ttk.Label(ventana_carrito, text=f"Total: ${self.carrito.calcular_total()}").pack()

        boton_pagar = ttk.Button(ventana_carrito, text="Pagar", command=self.pagar)
        boton_pagar.pack(pady=5)

    def agregar_producto_al_carrito(self, categoria, producto, precio):
        messagebox.showinfo("Carrito", f"Se agregó {producto} al carrito de compras.")
        self.carrito.agregar_producto(ProductoCarrito(producto, precio))

    def pagar(self):
        total = self.carrito.calcular_total()
        descuento = obtener_descuento_financiero(self.usuario, total)
        total_con_descuento = total - descuento
        messagebox.showinfo("Pago", f"Total a pagar: ${total_con_descuento} (Descuento aplicado: ${descuento}). ¡Gracias por su compra!")
        self.carrito.vaciar_carrito()

def open_auth_window():
    auth_window = tk.Tk()
    auth_window.title("Bienvenido")
    auth_frame = AuthWindow(auth_window)
    auth_frame.pack(padx=20, pady=20)

def open_store_window(usuario):
    store_window = tk.Toplevel()
    store_window.title("Tienda")
    StoreWindow(store_window, usuario)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Bienvenido")
    ttk.Button(root, text="Iniciar Sesión", command=open_auth_window).pack(pady=10)
    root.mainloop()
