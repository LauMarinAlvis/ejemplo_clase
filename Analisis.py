# Librerías necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

data = pd.read_csv("adult.csv")
print(data.head(4))

#hacer analisis generico de los datos usaremos una clase
class DataAnalyzer:
    def __init__(self, df):#defino la clase
        self.df = df#definiendo el dataframe el self trabaja el objeto, es como un valor local que el contructor le dice que permanezca a tal

    def summary(self):#aqui es para que pida un resumen
        print(self.df.info())#me da el tipo de dato
        print(self.df.describe())#hace un conteo un promedio, el minimo, la desvicion, el maximo estadistia o cuartiles

    def missing_values(self):
        return self.df.isnull().sum()

    def imprimir (self):
        print("Hello")


    def correlation_matrix(self):
        numeric_cols = self.df.select_dtypes(include=np.number).columns
        corr = self.df[numeric_cols].corr()
        plt.figure()#luego de esto debo decir que quiero hacer en setido de graficas
        sns.heatmap(corr, annot =True, cmap ='coolwarm')#mapa de calor aqui le digo que me selñae con color entre mas rojo mas correlacion hay
        plt.title('Matriz de Correlación')
        plt.show()

    def categorical_analisis(self):
        categorical_cols = self.df.select_dtypes(include='object').columns
        print(f"las columnas categoricas son: {categorical_cols}")
        column = input("digite la columna a visualizar: ")

        if column in categorical_cols:
            plt.figure()
            sns.countplot(data = self.df, x= column, order = self.df[column].value_counts().index)
            plt.xticks(rotation= 45)
            plt.show()

        else:
            print("la columna no es categorica o esta mal escrita")





