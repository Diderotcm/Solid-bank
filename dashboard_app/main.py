import streamlit as st
import pandas as pd
import plotly.express as px
import plost
import seaborn as sns
import matplotlib.pyplot as plt


st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.sidebar.header(' ')

st.sidebar.subheader('Histogram')
hist_value = st.sidebar.selectbox('Por', ('IDADE', 'TIPO_RESIDENCIA', 'OCUPACAO'))

st.sidebar.markdown('''
---
Criado de ❤️ por [Fernando Diderot](www.linkedin.com/in/fernando-diderot).
''')

# Row A
dados = pd.read_csv('https://raw.githubusercontent.com/Diderotcm/Solid-bank/main/dados/dados_preparados.csv')
st.markdown('### Metrics')
col1, col2, col3 = st.columns(3)
col1.metric('Clientes', value=dados['ID'].nunique())
col2.metric('Bons pagadores',value=dados['BOM'].value_counts()[1])
col3.metric('% Bons pagadores', value=round(dados['BOM'].value_counts(normalize=True)[1]*100))

# Row B
st.markdown('### Distribuição')
fig_2 = px.histogram(dados, x=hist_value, color="BOM", width=1000)
st.write(fig_2)

# Row C
c1, c2 = st.columns((7, 3))
v = dados['CAT_RENDA'].value_counts()
with c1:
    st.markdown('### Clientes por categoria de renda')
    df_1 = dados.groupby(by='CAT_RENDA')['ID'].count().reset_index()
    df_1.rename(columns={'ID': 'Count'}, inplace=True)
    df_1.sort_values('Count',inplace=True,ascending=True)

    fig_1 = px.bar(df_1,x='Count',y='CAT_RENDA',labels={'CAT_RENDA': ' ', 'Count': ' '}, height=350)
    st.write(fig_1)

with c2:
     df_2 = dados.groupby('ESCOLARIDADE')['BOM'].count().reset_index()
     df_2.rename(columns={'BOM': 'Contagem'}, inplace=True)
     fig_2 = px.pie(df_2, values='Contagem', names='ESCOLARIDADE', hole=.5, width=380)
     st.write(fig_2)


# Row C
