# Bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
dados_idade_aposentadoria = pd.read_csv('/content/dados_idade_aposentadoria.csv')

# Aleatorizar a ordem
dados_idade_aposentadoria = dados_idade_aposentadoria.sample(120)

# Mostrar as cinco primeiras linhas
dados_idade_aposentadoria.head()


# Coletar a média para cada tamanho de amostra
medias = [dados_idade_aposentadoria[0:i]['idade'].mean() for i in range(1, 120)]

# Plotar a linha
plt.figure(figsize=(16,6))
plt.title('O efeito do tamanho da amostra')
plt.xlabel('Quantidade de amostras')
plt.ylabel('Média de idades')
plt.plot(medias, linewidth=1)