import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

amostra_10_pesos = pd.DataFrame({'Peso das barras de chocolate (g)': [99.4197, 101.821, 98.5708, 100.63, 94.7449, 99.3241, 97.6067, 100.679, 108.739, 99.0544]})
dp = amostra_10_pesos['Peso das barras de chocolate (g)'].std()

sns.kdeplot(amostra_10_pesos['Peso das barras de chocolate (g)'], linewidth=2, fill= True, label=f'Desvio padrão = {dp:.3f}')
plt.legend()

plt.ylabel('Frequência')
plt.title('Distribuição suave pesos de barra amostrais')
plt.show()

import numpy as np
import pandas as pd
 
amostra_10_pesos = pd.DataFrame({'Peso das barras de chocolate (g)': [99.4197, 101.821, 98.5708, 100.63, 94.7449, 99.3241, 97.6067, 100.679, 108.739, 99.0544]})

# Desvio padrão
dp_amostral = amostra_10_pesos['Peso das barras de chocolate (g)'].std()

# Tamanho da amostra
tamanho_amostra = len(amostra_10_pesos)

# Calculando o Erro Padrão da Amostra
erro_padrao_amostral = dp_amostral / np.sqrt(tamanho_amostra)

print('Erro padrão:', erro_padrao_amostral )

import pandas as pd
 
amostra_10_pesos = pd.DataFrame({'Peso das barras de chocolate (g)': [99.4197, 101.821, 98.5708, 100.63, 94.7449, 99.3241, 97.6067, 100.679, 108.739, 99.0544]})

## Calculando o Erro Padrão da Amostra

from scipy import stats

erro_padrao_amostral = stats.sem(amostra_10_pesos['Peso das barras de chocolate (g)'])
print('Erro padrão:', erro_padrao_amostral)