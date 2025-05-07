import streamlit as st
import datetime

# 1. Adiciona imagem de fundo via CSS (substitua o link pela imagem desejada)
# e personaliza fontes e fundos dos campos
st.markdown(
    """
    <style>
    /* Fundo da página com imagem */
    .stApp {
        background-image: url('https://img.odcdn.com.br/wp-content/uploads/2024/11/reacher--1024x576.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        opacity: 0.9;
    }
    /* Fundo dos inputs e textarea */
    .stTextInput input, .stNumberInput input, .stTextArea textarea, select, input, textarea {
        background: black !important;
        color: white !important;
    }
    /* Cor dos títulos e mensagens em vermelho */
    h1, h2, h3, h4, h5, h6, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6,
    label, .stMarkdown p, .stMarkdown, .stText {
        color: red !important;
    }
    /* Garante que o texto digitado nos campos fique branco */
    .stTextInput input, .stNumberInput input, .stTextArea textarea, input, textarea {
        color: white !important;
    }
    /* Mensagens específicas em vermelho */
    .custom-message-red {
        color: red !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 2. Container principal para os campos do formulário
with st.container():
    st.title('Bem-vindo(a)')
    st.write('Chega mais ao nosso portal de séries!')

    # 3. Campos do formulário (organizados em colunas, se quiser)
    col1, col2 = st.columns(2)
    with col1:
        nome_Serie = st.text_input('Nome da Série:')
        ano_Serie = st.number_input('Ano de lançamento:', step=1, value=0, format="%d")
        season_Serie = st.number_input('Temporadas:', step=1, value=0, format="%d")
    with col2:
        episodios_Serie = st.number_input('Quantidade de episódios:', step=1, value=0, format="%d")
        pais_Serie = st.text_input('País:')
        categoria_Serie = st.text_input('Categoria da Série:')

    st.write('Faça um resumo da série:')
    bio = st.text_area('', height=100)

    # 4. Botão para salvar os dados
    if st.button('Salvar'):
        dados_serie = {
            'Nome': nome_Serie,
            'Ano': ano_Serie,
            'Temporadas': season_Serie,
            'Episódios': episodios_Serie,
            'País': pais_Serie,
            'Categoria': categoria_Serie,
            'Resumo': bio
        }
        st.success('Dados da série salvos com sucesso!')
        st.write(dados_serie)  # Exibe os dados salvos (opcional)
