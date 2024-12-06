import streamlit as st

# Título de la aplicación
st.title('Calculadora de ROI para Proyectos')

# Entrada de datos
inversion = st.number_input('Ingrese el costo de la inversión', min_value=1)
beneficio = st.number_input('Ingrese el beneficio neto generado', min_value=0)

# Calcular el ROI
if inversion > 0:
    roi = (beneficio / inversion) * 100
    st.write(f'El ROI del proyecto es: {roi:.2f}%')

    # Interpretar el resultado del ROI
    if roi > 20:
        st.success("¡Excelente! El proyecto fue muy rentable.")
    elif roi >= 5:
        st.success("¡Buen trabajo! El proyecto fue rentable.")
    else:
        st.warning("¡Cuidado! El proyecto apenas fue rentable.")
else:
    st.error("El costo de la inversión debe ser mayor a 0.")
