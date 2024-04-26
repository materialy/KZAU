import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Definice funkce pro simulaci regulátoru
def simulate_regulator(regulator_type, Kp, Ki, Kd, time_end=20):
    time = np.linspace(0, time_end, 1000)
    setpoint = 1
    y = 0
    e_sum = 0
    e_prev = 0
    y_values = []

    for t in time:
        e = setpoint - y
        e_sum += e
        u = 0
        if regulator_type == "P":
            u = Kp * e
        elif regulator_type == "I":
            u = Ki * e_sum
        elif regulator_type == "D":
            u = Kd * (e - e_prev)
            e_prev = e
        elif regulator_type == "PI":
            u = Kp * e + Ki * e_sum
        elif regulator_type == "PD":
            u = Kp * e + Kd * (e - e_prev)
            e_prev = e
        elif regulator_type == "PID":
            u = Kp * e + Ki * e_sum + Kd * (e - e_prev)
            e_prev = e
        y += 0.6 * u
        y_values.append(y)

    plt.figure(figsize=(10, 6))
    plt.plot(time, y_values, label='Output')
    plt.axhline(setpoint, color='r', linestyle='--', label='Setpoint')
    plt.xlabel('Čas')
    plt.ylabel('Regulovaná veličina')
    plt.title(f'Simulace {regulator_type} regulátoru')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)

st.title("Simulace PID Regulátoru")

# Získání vstupů uživatele
regulator_type = st.radio("Vyberte typ regulátoru:", options=['P', 'I', 'D', 'PI', 'PD', 'PID'])
Kp = st.slider("Proporcionální zesílení Kp:", min_value=0.0, max_value=5.0, value=1.0, step=0.1)
Ki = st.slider("Integrační zesílení Ki:", min_value=0.0, max_value=2.0, value=0.2, step=0.1)
Kd = st.slider("Derivační zesílení Kd:", min_value=0.0, max_value=5.0, value=0.5, step=0.1)

# Tlačítko pro spuštění simulace
if st.button("Simulovat PID"):
    simulate_regulator(regulator_type, Kp, Ki, Kd)
