# -*- coding: utf-8 -*-

# st.chat_input()
# st.chat_message()
# st.selectbox()
# st.write_stream()

#####################################################
# import streamlit as st
# import json

# Função para carregar perguntas
# def carregar_perguntas():
#     with open('perguntas.json', encoding='utf-8') as f:
#         return json.load(f)

# # Função para calcular pontuação
# def calcular_pontuacao(respostas, perguntas):
#     pontos = 0
#     for resposta, pergunta in zip(respostas, perguntas['perguntas']):
#         if resposta.lower() == pergunta['resposta_correta'].lower():
#             pontos += 1
#     return pontos

# # Função principal do app
# def app():
#     st.title("Chatbot de Questionário")

#     perguntas = carregar_perguntas()
#     respostas = []

#     for pergunta in perguntas['perguntas']:
#         st.chat_message("assistant").markdown(pergunta['pergunta'])
#         resposta = st.radio("Escolha uma resposta:", pergunta['opcoes'])
#         respostas.append(resposta)

#     if st.button("Submeter Respostas"):
#         pontos = calcular_pontuacao(respostas, perguntas)
#         st.chat_message("assistant").markdown(f"Você obteve {pontos} pontos!")
#         resultado = {
#             "respostas": [{"id": p['id'], "resposta_usuario": r} for p, r in zip(perguntas['perguntas'], respostas)],
#             "pontuacao": pontos
#         }
#         st.download_button("Baixar Resultado", json.dumps(resultado), file_name="resultados.json", mime="application/json")

# if __name__ == "__main__":
#     app()
#####################################################

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

# json.dumps

###########################

# import streamlit as st

# # st.write("Hello world")

# def form_callback():
#     st.write(st.session_state.my_slider)
#     st.write(st.session_state.my_checkbox)

# with st.form(key='my_form'):
#     slider_input = st.slider('My slider', 0, 10, 5, key='my_slider')
#     checkbox_input = st.checkbox('Yes or No', key='my_checkbox')
#     submit_button = st.form_submit_button(label='Submit', on_click=form_callback)


# import streamlit as st

# st.session_state
# x = st.slider('x', key="x")  # 👈 this is a widget
# st.write(x, 'squared is', x * x)

# import streamlit as st

# # Add a selectbox to the sidebar:
# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone')
# )

# # Add a slider to the sidebar:
# add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )



# st.columns(2)




# import streamlit as st
# import time

# 'Starting a long computation...'

# # Add a placeholder
# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#   # Update the progress bar with each iteration.
#   latest_iteration.text(f'Iteration {i+1}')
#   bar.progress(i + 1)
#   time.sleep(0.1)

# '...and now we\'re done!'




# import streamlit as st
# import pandas as pd
# import numpy as np
# if "df" not in st.session_state:
#     st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

# st.header("Choose a datapoint color")
# color = st.color_picker("Color", "#FF0000")
# st.divider()
# st.scatter_chart(st.session_state.df, x="x", y="y", color=color)



# import streamlit as st
# import pandas as pd
# import numpy as np

# st.title('Uber pickups in NYC')

# DATE_COLUMN = 'date/time'
# DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
#             'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# @st.cache_data
# def load_data(nrows):
#     data = pd.read_csv(DATA_URL, nrows=nrows)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#     return data

# data_load_state = st.text('Loading data...')
# data = load_data(10000)
# data_load_state.text("Done! (using st.cache_data)")

# if st.checkbox('Show raw data'):
#     st.subheader('Raw data')
#     st.write(data)

# st.subheader('Number of pickups by hour')
# hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
# st.bar_chart(hist_values)

# # Some number in the range 0-23
# hour_to_filter = st.slider('hour', 0, 23, 17)
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

# st.subheader('Map of all pickups at %s:00' % hour_to_filter)
# st.map(filtered_data)




# import streamlit as st
# import json

# def carregar_perguntas():
#     with open('perguntas.json') as f:
#         return json.load(f)

# ai = st.chat_message('ai')
# ai.text("Olá, seja bem-vindo! Sou o chatbot \"Maicon\".")

# question = 0

# prompt = st.chat_input("Digite sua resposta")
# if prompt:
#     question+=1
