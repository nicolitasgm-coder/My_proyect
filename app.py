from flask import Flask

# Creamos la aplicación
app = Flask(__name__)

# Definimos una ruta principal
@app.route("/")
def home():
    return "Hola, Render está funcionando 🚀"

# Esto asegura que se ejecute en Render
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('../vehicles_us.csv')
st.header('Evaluacion de Carros en US')
st.write('Esta aplicacion aun no es funcional. En construccion')

hist_button = st.button('Construir histograma')
if hist_button:
    st.write('Creacion de un histograma para el conjunto de datos de anuncios de venta de vehiculos')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

dis_button = st.button('Construir Dispersion')
if dis_button:
    st.write('Creacion de la dispersion para el sonjunto de datos de anuncion de venta de vehiculos')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
