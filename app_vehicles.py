import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar el dataset
car_data = pd.read_csv('vehicles_us.csv')

# Definir un Encabezado
st.header("Análisis de Anuncio de Ventas de Vehículos")

# Mostrar el dataset en la aplicación en una tabla
st.subheader("Conjunto de Datos de Anuncio de Ventas de Vehículos")
st.dataframe(car_data)

# Casillas de verificación para elegir el tipo de gráfico a crear
st.subheader("Selecciona el tipo de gráfico a crear:")
build_hist = st.checkbox("Crear Histograma de Kilómetros Recorridos")
build_scatter = st.checkbox("Crear Gráfico de Dispersión de Precio vs Año")

# Si la casilla de Histograma está seleccionada, generamos un histograma
if build_hist: 
    # Escribir un mensaje
    st.write("Creando histograma para el conjunto de datos de anuncio de ventas de vehículos...")   
    st.subheader("Histograma de Kilómetros Recorridos")
    # Crear un histograma
    fig = px.histogram(car_data, x='odometer')
    # Mostrar el histograma
    st.plotly_chart(fig, use_container_width=True)

# Si la casilla de Diagrama de Dispersión está seleccionada, generamos un diagrama de dispersión
if build_scatter: 
    # Escribir un mensaje
    st.write("Creando gráfico de dispersión para el conjunto de datos de anuncio de ventas de vehículos...") 
    st.subheader("Gráfico de Dispersión de Precio vs Año")  
    # Crear un gráfico de dispersión
    fig = px.scatter(car_data, x='price', y='model_year', title='Gráfico de Dispersión de Precio vs Año')
    # Mostrar el gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)  
