import streamlit as st
from joblib import load
import pandas as pd
from PIL import Image


def avaliador_credito(dados_novo):

    modelo = load("Modelo\modelo_pipe.joblib")

    df_dados_novo_cliente = pd.DataFrame(data=dados_novo,index=[0])
    previsao = modelo.predict(df_dados_novo_cliente)[0]


    return previsao


image = Image.open("logos/logo_canva_02.png")
st.image(image)

st.write('<p style="text-align: center;">Solid bank</strong> é um banco virtual criado com o intuito de facilitar a '
         'vida de milhões de brasileiros que sempre buscaram a facilidade'
         'e praticidade para resolver tudo na palma da mão</p><br><hr>',
         unsafe_allow_html=True)

st.write('<h1 <u style="text-align: center;color: grey">Avalie seu Crédito</u></h1>',
         unsafe_allow_html=True)

st.write('<p style="text-align: center;">Nós vamos precisar de algumas informações para começar a usar nossos serviços de crédito,'
         'mas prometemos que não levarão mais que <b> 5 min <b> pra preencher tudinho!!!.</p><br><hr>', unsafe_allow_html=True)

st.write('<h3 <u style="text-align: left;color: grey">Nós conte um pouco do seu trablaho</u></h3>',
         unsafe_allow_html=True)
st.write('<p style="text-align: left;">Primeiro gostariamos de saber um pouco mais sobre o seu trabalho, Mas pode ficar tranquilo'
         ' todas as informações são privadas.</p><br>', unsafe_allow_html=True)


my_expander_1 = st.expander('Primeiro seria MASSA te conhecer um pouco melhor.')
my_expander_2 = st.expander('Sabemos que trabalho é chato, mas nos fale um pouco sobre.')
my_expander_3 = st.expander('E como anda a familia??')



dados_novo_cliente = {}
opcao_feature = load("utilitarios\opcao_feature")

with my_expander_1:
    col1, col2 = st.columns(2)

    dados_novo_cliente['ESTADO_CIVIL'] = col2.selectbox(
        'E o coração? nos conte seu estado civil!!', opcao_feature['ESTADO_CIVIL'])

    dados_novo_cliente['ESCOLARIDADE'] = col2.selectbox(
        'O estudos estão em dia?? conte qual sua escolaridade', opcao_feature['ESCOLARIDADE'])

    dados_novo_cliente['TIPO_RESIDENCIA'] = col1.selectbox(
        'Qual seu tipo de residencia?', opcao_feature['TIPO_RESIDENCIA'])

    dados_novo_cliente['IDADE'] = col1.slider(
        'Nós conte sua idade.', help='será segredo, ok?!', min_value=0, max_value=100,
        step=1)

with my_expander_2:

    col1, col2 = st.columns(2)

    dados_novo_cliente['CAT_RENDA'] = col1.selectbox(
        'Nós informe sua categoria de renda', opcao_feature['CAT_RENDA'])

    dados_novo_cliente['OCUPACAO'] = col1.selectbox(
        'E você mexe com o que?', opcao_feature['OCUPACAO'])

    dados_novo_cliente['RENDIMENTO_ANUAL'] = col2.slider(
        'Qual seu salario mensal?', help='Fica tranquilo que isso é segredo nosso!!',
        min_value=0, max_value=50000, step=500) * 12

    dados_novo_cliente['ANOS_EMPREGO'] = col2.slider(
        'A quanto tempo você está empregado?', help='Caso não esteja trabalhando, basta responder 0',
        min_value=0, max_value=80,step=1)



with my_expander_3:
    col1, col2 = st.columns(2)

    dados_novo_cliente['IMOVEL_PROPRIO'] = 1 if col1.radio(
        "Você tem casa propria?", ('Sim!', 'Não')) == 'Sim!' else 0


    dados_novo_cliente['TEM_CARRO'] = 1 if col1.radio(
        "Você tem carro proprio?", ('Sim!', 'Não')) == 'Sim!' else 0

    dados_novo_cliente['N_FILHOS'] = col2.slider(
        'E as crianças, são quantas?', help='criança da trabalho mesmo mas é bom demais!!!',
        min_value=0, max_value=15, step=1)

    dados_novo_cliente['TAM_FAMILIA'] = col2.slider(
        'Quantas pessoas integram sua família?', min_value=0, max_value=30, step=1)


col1, col2, col3 = st.columns([1.3, 1, 1])
col4, col5, col6 = st.columns([1, 4, 1])


def negado():
    st.error('Crédito negado')
    st.write('<h1 <u style="text-align: center;color: red">own!!!</u></h1>',
             unsafe_allow_html=True)
def aprovado():
    col4, col5, col6 = st.columns([1, 4, 1])

    st.write('<h1 <u style="text-align: center;color: green">BOAAAAA!!!</u></h1>',
             unsafe_allow_html=True)

    st.write('<h3 <u style="text-align: center;color: green">Seu credito foi aprovado com a gente!!!</u></h3>',
             unsafe_allow_html=True)


    st.write('Seria muito massa se fosse verdade, ne? mas é apenas um projeto de simulação utilizando modelos de machine learning')
    col5.success('Crédito aprovado')


if col2.button('Avaliar crédito'):
       if avaliador_credito(dados_novo_cliente)==1:
           aprovado()
       else:
           negado()


