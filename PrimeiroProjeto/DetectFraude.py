import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# 1. Carregar os dados
dados = pd.read_csv("E:\DataSet\Transacoes.csv")

# 🔧 Converter colunas categóricas em numéricas
dados = pd.get_dummies(dados, columns=["localizacao", "tipo_pagamento"])

# 2. Separar variáveis independentes (X) e alvo (y)
X = dados.drop("fraude", axis=1)
y = dados["fraude"]

# 3. Dividir em treino e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# 4. Criar e treinar o modelo Random Forest
modelo = RandomForestClassifier(
    n_estimators=200,
    class_weight={0:1, 1:10},
    random_state=42,
    n_jobs=-1
)

modelo.fit(X_treino, y_treino)

# 5. Fazer previsões
y_pred = modelo.predict(X_teste)

# 6. Avaliar o desempenho
print("\n=== Matriz de Confusão ===")
print(confusion_matrix(y_teste, y_pred))
print("\n=== Relatório de Classificação ===")
print(classification_report(y_teste, y_pred))

# 7. Ver as variáveis mais importantes
importances = pd.Series(modelo.feature_importances_, index=X.columns)
print("\n=== Top 10 variáveis mais importantes ===")
print(importances.sort_values(ascending=False).head(10))