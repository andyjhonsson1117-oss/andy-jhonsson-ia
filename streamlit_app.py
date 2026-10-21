from google import genai
import streamlit as st

# Configuración de página de ANDY JHONSSON
st.set_page_config(
    page_title="ANDY JHONSSON IA", page_icon="💈", layout="centered"
    )

    st.title("💈 ANDY JHONSSON IA")
    st.caption("Asistente Virtual Avanzado de Edwin")

    # Reemplaza con tu clave ANDY API Key 1117
    API_KEY = "PEGA_AQUI_TU_API_KEY"

    client = genai.Client(api_key=API_KEY)

    # Memoria de la sesión actual
    if "messages" not in st.session_state:
        st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                    st.markdown(message["content"])

                    if prompt := st.chat_input("Escribe tu mensaje a ANDY JHONSSON..."):
                        st.chat_message("user").markdown(prompt)
                            st.session_state.messages.append({"role": "user", "content": prompt})

                                try:
                                        response = client.models.generate_content(
                                                    model="gemini-2.5-flash",
                                                                config={
                                                                                "system_instruction": "Tu nombre es ANDY JHONSSON. Eres una Inteligencia Artificial avanzada creada por Edwin. Tienes amplios conocimientos y respondes de forma directa, rápida y cordial."
                                                                                            },
                                                                                                        contents=prompt,
                                                                                                                )

                                                                                                                        with st.chat_message("assistant"):
                                                                                                                                    st.markdown(response.text)
                                                                                                                                            st.session_state.messages.append(
                                                                                                                                                        {"role": "assistant", "content": response.text}
                                                                                                                                                                )
                                                                                                                                                                    except Exception as e:
                                                                                                                                                                            st.error(
                                                                                                                                                                                        f"Error al conectar con la IA. Revisa tu API Key. Detalle: {e}"
                                                                                                                                                                                                )
                                                                                                                                    