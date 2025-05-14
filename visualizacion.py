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

Data = pd.read_csv("adult.csv")
analizar = DataAnalyzer(Data) #Crear objeto con diferentes 


def informacion():
    try:
        text_area.delete ("1.0", tk.END)#para vaciar al ejecutar
        info = analizar.summary()
        text_area.insert(tk.END, info)
    except:
        messagebox.showerror("error", "no se puede")

ventana = tk.Tk()
ventana.title("analisis de datos")

boton_summary = tk.Button(ventana, text="informacion",)
boton_summary.pack()

xt_area = ScrolledText(ventana, width=60, height=29)
xt_area.pack()
#analizar.categorical_analisis(


ventana.mainloop()
