# Librerías necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox, simpledialog
from PIL import ImageTk
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

        #vamos a usar las imagens para q tkinter las pueda ver

def mostrar_imagenes(pil_img):
    image_tk = ImageTk.PhotoImage(pil_img)
    image_label.configure(image=image_tk)
    image_label.image = image_tk

def mostrar_correlacion():
    img = analizar.correlation_matrix()
    mostrar_imagenes(img)

#cols hace que 
def mostrar_categorico():
    cols = analizar.df.select_dtypes(include="object").columns.tolist()
    if not cols:
        messagebox.showwarning("atencion", "el dataframe no tiene columnas. categoricas")
    else:
        sel = simpledialog.askstring("columna", f"elige una:/n{cols}")
        img = analizar.categorical_analisis_col(sel)
        mostrar_imagenes(img)
        

ventana = tk.Tk()
ventana.title("analisis de datos")

boton_summary = tk.Button(ventana, text="Resumen",command=informacion)
boton_summary.grid(row=0, column=0)

boton_numerico = tk.Button(ventana, text="Nùmerico",command=mostrar_correlacion)
boton_numerico.grid(row=0, column=0)

boton_categorico = tk.Button(ventana, text="Categorico",command=mostrar_categorico)
boton_categorico.grid(row=0, column=2)

text_area =ScrolledText(ventana, width=70, height=30)
text_area.grid(row=1, column=1)
#analizar.categorical_analisis(

content_frame = tk.Frame(ventana)
content_frame.grid(row=1, column=2)
#aqui ara mostrar imagenes
image_label = tk.Label(content_frame, text="Resultado")
image_label.grid(row=0, column=3)

ventana.mainloop()
