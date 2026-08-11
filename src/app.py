import streamlit as st

st.set_page_config(page_title="IaFin - Assistente Financeiro", page_icon="💰")

st.title("💰 IaFin - Seu Professor de Finanças")
st.markdown("Bem-vindo! Sou o **IaFin**, um agente especializado em ajudar você a dar os primeiros passos no mundo dos investimentos de forma segura.")

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant", 
        "content": "Olá! Vamos dar o primeiro passo para organizar suas finanças hoje? Você já sabe qual é o seu perfil de investidor?"
    })

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Digite sua dúvida aqui..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Lógica simples de mock do LLM
    with st.chat_message("assistant"):
        resposta = "Entendi! Como este é um protótipo de front-end, ainda estou conectando minha base de dados. Mas lembre-se: o primeiro passo é focar na Reserva de Emergência em ativos como Tesouro Selic!"
        st.markdown(resposta)
        st.session_state.messages.append({"role": "assistant", "content": resposta})
