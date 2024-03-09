# perfiles.py

import tkinter as tk
from tkinter import ttk

nombre_usuario = ""
direccion_usuario = ""
tiene_tarjeta = False
tiene_seguro = False
tiene_fidelizacion = False

def guardar_cambios_perfil(entry_nombre, entry_direccion, var_tarjeta, var_seguro, var_fidelizacion):
    global nombre_usuario, direccion_usuario, tiene_tarjeta, tiene_seguro, tiene_fidelizacion
    nombre_usuario = entry_nombre.get()
    direccion_usuario = entry_direccion.get()
    tiene_tarjeta = var_tarjeta.get()
    tiene_seguro = var_seguro.get()
    tiene_fidelizacion = var_fidelizacion.get()

def abrir_ventana_perfil(root):
    ventana_perfil = tk.Toplevel(root)
    ventana_perfil.title("Perfil de Usuario")

    ttk.Label(ventana_perfil, text="Perfil de Usuario", font=("Helvetica", 16, "bold")).pack(pady=10)

    ttk.Label(ventana_perfil, text="Nombre:").pack()
    entry_nombre = ttk.Entry(ventana_perfil)
    entry_nombre.pack()
    entry_nombre.insert(0, nombre_usuario)

    ttk.Label(ventana_perfil, text="Dirección:").pack()
    entry_direccion = ttk.Entry(ventana_perfil)
    entry_direccion.pack()
    entry_direccion.insert(0, direccion_usuario)

    ttk.Label(ventana_perfil, text="Beneficios Financieros", font=("Helvetica", 12, "bold")).pack()

    var_tarjeta = tk.BooleanVar(value=tiene_tarjeta)
    var_seguro = tk.BooleanVar(value=tiene_seguro)
    var_fidelizacion = tk.BooleanVar(value=tiene_fidelizacion)

    ttk.Checkbutton(ventana_perfil, text="Tarjeta de Crédito", variable=var_tarjeta).pack()
    ttk.Checkbutton(ventana_perfil, text="Seguro", variable=var_seguro).pack()
    ttk.Checkbutton(ventana_perfil, text="Programa de Fidelización", variable=var_fidelizacion).pack()

    ttk.Button(ventana_perfil, text="Guardar Cambios", command=lambda: guardar_cambios_perfil(entry_nombre, entry_direccion, var_tarjeta, var_seguro, var_fidelizacion)).pack(pady=10)
  
def obtener_descuento_financiero(usuario, total):
  global tiene_tarjeta, tiene_seguro, tiene_fidelizacion
  descuento = 0
  if tiene_tarjeta:
      descuento += total * 0.05  # Descuento del 5% para usuarios con tarjeta de crédito
  if tiene_seguro:
      descuento += total * 0.1   # Descuento del 10% para usuarios con seguro
  if tiene_fidelizacion:
      descuento += total * 0.15  # Descuento del 15% para usuarios con programa de fidelización
  return descuento

