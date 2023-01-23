

<p align= "center">
<img src="https://raw.githubusercontent.com/Diderotcm/Solid-bank/main/logos/logo_canva_02.png" min-width="50px" max-width="200px" width="500px" > 
</p>

<p align= "center">
Acesse o App: <a href="https://diderotcm-solid-bank-app-credito-nqxl87.streamlit.app/">Solid Bank</a>
</p>

# SOLID BANK

é um projeto de um banco virtual criado com o intuito de
disponibilizar crédito utilizando um modelo de machine learning
que prevê se um novo cliente é um bom pagador ou não.
## Descrição do projeto

O projeto foi ralizado em 3 etapas:

- __Limpeza e tradução dos dados__
foi realizado primeiro a tradução de todo o bnco de dados e em seguida realizada a Limpeza
tratando valores ausente, removendo ouliers e etc.
- __Crianção do modelo.__
criação de diversos modelos e aplicando o modelo que melhor se enquadra no bando de dados
alem de utilização de tecnicas de otimização de hiper parametros.

- __Criação do App__
App criado com a API streamlit, uma API especifica para deploy e aplicação de modelos
de machine learning.

## Base de dados.
Todos os dados foram retirados da platafomado do Kaggle
- __application_record__ = Dataset referente a informações de cada cliente com 17 features.
- __credit_record__ = Dataset referente ao status de bom ou mal pagador.
- __dados_preparados__ = Dataset criado a partir dos dois anteriores com o objetivo de ser aplicado a uma modelo de machine learning.
