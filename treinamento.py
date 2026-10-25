
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression

SEED = 42

# 1. Carregar o dataset
dataset = pd.read_csv("dataset/survey_results_public.csv")

# 2. Selecionar as colunas necessárias
dados = dataset[
    ["Age", "Education", "YearsCode", "Employment"]
].copy()

# 3. Limpar espaços das categorias
for coluna in ["Age", "Education", "Employment"]:
    dados[coluna] = dados[coluna].apply(
        lambda valor: valor.strip()
        if isinstance(valor, str)
        else valor
    )

# 4. Converter anos de programação para número
dados["YearsCode"] = pd.to_numeric(
    dados["YearsCode"],
    errors="coerce"
)

# 5. Definir as categorias de emprego
empregados = [
    "Employed",
    "Independent contractor, freelancer, or self-employed"
]

nao_empregados = [
    "Student",
    "Not employed"
]

# 6. Manter apenas as categorias selecionadas
dados = dados[
    dados["Employment"].isin(empregados + nao_empregados)
].copy()

# 7. Criar a variável-alvo
dados["Empregado"] = (
    dados["Employment"].isin(empregados).astype(int)
)

# 8. Separar as entradas e o resultado esperado
X = dados[["Age", "Education", "YearsCode"]]
y = dados["Empregado"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=SEED,
    stratify=y
)

# 9. Preparar os dados numéricos
preprocessamento_numerico = Pipeline([
    ("imputador", SimpleImputer(strategy="median")),
    ("escalador", StandardScaler())
])

# 10. Preparar os dados categóricos
preprocessamento_categorico = Pipeline([
    ("imputador", SimpleImputer(strategy="most_frequent")),
    ("codificador", OneHotEncoder(handle_unknown="ignore"))
])

# 11. Combinar os pré-processamentos
preprocessamento = ColumnTransformer([
    (
        "numerico",
        preprocessamento_numerico,
        ["YearsCode"]
    ),
    (
        "categorico",
        preprocessamento_categorico,
        ["Age", "Education"]
    )
])

# 12. Criar o pipeline completo
modelo = Pipeline([
    ("preprocessamento", preprocessamento),
    (
        "modelo",
        LogisticRegression(
            random_state=SEED,
            max_iter=1000,
            class_weight="balanced"
        )
    )
])

# 13. Treinar o modelo
modelo.fit(X_train, y_train)

# 14. Salvar o modelo completo
with open("modelo/modelo_emprego.sav", "wb") as arquivo:
    pickle.dump(modelo, arquivo)
