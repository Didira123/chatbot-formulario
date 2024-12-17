# -*- coding: utf-8 -*-

import streamlit as st
import json

st.set_page_config(page_title="ChatBot - Formulário", page_icon="🎯")


# Functions
def load_questions():
    with open("questions.json", encoding="utf-8") as qs:
        return json.load(qs)

def update_pos():
    st.session_state["pos"]+=1

def update_pos_and_report():
    user_answer = st.session_state["user_answer"]
    st.session_state["relatorio"]["questions_and_answers"][pos]["user_answer"] = user_answer

    correct_answer = st.session_state["relatorio"]["questions_and_answers"][pos]["correct_answer"]
    if user_answer.lower() == correct_answer.lower():
        st.session_state["relatorio"]["score"]+=1
    st.session_state["pos"]+=1

# State variables initialization
if "relatorio" not in st.session_state:
    questions = load_questions()
    st.session_state["relatorio"] = {
        "questions_and_answers": questions.copy(),
        "score": 0
    }

if "pos" not in st.session_state:
    st.session_state["pos"] = -1

pos = st.session_state["pos"]
questions = st.session_state["relatorio"]["questions_and_answers"]

# Form Control
with st.form("pergunta_atual"):
    if questions and pos < len(questions):    
        bot = st.chat_message("assistant")
        if pos == -1:
            bot.text(f"""
                     Bem-vindo ao nosso quiz interativo! 🚀
Vou te guiar por uma série de {len(questions)} perguntas. Responda com atenção, pois ao final você verá sua pontuação e poderá fazer o download do seu desempenho.
Pronto? Vamos lá! Clique em "Começar" para iniciar! 🎯
             """)
            bot.form_submit_button("Começar", on_click=update_pos, icon=":material/arrow_forward:")
        else:
            bot.radio(f"\u200B{pos+1}) {questions[pos]['question']}", questions[pos]["options"], key="user_answer")

            bot.form_submit_button("Próxima", on_click=update_pos_and_report, icon=":material/forward:")

if not pos < len(questions):
    botFinal = st.chat_message("assistant")
    relatorio = st.session_state["relatorio"]
    botFinal.text(f"""
                Parabéns, você completou o quiz! 🎉
Obrigado por participar do nosso quiz interativo! Você respondeu a todas as perguntas e sua pontuação final foi calculada com base nas suas respostas. 👏
Se quiser, você pode baixar seu desempenho clicando no link abaixo para salvar um arquivo com suas respostas e a pontuação obtida.
Esperamos que tenha se divertido! Fique à vontade para tentar novamente ou compartilhar com seus amigos. 🚀
Sua pontuação final: {relatorio["score"]} / {len(questions)}""")
    botFinal.download_button("Baixar Resultado", json.dumps(relatorio, ensure_ascii=False, indent=4), file_name="resultados.json", mime="application/json", icon=":material/download:")

