# Librerías necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from Analisis import DataAnalyzer
from PIL import ImageTk
from tkinter import messagebox, simpledialog,filedialog
from PIL import ImageTk

data = pd.read_csv('adult.csv') #Puedo colocar la ruta del archivo .csv o de otro archivo .csv
analizar = DataAnalyzer(data)
info = analizar.summary()
def informacion():
    try:
        text_area.delete('1.0', tk.END)  # Limpiar el área de texto antes de mostrar la nueva información
        info = analizar.summary()
        text_area.insert(tk.END, info)
    except:
        messagebox.showerror("Error", "No se pudo obtener la información del DataFrame.")
        
def mostrar_imagenes(pill_img):
    image_tk = ImageTk.PhotoImage(pill_img)
    image_label.config(image=image_tk) #Muestra la imagen
    image_label.image = image_tk  # Mantener una referencia a la imagen para evitar que se elimine por el recolector de basura
    
def mostrar_matriz_correlacion():
    img = analizar.correlation_matrix() #muestra la matriz de correlación
    mostrar_imagenes(img) #esta función muestra la imagen de la matriz de correlación

def mostrar_categorico():
    cols = analizar.df.select_dtypes(include="object").columns.tolist()
    if not cols:
        messagebox.showwarning("Atencion", "El df no tiene col. categoricas")
    else:
        sel = simpledialog.askstring("columna", f"Elige una:\n {cols}")
        if sel in cols:
            img = analizar.categorical_analisis_col(sel)
            mostrar_imagenes(img)

def agregar_usuario():
    # Crear una nueva ventana para el formulario
    form_window = tk.Toplevel(ventana)
    form_window.title("Agregar Usuario")
    
    entries = {}
    columnas = analizar.df.columns.tolist()

    # Crear una entrada por cada columna
    for idx, col in enumerate(columnas):
        tk.Label(form_window, text=col).grid(row=idx, column=0, padx=5, pady=5)
        entry = tk.Entry(form_window)
        entry.grid(row=idx, column=1, padx=5, pady=5)
        entries[col] = entry

    def guardar_usuario():
        # Crear un diccionario con los datos ingresados
        nuevo_usuario = {}
        for col in columnas:
            val = entries[col].get()
            if col in analizar.numeric_cols:
                try:
                    val = float(val)  # Convertir a numérico si aplica
                except ValueError:
                    messagebox.showerror("Error", f"El valor de '{col}' debe ser numérico.")
                    return
            nuevo_usuario[col] = val

        # Convertir a DataFrame y agregar al original
        nuevo_df = pd.DataFrame([nuevo_usuario])
        analizar.df = pd.concat([analizar.df, nuevo_df], ignore_index=True)
        analizar.df.to_csv('adult.csv', index=False)  # Guardar al CSV original

        messagebox.showinfo("Éxito", "Usuario agregado correctamente.")
        form_window.destroy()

    # Botón para guardar
    tk.Button(form_window, text="Guardar", command=guardar_usuario).grid(row=len(columnas), column=0, columnspan=2, pady=10)
ventana = tk.Tk()
ventana.title("Análisis de Datos")

boton_summary = tk.Button(ventana, text="Resumen", command= informacion )
boton_summary.grid(row =0, column=0, padx=10, pady=10)

boton_summary = tk.Button(ventana, text="Numerico", command= mostrar_matriz_correlacion )
boton_summary.grid(row =0, column=1, padx=10, pady=10)

boton_summary = tk.Button(ventana, text="Categorico", command= mostrar_categorico)
boton_summary.grid(row =0, column=2, padx=10, pady=10)

boton_agregar = tk.Button(ventana, text="Agregar Usuario", command=agregar_usuario)
boton_agregar.grid(row=0, column=3, padx=10, pady=10)

text_area = ScrolledText(ventana, width=70, height=30)
text_area.grid(row = 1, column = 1)

content_frame = tk.Frame(ventana)
content_frame.grid(row=1, column=0, padx=10, pady=10)
# Crear un área de texto para mostrar la información
image_label = tk.Label(content_frame)
image_label.grid(row=0, column=0, padx=10, pady=10)
ventana.mainloop()