import streamlit as st
import pandas as pd
import plotly.express as px


car_data = pd.read_csv('vehicles.csv')
hist_button = st.button('Criar histrograma')

st.header('Análise de carros')

if hist_button:# se o botão for clicado
    #escrever uma mensagem
    st.write('Criando um histrograma para o conjunto de dados de anúncios de vendas de caros')

    fig = px.histogram(car_data, x="odometer")
    #criar um histrograma

    st.plotly_chart(fig, use_container_width=True)
    #exibir um gráfico plotly interativo




