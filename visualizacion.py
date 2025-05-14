# Librerías necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

from Analisis import DataAnalyzer

Data = pd.read_csv("adult.csv")

#Crear objeto con diferentes 
analizar = DataAnalyzer(Data)
analizar.summary()
analizar.correlation_matrix()
analizar.categorical_analisis()
