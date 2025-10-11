import pandas as pd

# Exemplo integrando Series e DataFrame
# Análise de vendas de uma empresa

# Criando Series individuais
vendedores = pd.Series(['Ana', 'Carlos', 'Beatriz', 'Daniel'])
vendas_q1 = pd.Series([15000, 22000, 18000, 25000])
vendas_q2 = pd.Series([17000, 24000, 19000, 26000])
comissoes = pd.Series([0.05, 0.06, 0.055, 0.065])

# Criando DataFrame a partir das Series
df_vendas = pd.DataFrame({
    'Vendedor': vendedores,
    'Vendas_Q1': vendas_q1,
    'Vendas_Q2': vendas_q2,
    'Taxa_Comissao': comissoes
})

print("DataFrame de Vendas:")
print(df_vendas)

# Cálculos usando Series
df_vendas['Vendas_Total'] = df_vendas['Vendas_Q1'] + df_vendas['Vendas_Q2']
df_vendas['Comissao_Total'] = df_vendas['Vendas_Total'] * df_vendas['Taxa_Comissao']
df_vendas['Crescimento'] = ((df_vendas['Vendas_Q2'] - df_vendas['Vendas_Q1']) / 
                           df_vendas['Vendas_Q1'] * 100)

print("\nDataFrame com cálculos:")
print(df_vendas)

# Análises usando métodos de Series
melhor_vendedor = df_vendas.loc[df_vendas['Vendas_Total'].idxmax(), 'Vendedor']
maior_crescimento = df_vendas['Crescimento'].max()
media_vendas = df_vendas['Vendas_Total'].mean()

print(f"\nMelhor vendedor: {melhor_vendedor}")
print(f"Maior crescimento: {maior_crescimento:.1f}%")
print(f"Média de vendas: R$ {media_vendas:.2f}")

# Filtro complexo
alta_performance = df_vendas[
    (df_vendas['Vendas_Total'] > media_vendas) & 
    (df_vendas['Crescimento'] > 0)
]

print("\nVendedores de alta performance:")
print(alta_performance[['Vendedor', 'Vendas_Total', 'Crescimento']])