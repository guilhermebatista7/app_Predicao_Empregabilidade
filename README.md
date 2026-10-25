# 💼 Predição de Empregabilidade com Inteligência Artificial

Aplicação web interativa desenvolvida para estimar a probabilidade de um profissional do setor de tecnologia pertencer ao grupo de empregados, com base em sua faixa etária, escolaridade e anos de experiência em programação.

Projeto acadêmico desenvolvido para a disciplina de **Tópicos Avançados em Inteligência Artificial** no **IFSP - Campus Catanduva**, sob orientação do **Prof. Dr. Márcio Andrey Teixeira**.

---

## 📁 Estrutura do Projeto

```text
app_Predicao_Empregabilidade/
│
├── dataset/
│
├── modelo/
│   └── modelo_emprego.sav     # Modelo treinado
│
├── .gitignore                 
├── app.py                     # Aplicação web Streamlit
├── requirements.txt           # Dependências para deploy no Streamlit Cloud
├── treinamento.py             # Script de preparação e treinamento do modelo
└── README.md                  # Documentação do projeto
```

---

## Metodologia e Escolha do Modelo

O conjunto de dados utilizado é o **Stack Overflow Developer Survey**.  
Variáveis utilizadas:
* `Age` (Faixa etária)
* `Education` (Nível educacional)
* `YearsCode` (Tempo total em anos de experiência com programação)

A variável-alvo `Empregado` foi binarizada:
* **1 (Empregado):** Profissionais com emprego em tempo integral/parcial ou atuando de forma independente/freelancer.
* **0 (Não empregado):** Estudantes ou pessoas sem ocupação no momento da pesquisa.

---

## Como Executar Localmente

### 1. Clonar ou navegar até a pasta do projeto:
```bash
cd app_Predicao_Empregabilidade
```

### 2. Criar e ativar um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate
```

### 3. Instalar as dependências:
```bash
pip install -r requirements.txt
```

### 4. Executar a aplicação Streamlit:
```bash
streamlit run app.py
```

---

## 🌐 Como Hospedar Gratuitamente no Streamlit Cloud via GitHub

### Passo 1: Subir o projeto para o GitHub
1. Crie um novo repositório no seu GitHub (exemplo: `app-predicao-empregabilidade`), deixe-o como **Public**.
2. Na pasta do projeto em seu terminal (ou via **GitHub Desktop**):
   ```bash
   git init
   git add .
   git commit -m "Deploy: app de predição de empregabilidade"
   git branch -M main
   git remote add origin https://github.com/SEU_USUARIO/app-predicao-empregabilidade.git
   git push -u origin main
   ```
   *(Certifique-se de que o arquivo `modelo/modelo_emprego.sav` esteja comitad*

### Passo 2: Publicar no Streamlit Community Cloud
1. Acesse [share.streamlit.io](https://share.streamlit.io/) e faça login com sua conta do GitHub.
2. Clique no botão **"New app"** (ou "Create app").
3. Selecione o repositório que você acabou de criar:
   - **Repository:** `SEU_USUARIO/app-predicao-empregabilidade`
   - **Branch:** `main`
   - **Main file path:** `app.py`
4. Clique em **"Deploy!"**.
5. O Streamlit Cloud instalará as dependências do `requirements.txt` e sua aplicação ficará disponível mundialmente com uma URL pública (ex.: `https://apppredicaoempregabilidade-a7umgur4buq9h4bqfk4hjz.streamlit.app/`).

---

## 📊 Caso queira realizar testes e verificar como o modelo desenvolvido, acesse o notebook criado no google colab.
Aesse o link, baixe o notebook e crie um próprio com o mesmo conteúdo: `https://colab.research.google.com/drive/1vDlo6nu46oj4mvKJ2YfQCV9LnWfHBjvM?usp=sharing`

Em seguida acesse: `https://github.com/StackExchange/Survey/blob/main/packages/archive/2026/survey_results_public.csv` e baixa o arquivo com extensão .csv poara ter acesso ao mesmo banco utilizado.

Logo após, crie a essa sequência de pastas em seu drive e coloque o dataset instalado: Lab_IA/Dataset/survey_results_public.csv

Nesse momento, basta conectar seu google colab ao google drive para conseguir executar o notebook passo a passo.
