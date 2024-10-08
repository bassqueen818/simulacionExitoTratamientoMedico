import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title("Simulación del éxito de un tratamiento médico")
st.write("Proyecto de actividad # 3 Modelamiento y Simulación")


st.sidebar.header("Parámetros de la simulación")
st.write("Simulando el resultado de 100 pacientes que reciben un nuevo medicamento con una tasa de éxito del 80%. Un histograma muestra la frecuencia del número de tratamientos exitosos en 100 pacientes.")
p = st.sidebar.slider("Probabilidad de éxito del tratamiento de 0% a 100% (p)", 0.0, 1.0, 0.8)
n = st.sidebar.number_input("Número de tratamientos por simulación (n)", min_value=1, value=100)
simulaciones = st.sidebar.number_input("Número de simulaciones", min_value=1, value=1000)

resultados = np.random.binomial(n, p, simulaciones)

fig, ax = plt.subplots()
ax.hist(resultados, bins=20, color='deeppink', edgecolor='black')
ax.set_title("Distribución del éxito de tratamientos")
ax.set_xlabel("Número de tratamientos éxitosos")
ax.set_ylabel("Frecuencia")


st.pyplot(fig)

st.subheader("Estadísticas de la simulación")
st.write(f"Media: {np.mean(resultados):.2f}")
st.write(f"Desviación estándar: {np.std(resultados):.2f}")
st.write(f"Máximo de tratamientos exitosos: {np.max(resultados)}")
st.write(f"Mínimo de tratamientos exitosos: {np.min(resultados)}")

st.write("_________________________________________")

st.write("Realizado por:")
st.write("Camila Martinez Lopez")
st.write("Carlos Alberto Alvarez Diaz") 
st.write("Jessica Andrea Torres Fernandez") 
st.write("Marco Tulio Rueda Londoño")  
st.write("Sergio Alejandro Londoño Osorio") 
