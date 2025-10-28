
import pandas as pd

# Dados do exemplo
df = pd.DataFrame({'Desempenho': {0: 'Regular', 1: 'Bom', 2: 'Bom', 3: 'Excelente', 4: 'Bom', 5: 'Bom', 6: 'Regular', 7: 'Regular', 8: 'Excelente', 9: 'Ruim', 10: 'Bom', 11: 'Regular', 12: 'Muito Bom', 13: 'Bom', 14: 'Bom', 15: 'Regular', 16: 'Muito Bom', 17: 'Bom', 18: 'Muito Bom', 19: 'Excelente', 20: 'Ruim', 21: 'Excelente', 22: 'Ruim', 23: 'Ruim', 24: 'Regular', 25: 'Excelente', 26: 'Ruim', 27: 'Excelente', 28: 'Excelente', 29: 'Regular', 30: 'Regular', 31: 'Ruim', 32: 'Regular', 33: 'Regular', 34: 'Muito Bom', 35: 'Excelente', 36: 'Regular', 37: 'Excelente', 38: 'Excelente', 39: 'Muito Bom', 40: 'Ruim', 41: 'Ruim', 42: 'Ruim', 43: 'Ruim', 44: 'Muito Bom', 45: 'Regular', 46: 'Excelente', 47: 'Muito Bom', 48: 'Muito Bom', 49: 'Muito Bom', 50: 'Muito Bom', 51: 'Muito Bom', 52: 'Bom', 53: 'Ruim', 54: 'Muito Bom', 55: 'Bom', 56: 'Bom', 57: 'Excelente', 58: 'Bom', 59: 'Muito Bom'},
                   'Metodo_Ensino': {0: 'Moderno', 1: 'Tradicional', 2: 'Tradicional', 3: 'Moderno', 4: 'Moderno', 5: 'Moderno', 6: 'Moderno', 7: 'Moderno', 8: 'Moderno', 9: 'Tradicional', 10: 'Tradicional', 11: 'Moderno', 12: 'Tradicional', 13: 'Moderno', 14: 'Tradicional', 15: 'Tradicional', 16: 'Moderno', 17: 'Moderno', 18: 'Tradicional', 19: 'Tradicional', 20: 'Moderno', 21: 'Tradicional', 22: 'Moderno', 23: 'Moderno', 24: 'Tradicional', 25: 'Tradicional', 26: 'Moderno', 27: 'Moderno', 28: 'Moderno', 29: 'Moderno', 30: 'Moderno', 31: 'Moderno', 32: 'Tradicional', 33: 'Moderno', 34: 'Tradicional', 35: 'Tradicional', 36: 'Tradicional', 37: 'Moderno', 38: 'Tradicional', 39: 'Moderno', 40: 'Tradicional', 41: 'Moderno', 42: 'Tradicional', 43: 'Moderno', 44: 'Moderno', 45: 'Moderno', 46: 'Moderno', 47: 'Moderno', 48: 'Moderno', 49: 'Tradicional', 50: 'Moderno', 51: 'Moderno', 52: 'Moderno', 53: 'Moderno', 54: 'Tradicional', 55: 'Moderno', 56: 'Moderno', 57: 'Tradicional', 58: 'Moderno', 59: 'Tradicional'}})

# Tabela de contingência
tab_contingencia = pd.crosstab(df['Desempenho'], df['Metodo_Ensino'])

from scipy.stats import chi2_contingency

chi2, p_valor, _, _ = chi2_contingency(tab_contingencia)

# Resultados iniciais
print(f'Estatística chi2: {chi2}')
print(f'p-valor: {p_valor}')

# Tomada de decisão
nivel_significancia = 0.05
if p_valor < nivel_significancia:
    conclusao = 'Rejeitar a hipótese nula'
else:
    conclusao = 'Não rejeitar a hipótese nula'

print('Conclusão:', conclusao)

