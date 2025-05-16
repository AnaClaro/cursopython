import streamlit as st
import json
import os
from datetime import datetime

# Nome do arquivo JSON
ARQUIVO_DADOS = "pacientes.json"

# Funções para manipulação do arquivo JSON
def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            dados = json.load(f)
            for cpf, paciente in dados.items():
                # Tenta converter data_cadastro se existir e for string
                if 'data_cadastro' in paciente and isinstance(paciente['data_cadastro'], str):
                    try:
                        # Tenta o formato ISO completo (como salvamos agora)
                        paciente['data_cadastro'] = datetime.fromisoformat(paciente['data_cadastro'])
                    except ValueError:
                        # Se não for ISO, tenta o formato DD/MM/YYYY HH:MM:SS
                        try:
                            paciente['data_cadastro'] = datetime.strptime(paciente['data_cadastro'], '%d/%m/%Y %H:%M:%S')
                        except ValueError:
                            # Se falhar, tenta apenas DD/MM/YYYY
                            try:
                                paciente['data_cadastro'] = datetime.strptime(paciente['data_cadastro'], '%d/%m/%Y')
                            except ValueError:
                                pass # Deixa como string ou lida com erro se não for nenhum formato esperado
                # Tenta converter data_atualizacao se existir e for string
                if 'data_atualizacao' in paciente and isinstance(paciente['data_atualizacao'], str):
                    try:
                        paciente['data_atualizacao'] = datetime.fromisoformat(paciente['data_atualizacao'])
                    except ValueError:
                        try:
                            paciente['data_atualizacao'] = datetime.strptime(paciente['data_atualizacao'], '%d/%m/%Y %H:%M:%S')
                        except ValueError:
                            pass
            return dados
    return {}

def salvar_dados(dados):
    dados_para_salvar = {}
    for cpf, paciente in dados.items():
        paciente_copy = paciente.copy()
        if 'data_cadastro' in paciente_copy and isinstance(paciente_copy['data_cadastro'], datetime):
            paciente_copy['data_cadastro'] = paciente_copy['data_cadastro'].isoformat()
        if 'data_atualizacao' in paciente_copy and isinstance(paciente_copy['data_atualizacao'], datetime):
            paciente_copy['data_atualizacao'] = paciente_copy['data_atualizacao'].isoformat()
        dados_para_salvar[cpf] = paciente_copy

    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(dados_para_salvar, f, ensure_ascii=False, indent=4)

def criar_paciente(cpf, nome, data_nascimento, sexo, endereco, telefone, email, historico_medico=None):
    return {
        "cpf": cpf,
        "nome": nome,
        "data_nascimento": data_nascimento,
        "sexo": sexo,
        "endereco": endereco,
        "telefone": telefone,
        "email": email,
        "historico_medico": historico_medico or [],
        "data_cadastro": datetime.now() # Salva como objeto datetime ao criar
    }

# Funções CRUD
def cadastrar_paciente():
    st.subheader("Cadastrar Novo Paciente")

    with st.form(key="form_cadastro"):
        col1, col2 = st.columns(2)

        with col1:
            cpf = st.text_input("CPF (somente números)", max_chars=11)
            nome = st.text_input("Nome Completo")
            data_nascimento_obj = st.date_input("Data de Nascimento", min_value=datetime(1900, 1, 1))
            sexo = st.selectbox("Sexo", ["Masculino", "Feminino", "Outro"])

        with col2:
            endereco = st.text_input("Endereço")
            telefone = st.text_input("Telefone")
            email = st.text_input("E-mail")
            historico_medico_raw = st.text_area("Histórico Médico (opcional)")

        submit_button = st.form_submit_button("Cadastrar Paciente")

        if submit_button:
            if not cpf or not nome:
                st.error("CPF e Nome são campos obrigatórios!")
                return

            dados = carregar_dados()

            if cpf in dados:
                st.error("Paciente com este CPF já cadastrado!")
                return

            data_nascimento_str = data_nascimento_obj.strftime("%d/%m/%Y")

            paciente = criar_paciente(
                cpf=cpf,
                nome=nome,
                data_nascimento=data_nascimento_str,
                sexo=sexo,
                endereco=endereco,
                telefone=telefone,
                email=email,
                historico_medico=historico_medico_raw.split("\n") if historico_medico_raw else []
            )

            dados[cpf] = paciente
            salvar_dados(dados)

            st.success("Paciente cadastrado com sucesso!")
            st.balloons()

def listar_pacientes():
    st.subheader("Lista de Pacientes Cadastrados")

    dados = carregar_dados()

    if not dados:
        st.info("Nenhum paciente cadastrado ainda.")
        return

    filtro_nome = st.text_input("Filtrar por nome:")

    pacientes_filtrados = []
    for cpf, paciente in dados.items():
        if filtro_nome.lower() in paciente["nome"].lower():
            pacientes_filtrados.append((cpf, paciente))

    if not pacientes_filtrados:
        st.warning("Nenhum paciente encontrado com o filtro aplicado.")
        return

    for cpf, paciente in pacientes_filtrados:
        with st.expander(f"{paciente['nome']} - CPF: {cpf}"):
            col1, col2 = st.columns(2)

            with col1:
                st.write(f"**Data de Nascimento:** {paciente['data_nascimento']}")
                st.write(f"**Sexo:** {paciente['sexo']}")
                st.write(f"**Endereço:** {paciente['endereco']}")

            with col2:
                st.write(f"**Telefone:** {paciente['telefone']}")
                st.write(f"**E-mail:** {paciente['email']}")
                # Verifica se a chave existe antes de tentar acessá-la e formatá-la
                if 'data_cadastro' in paciente:
                    if isinstance(paciente['data_cadastro'], datetime):
                        st.write(f"**Cadastrado em:** {paciente['data_cadastro'].strftime('%d/%m/%Y %H:%M:%S')}")
                    else:
                        st.write(f"**Cadastrado em:** {paciente['data_cadastro']}") # Se for string por algum motivo, exibe direto
                else:
                    st.write(f"**Cadastrado em:** Não disponível") # Caso a chave não exista (registros antigos)

                if 'data_atualizacao' in paciente:
                    if isinstance(paciente['data_atualizacao'], datetime):
                        st.write(f"**Última Atualização:** {paciente['data_atualizacao'].strftime('%d/%m/%Y %H:%M:%S')}")
                    else:
                        st.write(f"**Última Atualização:** {paciente['data_atualizacao']}")
                else:
                    st.write(f"**Última Atualização:** Não disponível")


            if paciente["historico_medico"]:
                st.write("**Histórico Médico:**")
                for item in paciente["historico_medico"]:
                    st.write(f"- {item}")

def editar_paciente():
    st.subheader("Editar Paciente")

    dados = carregar_dados()

    if not dados:
        st.info("Nenhum paciente cadastrado para editar.")
        return

    cpf_selecionado = st.selectbox(
        "Selecione o paciente pelo CPF",
        options=list(dados.keys()),
        format_func=lambda x: f"{dados[x]['nome']} - {x}"
    )

    paciente = dados[cpf_selecionado]

    with st.form(key="form_edicao"):
        col1, col2 = st.columns(2)

        with col1:
            novo_cpf = st.text_input("CPF (somente números)", value=paciente["cpf"], max_chars=11)
            nome = st.text_input("Nome Completo", value=paciente["nome"])

            data_nascimento_str_atual = paciente["data_nascimento"]
            try:
                data_nascimento_obj_atual = datetime.strptime(data_nascimento_str_atual, "%d/%m/%Y").date()
            except ValueError:
                data_nascimento_obj_atual = datetime(2000, 1, 1).date()

            data_nascimento_obj_nova = st.date_input("Data de Nascimento", value=data_nascimento_obj_atual, min_value=datetime(1900, 1, 1))

            sexo_options = ["Masculino", "Feminino", "Outro"]
            sexo_index = sexo_options.index(paciente["sexo"]) if paciente["sexo"] in sexo_options else 0
            sexo = st.selectbox("Sexo", sexo_options, index=sexo_index)

        with col2:
            endereco = st.text_input("Endereço", value=paciente["endereco"])
            telefone = st.text_input("Telefone", value=paciente["telefone"])
            email = st.text_input("E-mail", value=paciente["email"])
            historico_medico = st.text_area("Histórico Médico", value="\n".join(paciente["historico_medico"]))

        submit_button = st.form_submit_button("Atualizar Paciente")

    if submit_button:
        if not novo_cpf or not nome:
            st.error("CPF e Nome são campos obrigatórios!")
            return

        if novo_cpf != cpf_selecionado and novo_cpf in dados:
            st.error("Já existe um paciente com este novo CPF!")
            return

        # Captura a data de cadastro original, se existir
        data_cadastro_original = paciente.get("data_cadastro", datetime.now()) # Usa a data atual se não existir

        if novo_cpf != cpf_selecionado:
            dados.pop(cpf_selecionado)

        paciente_atualizado = {
            "cpf": novo_cpf,
            "nome": nome,
            "data_nascimento": data_nascimento_obj_nova.strftime("%d/%m/%Y"),
            "sexo": sexo,
            "endereco": endereco,
            "telefone": telefone,
            "email": email,
            "historico_medico": historico_medico.split("\n") if historico_medico else [],
            "data_cadastro": data_cadastro_original, # Mantém a data de cadastro original ou a nova se não existia
            "data_atualizacao": datetime.now()
        }

        dados[novo_cpf] = paciente_atualizado
        salvar_dados(dados)

        st.success("Paciente atualizado com sucesso!")

def excluir_paciente():
    st.subheader("Excluir Paciente")

    dados = carregar_dados()

    if not dados:
        st.info("Nenhum paciente cadastrado para excluir.")
        return

    cpf_selecionado = st.selectbox(
        "Selecione o paciente pelo CPF para excluir",
        options=list(dados.keys()),
        format_func=lambda x: f"{dados[x]['nome']} - {x}"
    )

    paciente = dados[cpf_selecionado]

    st.warning("Você está prestes a excluir o seguinte paciente:")
    st.json(paciente)

    if st.button("Confirmar Exclusão"):
        dados.pop(cpf_selecionado)
        salvar_dados(dados)
        st.success("Paciente excluído com sucesso!")

# Menu lateral
st.sidebar.title("Menu")
opcao = st.sidebar.radio(
    "Selecione uma opção:",
    ("Cadastrar Paciente", "Listar Pacientes",
     "Editar Paciente", "Excluir Paciente")
)

# Navegação entre páginas
if opcao == "Cadastrar Paciente":
    cadastrar_paciente()
elif opcao == "Listar Pacientes":
    listar_pacientes()
elif opcao == "Editar Paciente":
    editar_paciente()
elif opcao == "Excluir Paciente":
    excluir_paciente()

# Rodapé
st.sidebar.markdown("---")
st.sidebar.markdown("Desenvolvido por Gilberto")
st.sidebar.markdown(f"Total de pacientes: {len(carregar_dados())}")