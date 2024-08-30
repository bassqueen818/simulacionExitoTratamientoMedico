import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Título de la aplicación
st.title("Simulación del Éxito de un Tratamiento Médico")

# Sidebar para ajustar parámetros
st.sidebar.header("Parámetros de Simulación")
p = st.sidebar.slider("Probabilidad de éxito del tratamiento (p)", 0.0, 1.0, 0.8)
n = st.sidebar.number_input("Número de tratamientos por simulación (n)", min_value=1, value=100)
simulaciones = st.sidebar.number_input("Número de simulaciones", min_value=1, value=1000)

# Simular los ensayos de Bernoulli
resultados = np.random.binomial(n, p, simulaciones)

# Graficar los resultados
fig, ax = plt.subplots()
ax.hist(resultados, bins=20, color='blue', edgecolor='black')
ax.set_title("Distribución del Éxito de Tratamientos")
ax.set_xlabel("Número de Tratamientos Exitosos")
ax.set_ylabel("Frecuencia")

# Mostrar la gráfica en la aplicación
st.pyplot(fig)

# Mostrar estadísticos básicos
st.subheader("Estadísticas de la Simulación")
st.write(f"Media: {np.mean(resultados):.2f}")
st.write(f"Desviación estándar: {np.std(resultados):.2f}")
st.write(f"Máximo de tratamientos exitosos: {np.max(resultados)}")
st.write(f"Mínimo de tratamientos exitosos: {np.min(resultados)}")
