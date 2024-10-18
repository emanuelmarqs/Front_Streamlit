import numpy
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.title('meu primeiro dashboard')
st.header('esse é um header')

if st.button('clique aqui'):
    st.text('Voce apertou o botao')

opcao = st.radio(
    'Escolha a opção:',
    ('Flamengo', 'Corinthias', 'Palmeiras')
)

if opcao == 'Flamengo':
    st.info('Voce é um urubu')
elif opcao == 'Corinthias':
    st.warning ('Voce é um campeao')
else: 
    st.error('voce é um perdedor')


caminho = "C:\\Users\\emanu\\OneDrive\\Área de Trabalho\\IBMEC\\2° Semestre\\Ciência de Dados I\\Projetos\\FrontEnd\\Aula1\\data\\ibov.csv"
#df = pd.read_csv(caminho + "\\ibov.csv")
df = pd.read_csv(caminho)
st.dataframe(df)

fig, ax = plt.subplots()

fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100, 30, 55]
bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')

st.pyplot(fig)