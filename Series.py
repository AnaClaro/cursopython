import streamlit as st
import json
import os
from datetime import datetime

# Nome do arquivo JSON
ARQUIVO_DADOS = "series.json"

# --- Funções de Estilo ---
def set_page_style():
    st.markdown(
        """
        <style>
        /* Definir fundo preto para a página principal */
        .stApp {
            background-color: black;
            color: white; /* Texto padrão da aplicação em branco */
        }

        /* Cor do texto para st.write (onde as informações são exibidas) */
        div.stMarkdown p {
            color: red; /* Texto em vermelho para a maioria das exibições de conteúdo */
        }
        /* Ajustar a cor dos títulos/subtítulos para se destacarem */
        h1, h2, h3, h4, h5, h6 {
            color: white;
        }

        /* Ajustar a cor do texto dentro dos inputs para ser visível no fundo escuro */
        .stTextInput > div > div > input,
        .stNumberInput > div > input,
        .stDateInput > div > input {
            color: white; /* Cor do texto digitado no input */
            background-color: #333333; /* Fundo do campo de input um pouco mais claro que o fundo geral */
        }
        /* Cor do label do input */
        .stTextInput > label,
        .stNumberInput > label,
        .stDateInput > label,
        .stSelectbox > label,
        .stTextArea > label {
            color: white; /* Cor do label do campo de entrada */
        }
        /* Cor das opções do selectbox */
        div[data-baseweb="select"] > div:first-child {
            background-color: #333333; /* Fundo do selectbox */
            color: white; /* Cor do texto selecionado no selectbox */
        }
        /* Cor da lista de opções do selectbox */
        div[role="listbox"] {
            background-color: #333333; /* Fundo da lista de opções */
            color: white;
        }
        /* Cor dos itens da lista de opções do selectbox */
        div[role="option"] {
            color: white;
        }

        /* Cor padrão para TODOS os botões */
        .stButton > button {
            background-color: #8B0000; /* Vermelho escuro para a maioria dos botões */
            color: black !important; /* Cor do texto do botão para preto por padrão */
            border-radius: 5px;
            padding: 10px 20px;
        }
        .stButton > button:hover {
            background-color: #A52A2A; /* Um pouco mais claro no hover */
        }

        /* Estilo específico para botões DENTRO de formulários (Cadastrar e Atualizar) */
        /* Isso deve ter prioridade sobre o estilo geral do botão */
        div[data-testid="stForm"] button {
            background-color: black !important;
            color: white !important; /* Garante que o texto seja branco */
            border: 1px solid white !important; /* Adiciona uma borda branca para destaque, opcional */
        }

        /* Cor dos warnings e success messages */
        .stAlert {
            color: black; /* Texto preto */
        }
        .stAlert[data-baseweb="notification"] {
            background-color: white; /* Fundo branco para contrastar */
        }
        .stAlert[data-baseweb="notification"].st-bd { /* Para sucesso */
            background-color: #d4edda;
            color: #155724;
        }
        .stAlert[data-baseweb="notification"].st-ce { /* Para erro */
            background-color: #f8d7da;
            color: #721c24;
        }
        .stAlert[data-baseweb="notification"].st-cf { /* Para info */
            background-color: #d1ecf1;
            color: #0c5460;
        }
        .stAlert[data-baseweb="notification"].st-cg { /* Para warning */
            background-color: #fff3cd;
            color: #856404;
        }

        /* Cor do expander */
        .streamlit-expanderHeader {
            background-color: #333333; /* Fundo do cabeçalho do expander */
            color: white; /* Texto do cabeçalho */
            border-radius: 5px;
        }
        .streamlit-expanderContent {
            background-color: #1a1a1a; /* Fundo do conteúdo do expander */
            border-radius: 0 0 5px 5px;
            padding: 10px;
        }
        .streamlit-expanderHeader > div > div > svg {
            color: white; /* Cor do ícone de seta do expander */
        }

        /* Cor da sidebar */
        .css-vk325g { /* ID do elemento da sidebar, pode mudar em versões futuras do Streamlit */
            background-color: #222222; /* Fundo da sidebar */
            color: white; /* Texto da sidebar */
        }
        .css-vk325g .stRadio > label {
            color: white; /* Cor do label do rádio button na sidebar */
        }
        .css-vk325g .stRadio div[data-baseweb="radio"] label {
            color: white; /* Cor do texto da opção do rádio button */
        }

        /* Para o filtro de texto */
        .stTextInput input {
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# --- Funções para manipulação do arquivo JSON ---
def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            dados = json.load(f)
            for nome_serie, serie in dados.items():
                if 'data_cadastro' in serie and isinstance(serie['data_cadastro'], str):
                    try:
                        serie['data_cadastro'] = datetime.fromisoformat(serie['data_cadastro'])
                    except ValueError:
                        try:
                            serie['data_cadastro'] = datetime.strptime(serie['data_cadastro'], '%d/%m/%Y %H:%M:%S')
                        except ValueError:
                            try:
                                serie['data_cadastro'] = datetime.strptime(serie['data_cadastro'], '%d/%m/%Y')
                            except ValueError:
                                pass
                if 'data_atualizacao' in serie and isinstance(serie['data_atualizacao'], str):
                    try:
                        serie['data_atualizacao'] = datetime.fromisoformat(serie['data_atualizacao'])
                    except ValueError:
                        try:
                            serie['data_atualizacao'] = datetime.strptime(serie['data_atualizacao'], '%d/%m/%Y %H:%M:%S')
                        except ValueError:
                            pass
                if 'ano_Serie' in serie:
                    try:
                        serie['ano_Serie'] = int(serie['ano_Serie'])
                    except (ValueError, TypeError):
                        pass
            return dados
    return {}

def salvar_dados(dados):
    dados_para_salvar = {}
    for nome_serie, serie in dados.items():
        serie_copy = serie.copy()
        if 'data_cadastro' in serie_copy and isinstance(serie_copy['data_cadastro'], datetime):
            serie_copy['data_cadastro'] = serie_copy['data_cadastro'].isoformat()
        if 'data_atualizacao' in serie_copy and isinstance(serie_copy['data_atualizacao'], datetime):
            serie_copy['data_atualizacao'] = serie_copy['data_atualizacao'].isoformat()
        dados_para_salvar[nome_serie] = serie_copy

    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(dados_para_salvar, f, ensure_ascii=False, indent=4)

def criar_serie(nome_serie, ano_Serie, season_Serie, episodios_Serie, pais_Serie, categoria_Serie, historico_medico=None):
    return {
        "nome_serie": nome_serie,
        "ano_Serie": ano_Serie,
        "season_Serie": season_Serie,
        "episodios_Serie": episodios_Serie,
        "pais_Serie": pais_Serie,
        "categoria_Serie": categoria_Serie,
        "historico_medico": historico_medico or [],
        "data_cadastro": datetime.now()
    }

# Funções CRUD
def cadastrar_serie():
    st.subheader("Cadastrar Nova Série")

    with st.form(key="form_cadastro_serie"):
        col1, col2 = st.columns(2)

        with col1:
            nome_serie = st.text_input("Nome da Série", max_chars=100)
            season_Serie = st.number_input("Temporada da Série", min_value=1, step=1)
            categoria_Serie = st.selectbox("Categoria da Série", ["Ação", "Aventura", "Comédia", "Drama", "Ficção Científica", "Fantasia", "Terror", "Suspense", "Documentário", "Animação", "Outro"])

        with col2:
            ano_Serie = st.number_input("Ano de Lançamento da Série", min_value=1900, max_value=datetime.now().year, step=1)
            episodios_Serie = st.number_input("Número de Episódios", min_value=0, step=1)
            pais_Serie = st.text_input("País de Origem da Série")
            historico_medico_raw = st.text_area("Notas Adicionais (opcional)")

        # O estilo para este botão agora está em set_page_style()
        submit_button = st.form_submit_button("Cadastrar Série")

        if submit_button:
            if not nome_serie or not ano_Serie:
                st.error("Nome da Série e Ano de Lançamento são campos obrigatórios!")
                return

            dados = carregar_dados()

            if nome_serie in dados:
                st.error("Série com este nome já cadastrada!")
                return

            serie = criar_serie(
                nome_serie=nome_serie,
                ano_Serie=int(ano_Serie),
                season_Serie=season_Serie,
                episodios_Serie=episodios_Serie,
                pais_Serie=pais_Serie,
                categoria_Serie=categoria_Serie,
                historico_medico=historico_medico_raw.split("\n") if historico_medico_raw else []
            )

            dados[nome_serie] = serie
            salvar_dados(dados)

            st.success("Série cadastrada com sucesso!")
            st.balloons()

def listar_series():
    st.subheader("Lista de Séries Cadastradas")

    dados = carregar_dados()

    if not dados:
        st.info("Nenhuma série cadastrada ainda.")
        return

    filtro_nome = st.text_input("Filtrar por nome da série:")

    series_filtradas = []
    for nome_serie, serie in dados.items():
        if filtro_nome.lower() in serie["nome_serie"].lower():
            series_filtradas.append((nome_serie, serie))

    if not series_filtradas:
        st.warning("Nenhuma série encontrada com o filtro aplicado.")
        return

    for nome_serie, serie in series_filtradas:
        with st.expander(f"{serie['nome_serie']} - Categoria: {serie['categoria_Serie']}"):
            col1, col2 = st.columns(2)

            with col1:
                st.write(f"**Nome da Série:** {serie['nome_serie']}")
                st.write(f"**Temporada:** {serie['season_Serie']}")
                st.write(f"**Categoria:** {serie['categoria_Serie']}")


            with col2:
                st.write(f"**Ano de Lançamento:** {serie['ano_Serie']}")
                st.write(f"**Número de Episódios:** {serie['episodios_Serie']}")
                st.write(f"**País de Origem:** {serie['pais_Serie']}")

                if 'data_cadastro' in serie:
                    if isinstance(serie['data_cadastro'], datetime):
                        st.write(f"**Cadastrado em:** {serie['data_cadastro'].strftime('%d/%m/%Y %H:%M:%S')}")
                    else:
                        st.write(f"**Cadastrado em:** {serie['data_cadastro']}")
                else:
                    st.write(f"**Cadastrado em:** Não disponível")

                if 'data_atualizacao' in serie:
                    if isinstance(serie['data_atualizacao'], datetime):
                        st.write(f"**Última Atualização:** {serie['data_atualizacao'].strftime('%d/%m/%Y %H:%M:%S')}")
                    else:
                        st.write(f"**Última Atualização:** {serie['data_atualizacao']}")
                else:
                    st.write(f"**Última Atualização:** Não disponível")


            if serie.get("historico_medico"):
                st.write("**Notas Adicionais:**")
                for item in serie["historico_medico"]:
                    st.write(f"- {item}")

def editar_serie():
    st.subheader("Editar Série")

    dados = carregar_dados()

    if not dados:
        st.info("Nenhuma série cadastrada para editar.")
        return

    nome_serie_selecionado = st.selectbox(
        "Selecione a série pelo nome",
        options=list(dados.keys()),
        format_func=lambda x: f"{dados[x]['nome_serie']} - {x}"
    )

    serie = dados[nome_serie_selecionado]

    with st.form(key="form_edicao_serie"):
        col1, col2 = st.columns(2)

        with col1:
            novo_nome_serie = st.text_input("Nome da Série", value=serie["nome_serie"], max_chars=100)
            season_Serie = st.number_input("Temporada da Série", value=int(serie["season_Serie"]), min_value=1, step=1)
            categoria_options = ["Ação", "Aventura", "Comédia", "Drama", "Ficção Científica", "Fantasia", "Terror", "Suspense", "Documentário", "Animação", "Outro"]
            categoria_index = categoria_options.index(serie["categoria_Serie"]) if serie["categoria_Serie"] in categoria_options else 0
            categoria_Serie = st.selectbox("Categoria da Série", categoria_options, index=categoria_index)

        with col2:
            ano_Serie_atual = serie.get('ano_Serie', 2000)
            ano_Serie_nova = st.number_input("Ano de Lançamento da Série", value=int(ano_Serie_atual), min_value=1900, max_value=datetime.now().year, step=1)

            episodios_Serie = st.number_input("Número de Episódios", value=int(serie["episodios_Serie"]), min_value=0, step=1)
            pais_Serie = st.text_input("País de Origem da Série", value=serie["pais_Serie"])
            historico_medico = st.text_area("Notas Adicionais", value="\n".join(serie["historico_medico"]))

        # O estilo para este botão agora está em set_page_style()
        submit_button = st.form_submit_button("Atualizar Série")

    if submit_button:
        if not novo_nome_serie or not ano_Serie_nova:
            st.error("Nome da Série e Ano de Lançamento são campos obrigatórios!")
            return

        if novo_nome_serie != nome_serie_selecionado and novo_nome_serie in dados:
            st.error("Já existe uma série com este novo nome!")
            return

        data_cadastro_original = serie.get("data_cadastro", datetime.now())

        if novo_nome_serie != nome_serie_selecionado:
            dados.pop(nome_serie_selecionado)

        serie_atualizada = {
            "nome_serie": novo_nome_serie,
            "ano_Serie": int(ano_Serie_nova),
            "season_Serie": season_Serie,
            "episodios_Serie": episodios_Serie,
            "pais_Serie": pais_Serie,
            "categoria_Serie": categoria_Serie,
            "historico_medico": historico_medico.split("\n") if historico_medico else [],
            "data_cadastro": data_cadastro_original,
            "data_atualizacao": datetime.now()
        }

        dados[novo_nome_serie] = serie_atualizada
        salvar_dados(dados)

        st.success("Série atualizada com sucesso!")

def excluir_serie():
    st.subheader("Excluir Série")

    dados = carregar_dados()

    if not dados:
        st.info("Nenhuma série cadastrada para excluir.")
        return

    nome_serie_selecionado = st.selectbox(
        "Selecione a série para excluir",
        options=list(dados.keys()),
        format_func=lambda x: f"{dados[x]['nome_serie']} - {x}"
    )

    serie = dados[nome_serie_selecionado]

    st.warning("Você está prestes a excluir a seguinte série:")
    st.json(serie)

    if st.button("Confirmar Exclusão"):
        dados.pop(nome_serie_selecionado)
        salvar_dados(dados)
        st.success("Série excluída com sucesso!")

# --- Aplicação Streamlit ---
set_page_style() # Chame a função de estilo no início da execução da aplicação

st.sidebar.title("Menu")
opcao = st.sidebar.radio(
    "Selecione uma opção:",
    ("Cadastrar Série", "Listar Séries",
     "Editar Série", "Excluir Série")
)

if opcao == "Cadastrar Série":
    cadastrar_serie()
elif opcao == "Listar Séries":
    listar_series()
elif opcao == "Editar Série":
    editar_serie()
elif opcao == "Excluir Série":
    excluir_serie()

# Rodapé
st.sidebar.markdown("---")
st.sidebar.markdown("Desenvolvido por Ana")
st.sidebar.markdown(f"Total de séries: {len(carregar_dados())}")