import streamlit as st
import pandas as pd
import random

st.set_page_config(
    page_title="Química de la Corrosión",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ Plataforma Gamificada de Corrosión y Protección Anticorrosiva")

menu = st.sidebar.selectbox(
    "Seleccione un módulo",
    [
        "Inicio",
        "Quiz",
        "Simulador de Corrosión",
        "Resultados"
    ]
)

if "score" not in st.session_state:
    st.session_state.score = 0

# -----------------------------
# INICIO
# -----------------------------

if menu == "Inicio":

    st.header("Bienvenido")

    st.markdown("""
    Esta plataforma está basada en investigaciones sobre:

    - Oxidación
    - Corrosión
    - Factores climáticos
    - Protección anticorrosiva
    - Mantenimiento preventivo y correctivo

    Desarrollada en Streamlit.
    """)

    st.image(
        "https://images.unsplash.com/photo-1489515217757-5fd1be406fef",
        use_container_width=True
    )

# -----------------------------
# QUIZ
# -----------------------------

elif menu == "Quiz":

    st.header("🎯 Quiz de Corrosión")

    preguntas = [

        {
            "pregunta":"¿Qué es la oxidación?",
            "opciones":[
                "Una reacción entre un material y oxígeno",
                "Una limpieza química",
                "Un tipo de pintura",
                "Una aleación"
            ],
            "correcta":"Una reacción entre un material y oxígeno"
        },

        {
            "pregunta":"¿Cuál factor favorece la corrosión?",
            "opciones":[
                "Humedad",
                "Vacío",
                "Plástico",
                "Vidrio"
            ],
            "correcta":"Humedad"
        },

        {
            "pregunta":"¿Qué mantenimiento busca evitar fallas?",
            "opciones":[
                "Preventivo",
                "Correctivo",
                "Emergente",
                "Operacional"
            ],
            "correcta":"Preventivo"
        },

        {
            "pregunta":"¿Qué contaminante acelera la corrosión marina?",
            "opciones":[
                "Cloruros",
                "Oxígeno puro",
                "Nitrógeno",
                "Helio"
            ],
            "correcta":"Cloruros"
        }
    ]

    pregunta = random.choice(preguntas)

    st.subheader(pregunta["pregunta"])

    respuesta = st.radio(
        "Seleccione:",
        pregunta["opciones"]
    )

    if st.button("Verificar"):

        if respuesta == pregunta["correcta"]:
            st.success("✅ Correcto")
            st.session_state.score += 10

        else:
            st.error(
                f"❌ Incorrecto. Respuesta correcta: {pregunta['correcta']}"
            )

# -----------------------------
# SIMULADOR
# -----------------------------

elif menu == "Simulador de Corrosión":

    st.header("🧪 Simulador de Corrosión")

    humedad = st.slider(
        "Humedad (%)",
        0,
        100,
        70
    )

    temperatura = st.slider(
        "Temperatura (°C)",
        0,
        50,
        25
    )

    salinidad = st.slider(
        "Salinidad",
        0,
        100,
        40
    )

    mantenimiento = st.selectbox(
        "Mantenimiento aplicado",
        [
            "Ninguno",
            "Preventivo",
            "Correctivo",
            "Protección Anticorrosiva"
        ]
    )

    indice = (
        humedad * 0.4 +
        temperatura * 0.2 +
        salinidad * 0.4
    )

    if mantenimiento == "Preventivo":
        indice *= 0.75

    elif mantenimiento == "Correctivo":
        indice *= 0.60

    elif mantenimiento == "Protección Anticorrosiva":
        indice *= 0.40

    st.subheader("Resultado")

    if indice < 30:
        st.success("🟢 Riesgo Bajo")

    elif indice < 60:
        st.warning("🟡 Riesgo Medio")

    else:
        st.error("🔴 Riesgo Alto")

    st.metric(
        "Índice de Corrosión",
        round(indice,2)
    )

# -----------------------------
# RESULTADOS
# -----------------------------

elif menu == "Resultados":

    st.header("📊 Dashboard")

    st.metric(
        "Puntaje acumulado",
        st.session_state.score
    )

    datos = pd.DataFrame(
        {
            "Categoría":[
                "Oxidación",
                "Corrosión",
                "Protección",
                "Mantenimiento"
            ],
            "Avance":[
                80,
                70,
                60,
                90
            ]
        }
    )

    st.bar_chart(
        datos.set_index("Categoría")
    )
