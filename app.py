
import streamlit as st
import pickle
import pandas as pd

st.set_page_config(
    page_title="Predição de Empregabilidade",
    page_icon="📊",
    layout="centered"
)


@st.cache_resource
def carregar_modelo():
    with open("modelo/modelo_emprego.sav", "rb") as arquivo:
        modelo = pickle.load(arquivo)

    return modelo


try:
    modelo_emprego = carregar_modelo()
except FileNotFoundError:
    st.error(
        "Modelo não encontrado. Verifique se o arquivo "
        "modelo_emprego.sav está na pasta modelo."
    )
    st.stop()
except Exception as erro:
    st.error(f"Não foi possível carregar o modelo: {erro}")
    st.stop()


st.markdown("""
**Alunos:** Eduardo Lemes e Guilherme Batista de Souza

**Curso:** Análise e Desenvolvimento de Sistemas

**Disciplina:** Tópicos Avançados em Inteligência Artificial

**Dataset:** Stack Overflow Developer Survey
""")

st.divider()

st.title("📊 Predição de Empregabilidade")

st.write(
    "Informe suas características para estimar a probabilidade "
    "de pertencer ao grupo de profissionais empregados."
)

st.info(
    "A estimativa é baseada nos padrões encontrados nos dados "
    "do Stack Overflow. Ela não representa uma garantia de emprego."
)

st.header("Informações do profissional")

faixa_etaria = st.selectbox(
    "Faixa etária",
    [
        "Under 18 years old",
        "18-24 years old",
        "25-34 years old",
        "35-44 years old",
        "45-54 years old",
        "55-64 years old",
        "65 years or older",
        "Prefer not to say"
    ],
    index=2
)

escolaridade = st.selectbox(
    "Escolaridade",
    [
        "Primary/elementary school",
        "Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)",
        "Some college/university study without earning a degree",
        "Associate degree (A.A., A.S., etc.)",
        "Bachelor's degree (B.A., B.S., B.Eng., etc.)",
        "Master's degree (M.A., M.S., M.Eng., MBA, etc.)",
        "Professional degree (JD, MD, Ph.D, Ed.D, etc.)",
        "Something else"
    ],
    index=4
)

anos_programacao = st.number_input(
    "Anos de experiência com programação",
    min_value=0,
    max_value=60,
    value=5,
    step=1
)

st.divider()

if st.button("Calcular probabilidade", type="primary", use_container_width=True):

    # Criar DataFrame com os nomes e a ordem das colunas
    # utilizados durante o treinamento do modelo.
    dados_usuario = pd.DataFrame([{
        "Age": faixa_etaria,
        "Education": escolaridade,
        "YearsCode": anos_programacao
    }])

    # O Pipeline executa automaticamente o pré-processamento.
    previsao = modelo_emprego.predict(dados_usuario)[0]

    probabilidades = modelo_emprego.predict_proba(dados_usuario)[0]

    # Encontrar a posição correspondente à classe 1 (Empregado).
    classes = list(modelo_emprego.named_steps["modelo"].classes_)
    indice_empregado = classes.index(1)

    probabilidade_empregado = probabilidades[indice_empregado]

    st.subheader("Resultado da análise")

    st.metric(
        label="Probabilidade estimada de pertencer ao grupo empregado",
        value=f"{probabilidade_empregado:.2%}"
    )

    st.progress(float(probabilidade_empregado))

    if previsao == 1:
        st.success(
            "Classificação do modelo: Empregado"
        )
    else:
        st.warning(
            "Classificação do modelo: Não empregado"
        )

    st.caption(
        "A classificação é definida pelo modelo. A probabilidade "
        "é uma estimativa estatística e não uma previsão garantida "
        "de contratação."
    )

    with st.expander("Ver dados utilizados na previsão"):
        st.dataframe(
            dados_usuario,
            use_container_width=True,
            hide_index=True
        )
