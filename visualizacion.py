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

data = pd.read_csv('adult.csv')
analizar = DataAnalyzer(data)
info = analizar.summary()
def informacion():
    try:
        text_area.delete('1.0',tk.END)
        info = analizar.summary()
        text_area.insert(tk.END, info)
    except:
        messagebox.showerror('paila papi', 'No se puede mi papa')


ventana = tk.Tk()
ventana.title('Analisis todo es analisis aqui')

boton_summary = tk.Button(ventana, text='informacion del data frame', command= informacion)
boton_summary.pack()

text_area = ScrolledText(ventana, width= 70, height = 70)
text_area.pack()

ventana.mainloop()
