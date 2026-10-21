import streamlit as st
import google.generativeai as genai

# Configuración de la página
st.set_page_config(page_title="ANDY JHONSSON IA", page_icon="💈", layout="centered")

# Título y presentación
st.title("💈 ANDY JHONSSON IA")
st.write("¡Hola! Soy ANDY JHONSSON, tu asistente virtual. ¿En qué te puedo ayudar hoy?")

# Inicializar las claves de API en el estado de la sesión
if "api_key" not in st.session_state:
    st.session_state.api_key = ""

    # Entrada para la API Key de Gemini
    api_key_input = st.text_input("Ingresa tu Gemini API Key:", type="password", value=st.session_state.api_key)

    if api_key_input:
        st.session_state.api_key = api_key_input
            genai.configure(api_key=st.session_state.api_key)

            # Historial de mensajes
            if "messages" not in st.session_state:
                st.session_state.messages = []

                # Mostrar el historial de conversación
                for message in st.session_state.messages:
                    with st.chat_message(message["role"]):
                            st.markdown(message["content"])

                            # Entrada de texto del usuario
                            if prompt := st.chat_input("Escribe tu mensaje aquí..."):
                                if not st.session_state.api_key:
                                        st.warning("Por favor, ingresa tu Gemini API Key para continuar.")
                                            else:
                                                    # Guardar mensaje del usuario
                                                            st.session_state.messages.append({"role": "user", "content": prompt})
                                                                    with st.chat_message("user"):
                                                                                st.markdown(prompt)

                                                                                        # Generar respuesta de la IA
                                                                                                try:
                                                                                                            model = genai.GenerativeModel("gemini-1.5-flash")
                                                                                                                        response = model.generate_content(prompt)
                                                                                                                                    
                                                                                                                                                with st.chat_message("assistant"):
                                                                                                                                                                st.markdown(response.text)
                                                                                                                                                                            
                                                                                                                                                                                        st.session_state.messages.append({"role": "assistant", "content": response.text})
                                                                                                                                                                                                except Exception as e:
                                                                                                                                                                                                            st.error(f"Error al generar la respuesta: {e}")
                                                                                                                                                                