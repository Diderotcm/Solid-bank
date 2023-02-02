import streamlit as st
from joblib import load
import pandas as pd
from PIL import Image
from streamlit_option_menu import option_menu
import webbrowser
import streamlit_nested_layout
import plotly.express as px

st.set_page_config(layout="wide",initial_sidebar_state='expanded')

select = option_menu(
        menu_title=None,
        options=['Home', 'Dashboard', 'Projeto', 'Contato'],
        icons=['house', 'bar-chart', 'book', 'envelope'],
        menu_icon='cast',
        default_index=0,
        orientation='horizontal'
    )

@st.cache
def load_data():
    data = pd.read_csv('https://raw.githubusercontent.com/Diderotcm/Solid-bank/main/dados/dados_preparados.csv')
    return data

if select == 'Home':
    cl1, cl2, cl3 = st.columns([3,1,3])
    with cl1:
        def avaliador_credito(dados_novo):

            modelo = load("Modelo/modelo_pipe.joblib")

            df_dados_novo_cliente = pd.DataFrame(data=dados_novo, index=[0])
            previsao = modelo.predict(df_dados_novo_cliente)[0]

            return previsao

        image = Image.open("logos/logo_solid-bank.png")
        st.image(image,width=500)

        st.write('<p style="text-align: justify;">Solid bank</strong> é um banco virtual criado com o intuito de facilitar a'
                 'vida de milhões de brasileiros que sempre buscaram a facilidade'
                 ' e praticidade para resolver tudo na palma da mão</p><br><hr>',
                 unsafe_allow_html=True)

        st.write('<h1 <u style="text-align: center;color: #166D8A">Avalie seu Crédito</u></h1>',
                 unsafe_allow_html=True)

        st.write('<p style="text-align: justify;">Nós vamos precisar de algumas informações para começar a usar'
                 ' nossos serviços de crédito,'
                 ' mas prometemos que não levarão mais que <b> 5 min <b> pra preencher tudinho!!!.</p><br><hr>',
                 unsafe_allow_html=True)



    with cl3:
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")

        st.write('<h2 <u style="text-align: center;color: #166D8A">É rapidinho!!</u></h2>',
                 unsafe_allow_html=True)
        st.write('<p style="text-align: left;">Basta preencher o fomulario abaixo e'
                 ' logo em seguida clicar em <span style="color:#166D8A"><b> Avaliar credito.</b></span>'
                 ' todas as informações são privadas.</p><br>', unsafe_allow_html=True)
        my_expander_1 = st.expander('Primeiro seria MASSA te conhecer um pouco melhor.')
        my_expander_2 = st.expander('Nós conte sobre o trabalho!')
        my_expander_3 = st.expander('E como anda a familia??')

        dados_novo_cliente = {}
        opcao_feature = load("utilitarios/opcao_feature")

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
                min_value=0, max_value=45,step=1)

        with my_expander_3:
            col1, col2 = st.columns(2)

            dados_novo_cliente['IMOVEL_PROPRIO'] = 1 if col1.radio(
                "Você tem casa propria?", ('Sim!', 'Não')) == 'Sim!' else 0

            dados_novo_cliente['TEM_CARRO'] = 1 if col1.radio(
                'Você tem carro proprio?', ('Sim!', 'Não')) == 'Sim!' else 0

            dados_novo_cliente['N_FILHOS'] = col2.slider(
                'E as crianças, são quantas?', help='criança da trabalho mesmo mas é bom demais!!!',
                min_value=0, max_value=20, step=1)

            dados_novo_cliente['TAM_FAMILIA'] = col2.slider(
                'Quantas pessoas integram sua família?', min_value=0, max_value=20, step=1)

        col1, col2, col3 = st.columns([1.4, 1, 1])


        def negado():

            st.write('<h1 <u style="text-align: center;color: red">own!! &#128549;</u></h1>',
                     unsafe_allow_html=True)

            st.write('<h3 <u style="text-align: center;color: red">Infelizmente nao podemos disponibilizar crédito'
                     ' no momento</u></h3>',
                     unsafe_allow_html=True)

            st.write('<h3 <u style="text-align: center;color: black">Não fique triste por isso,'
                     ' é apenas um projeto de machine learning'
                     ' que utiliza dados do kaggel.</u></h3>',
                     unsafe_allow_html=True)

            col1, col2, col3 = st.columns(3)
            col1.image("logos/kaggle_resize.png")

            col1.write(
                '<p style="text-align: center;"><b>Quer saber de onde os dados foram tirados?</b><br> '
                ' Acesse os dados: <a style="color: lightblue" target="_blank" '
                'href ="https://www.kaggle.com/datasets/rikdifos/credit-card-approval-prediction">Kaggle</a><p>',
                unsafe_allow_html=True)

            col2.image("logos/github_resize.png")

            col2.write(
                '<p style="text-align: center;"><b>Quer saber como esse projeto foi feito?</b><br>'
                ' Acesse no Github: <a style="color: lightblue" target="_blank"'
                ' href ="https://github.com/Diderotcm/Solid-bank">Solid-Bank</a><p>',
                unsafe_allow_html=True)

            col3.image("logos/LinkedIn_resize.png")

            col3.write(
                '<p style="text-align: center;"><b>Da uma olhadinha no meu linkedin!!</b><br>'
                ' Acesse o Linkedin: <a style="color: lightblue" target="_blank"'
                ' href ="https://www.linkedin.com/in/fernando-diderot">Fernando Diderot</a><p>',
                unsafe_allow_html=True)


    def aprovado():
            st.balloons()
            st.write('<h1 <u style="text-align: center;color: green">BOAAAAA!!! &#128526; </u></h1>',
                     unsafe_allow_html=True)

            st.write('<h3 <u style="text-align: center;color: green">Seu credito foi aprovado com a gente!!!</u></h3>',
                     unsafe_allow_html=True)

            st.write('<h3 <u style="text-align: center;color: black">Seria muito divertido de fosse real, ne? mas isso'
                     ' é apenas um projeto de machine learning'
                     ' que utiliza dados do kaggel.</u></h3>',
                     unsafe_allow_html=True)

            col1, col2, col3 = st.columns(3)
            col1.image("logos/kaggle_resize.png")

            col1.write(
                '<p style="text-align: center;"><b>Quer saber de onde os dados foram tirados?</b><br> '
                ' Acesse os dados: <a style="color: lightblue" target="_blank" '
                'href ="https://www.kaggle.com/datasets/rikdifos/credit-card-approval-prediction">Kaggle</a><p>',
                unsafe_allow_html=True)

            col2.image("logos/github_resize.png")

            col2.write(
                '<p style="text-align: center;"><b>Quer saber como esse projeto foi feito?</b><br>'
                ' Acesse no Github: <a style="color: lightblue" target="_blank"'
                ' href ="https://github.com/Diderotcm/Solid-bank">Solid-Bank</a><p>',
                unsafe_allow_html=True)

            col3.image("logos/LinkedIn_resize.png")

            col3.write(
                '<p style="text-align: center;"><b>Da uma olhadinha no meu linkedin!!</b><br>'
                ' Acesse o Linkedin: <a style="color: lightblue" target="_blank"'
                ' href ="https://www.linkedin.com/in/fernando-diderot">Fernando Diderot</a><p>',
                unsafe_allow_html=True)

    if col2.button('Avaliar crédito'):
               if avaliador_credito(dados_novo_cliente)==1:
                   aprovado()
               else:
                   negado()

if select == 'Projeto':
    st.write('<h4 <u style="text-align: center;color: black">Quer saber de cada detalhe desse projeto?</u></h4>',
                 unsafe_allow_html=True)
    st.write('')

    col1, col2, col3 = st.columns([1,2,2])
    col2.image("logos/emoji_livro.png", width=100)
    col2.write(
        '<p style="text-align: left;"><b>Notebook de preparação dos dados:</b><br> '
        '  <a style="color: lightblue" target="_blank" '
        'href ="https://github.com/Diderotcm/Solid-bank/blob/main/Notebooks/Solid_Bank_prepara%C3%A7%C3%A3o_dados.ipynb">Notebook</a><p>',
        unsafe_allow_html=True)

    col3.image("logos/emoji_livro.png", width=100)
    col3.write(
        '<p style="text-align: left;"><b>Notebook de machine learning:</b><br> '
        '  <a style="color: lightblue" target="_blank" '
        'href ="https://github.com/Diderotcm/Solid-bank/blob/main/Notebooks/Solid-Bank-Machine_Leaning.ipynb">Notebook</a><p>',
        unsafe_allow_html=True)


    col2.image("logos/kaggle_resize.png", width=100)
    col2.write('')

    col2.write(
        '<p style="text-align: left;"><b>Quer saber de onde os dados foram tirados?</b><br> '
        ' Acesse os dados: <a style="color: lightblue" target="_blank" '
        'href ="https://www.kaggle.com/datasets/rikdifos/credit-card-approval-prediction">Kaggle</a><p>',
        unsafe_allow_html=True)

    col3.image("logos/github_resize.png", width=115)

    col3.write(
        '<p style="text-align: left;"><b>Quer saber como esse projeto foi feito?</b><br>'
        ' Acesse no Github: <a style="color: lightblue" target="_blank"'
        ' href ="https://github.com/Diderotcm/Solid-bank">Solid-Bank</a><p>',
        unsafe_allow_html=True)

if select == 'Contato':

    col10, col11 = st.columns([0.7, 2])
    col10.image('logos/foto_perfil.png',width=320)
    col11.write('<h1 <u style="text-align: left;">Fernando Diderot Carneiro Marinho </u></h1>',
             unsafe_allow_html=True)
    col11.write('<p align="justify">Apaixonado por dados e em criar soluções inovadoras por meio deles. Acredito que a junção'
                ' de ambos os pilares são capazes de transformar o mundo a nossa volta. Engenheiro Civil formado pelo'
                ' Instituto Politecnico de Bragançade de Portugal e pela Universidade de Fortaleza. Pós graduação em'
                ' Data Science e Analytics pela Univerdade de São Paulo (USP). No meu cotidiano sempre tento aprender'
                ' coisas novas e solucionar problemas de forma prática, rápidas e transformadoras, tentando desfrutar ao'
                ' máximo do aprendizado adquirido em cada desafio.</p>',
                unsafe_allow_html=True)
    col11.write(
        '<p style="text-align: left;"><b></b><br>'
        'Email: <a style="color: blue" target="_blank"'
        ' ">diderotmarinho@gmail.com</a><p>',
        unsafe_allow_html=True)
    col11.write(
        '<p style="text-align: left;"><b></b><br>'
        'Linkedin: <a style="color: blue" target="_blank"'
        ' href ="https://www.linkedin.com/in/fernando-diderot">Fernando Diderot</a><p>',
        unsafe_allow_html=True)

if select == 'Dashboard':
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    st.sidebar.header(' ')

    st.sidebar.subheader('Histogram')
    hist_value = st.sidebar.selectbox('Por', ('IDADE', 'TIPO_RESIDENCIA', 'OCUPACAO'))

    st.sidebar.subheader('Donut')
    donut_value = st.sidebar.selectbox('Por', ('IMOVEL_PROPRIO', 'TEM_CARRO', 'GENERO'))
    st.sidebar.write(
        '<p style="text-align: left;"><b></b><br>'
        'criado de ❤️ por <a style="color: blue" target="_blank"'
        ' href ="https://www.linkedin.com/in/fernando-diderot">Fernando Diderot</a><p>',
        unsafe_allow_html=True)

    # Row A
    dados = load_data()
    st.markdown('### Clientes')
    col1, col2, col3 = st.columns(3)
    col1.metric('Clientes',
                value=dados['ID'].nunique())
    col2.metric('Bons pagadores',
                value=dados['BOM'].value_counts()[1])
    col3.metric('% Bons pagadores',
                value=round(dados['BOM'].value_counts(normalize=True)[1] * 100))

    # Row B
    st.markdown('### Distribuição')
    fig_2 = px.histogram(dados,
                         x=hist_value,
                         width=1060,
                         height=350)
    st.write(fig_2)

    # Row C
    c1, c2 = st.columns((7, 3))
    v = dados['CAT_RENDA'].value_counts()
    with c1:
        st.markdown('### Clientes por categoria de renda')
        df_1 = dados.groupby(by='CAT_RENDA')['ID'].count().reset_index()
        df_1.rename(columns={'ID': 'Count'}, inplace=True)
        df_1.sort_values('Count', inplace=True, ascending=True)

        fig_1 = px.bar(df_1,
                       x='Count',
                       y='CAT_RENDA',
                       labels={'CAT_RENDA': ' ', 'Count': ' '},
                       width=720,
                       height=350)
        st.write(fig_1)

    with c2:
        st.write('### Clientes por categoria')
        df_2 = dados.groupby(donut_value)['ID'].count().reset_index()
        df_2.rename(columns={'ID': 'Contagem'}, inplace=True)
        df_2.replace([0, 1], ['Não tem', 'Tem'], inplace=True)
        fig_2 = px.pie(df_2,
                       values='Contagem',
                       names=donut_value,
                       hole=.5,
                       width=300,
                       height=350,
                       title=donut_value)
        st.write(fig_2)