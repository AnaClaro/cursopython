import streamlit as st
import json
import os
import datetime

# Nome do arquivo Json
ARQUIVO_DADOS = "series.json"

def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def salvar_dados(dados):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def criar_serie(nome_Serie, ano_Serie, season_Serie, episodios_Serie, pais_Serie, categoria_Serie):
    return {
        "nome_Serie": nome_Serie,
        "ano_Serie": ano_Serie,
        "season_Serie": season_Serie,
        "episodios_Serie": episodios_Serie,
        "pais_serie": pais_Serie,
        "categoria_Serie": categoria_Serie
    }
    

def cadastrar_serie(): # 2. Container principal para os campos do formulário
#    with st.container():
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

def listar_series():
    pass

def editar_serie():
    pass

def excluir_serie():
    pass

# Menu lateral
st.sidebar.title("Menu")
opcao = st.sidebar.radio("Selecione uma opção:", ("Cadastrar Série", "Listar Séries", "Editar Série", "Excluir Série"))

# Navegaçãoe entre páginas

if opcao == "Cadastrar Série":
    cadastrar_serie()
elif opcao == "Listar Série":
    listar_series()
elif opcao == "Editar Série":
    editar_serie()
elif opcao == "Excluir Série":
    excluir_serie()

# Rodapé
st.sidebar.markdown("---")
st.sidebar.markdown("Desenvolvido por Ana Claro")
st.sidebar.markdown(f"Total de séries: ")
