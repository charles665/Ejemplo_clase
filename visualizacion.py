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
        
        
ventana = tk.Tk()
ventana.title("Análisis de Datos")

boton_summary = tk.Button(ventana, text="Resumen", command= informacion )
boton_summary.grid(row =0, column=0, padx=10, pady=10)

boton_summary = tk.Button(ventana, text="Numerico", command= mostrar_matriz_correlacion )
boton_summary.grid(row =0, column=1, padx=10, pady=10)

boton_summary = tk.Button(ventana, text="Categorico", command= mostrar_categorico )
boton_summary.grid(row =0, column=2, padx=10, pady=10)

text_area = ScrolledText(ventana, width=70, height=30)
text_area.grid(row = 1, column = 1)

content_frame = tk.Frame(ventana)
content_frame.grid(row=1, column=0, padx=10, pady=10)
# Crear un área de texto para mostrar la información
image_label = tk.Label(content_frame)
image_label.grid(row=0, column=0, padx=10, pady=10)
ventana.mainloop()