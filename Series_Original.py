Perplexity, criei um código em Phyton formato web e gostaria de melhorar o layout. Gostaria de adicionar um botão para salvar os dados inseridos no formulário e também adicionar uma imagem de fundo utilizando um link disponível na web.

O código que criei é este:

#6 campos para cadastrar: Nome da Série, Ano de lançamento, Temporada, Episódios, País, Tema

import streamlit as st
import datetime

st.title('Bem-vindo(a)')
st.write('Chega mais ao nosso portal de séries!')

data_minima = datetime.date(1900,1,1)
data_maxima = datetime.date(2100,12,31)

nome_Serie = st.text_input('Nome da Série:')
ano_Serie = st.number_input('Ano de lançamento:',step=1, value=0, format="% d")
season_Serie = st.number_input('Temporadas:',step=1, value=0, format="% d")
episodios_Serie = st.number_input('Quantidade de episódios:',step=1, value=0, format="% d")
pais_Serie = st.text_input('País:')
categoria_Serie = st.text_input('Categoria da Série:')

st.write('Faça um resumo da série:')
bio=st.text_area('')