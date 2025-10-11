import pandas as pd
import numpy as np

# ========== CRIAÇÃO DE DATAFRAMES ==========

# Criando DataFrame a partir de dicionário
dados = {
    'Nome': ['Ana', 'João', 'Maria', 'Pedro', 'Carla'],
    'Idade': [25, 30, 35, 28, 32],
    'Cidade': ['SP', 'RJ', 'BH', 'SP', 'RJ'],
    'Salário': [5000, 7000, 6000, 5500, 6500],
    'Departamento': ['Vendas', 'TI', 'RH', 'Vendas', 'TI']
}

df = pd.DataFrame(dados)
print("DataFrame criado:")
print(df)

# Criando DataFrame com índice personalizado
df_index = pd.DataFrame(dados, index=['A', 'B', 'C', 'D', 'E'])
print("\nDataFrame com índice personalizado:")
print(df_index)

# ========== INFORMAÇÕES BÁSICAS ==========

print(f"\nShape do DataFrame: {df.shape}")
print(f"\nColunas: {df.columns.tolist()}")
print(f"\nTipos de dados:")
print(df.dtypes)
print(f"\nInformações gerais:")
df.info()

# ========== ACESSO A DADOS ==========

print("\nPrimeiras 3 linhas:")
print(df.head(3))

print("\nÚltimas 2 linhas:")
print(df.tail(2))

# Acesso a colunas
print("\nColuna 'Nome':")
print(df['Nome'])

print("\nColunas 'Nome' e 'Idade':")
print(df[['Nome', 'Idade']])

# Acesso a linhas por índice
print("\nLinha 2:")
print(df.iloc[2])

print("\nLinhas 1 a 3:")
print(df.iloc[1:4])

# Acesso por label
print("\nLinha com índice 'B':")
print(df_index.loc['B'])

# ========== FILTROS E SELEÇÕES ==========

# Filtro por condição
funcionarios_sp = df[df['Cidade'] == 'SP']
print("\nFuncionários de SP:")
print(funcionarios_sp)

# Múltiplas condições
ti_acima_30 = df[(df['Departamento'] == 'TI') & (df['Idade'] > 28)]
print("\nFuncionários de TI com mais de 28 anos:")
print(ti_acima_30)

# Filtro com query
alta_renda = df.query('Salário > 6000')
print("\nFuncionários com salário > 6000:")
print(alta_renda)

# ========== OPERAÇÕES E CÁLCULOS ==========

print(f"\nEstatísticas descritivas:")
print(df.describe())

print(f"\nMédia de salários: R$ {df['Salário'].mean():.2f}")
print(f"Salário máximo: R$ {df['Salário'].max()}")
print(f"Salário mínimo: R$ {df['Salário'].min()}")

# Agrupamento
salario_por_depto = df.groupby('Departamento')['Salário'].mean()
print("\nSalário médio por departamento:")
print(salario_por_depto)

contagem_por_cidade = df['Cidade'].value_counts()
print("\nNúmero de funcionários por cidade:")
print(contagem_por_cidade)

# ========== MANIPULAÇÃO DE DADOS ==========

# Adicionando nova coluna
df['Salário Ajustado'] = df['Salário'] * 1.1
df['Faixa Etária'] = pd.cut(df['Idade'], 
                           bins=[20, 30, 40], 
                           labels=['Jovem', 'Adulto'])
print("\nDataFrame com novas colunas:")
print(df)

# Removendo coluna
df_sem_idade = df.drop('Idade', axis=1)
print("\nDataFrame sem coluna Idade:")
print(df_sem_idade)

# ========== TRATAMENTO DE VALORES FALTANTES ==========

# Criando DataFrame com valores faltantes para exemplo
df_com_nan = df.copy()
df_com_nan.loc[2, 'Salário'] = np.nan
df_com_nan.loc[4, 'Idade'] = np.nan

print("\nDataFrame com valores faltantes:")
print(df_com_nan)

print("\nValores nulos por coluna:")
print(df_com_nan.isnull().sum())

# Preenchendo valores faltantes
df_preenchido = df_com_nan.fillna({'Salário': df_com_nan['Salário'].mean(), 
                                  'Idade': df_com_nan['Idade'].median()})
print("\nDataFrame com valores preenchidos:")
print(df_preenchido)

# ========== ORDENAÇÃO ==========

df_ordenado_salario = df.sort_values('Salário', ascending=False)
print("\nDataFrame ordenado por salário (decrescente):")
print(df_ordenado_salario)

df_ordenado_multiplo = df.sort_values(['Departamento', 'Salário'], 
                                     ascending=[True, False])
print("\nDataFrame ordenado por departamento (asc) e salário (desc):")
print(df_ordenado_multiplo)

# ========== OPERAÇÕES COM STRINGS ==========

df['Nome Maiúsculo'] = df['Nome'].str.upper()
df['Iniciais'] = df['Nome'].str.split().str[0].str[0] + df['Nome'].str.split().str[-1].str[0]
print("\nDataFrame com operações de string:")
print(df[['Nome', 'Nome Maiúsculo', 'Iniciais']])

# ========== EXPORTAÇÃO E IMPORTAÇÃO ==========

# Salvando para CSV
df.to_csv('funcionarios.csv', index=False)

# Lendo de CSV
# df_lido = pd.read_csv('funcionarios.csv')

# ========== EXEMPLO PRÁTICO COMPLETO ==========

print("\n=== ANÁLISE COMPLETA ===")
print("Resumo estatístico por departamento:")
resumo_depto = df.groupby('Departamento').agg({
    'Salário': ['mean', 'max', 'min', 'count'],
    'Idade': 'mean'
}).round(2)

print(resumo_depto)