# 🧮 Curso 3 — NumPy: Análise Numérica Eficiente com Python

Este módulo apresenta o **NumPy**, uma das bibliotecas fundamentais para **análise numérica e científica com Python**.  
Com o NumPy, é possível manipular grandes conjuntos de dados de forma eficiente e realizar cálculos matemáticos e estatísticos com alta performance.

---

## 📦 Instalação

```bash
pip install numpy matplotlib

📚 Importação de Bibliotecas
import numpy as np
import matplotlib.pyplot as plt

🔹 Criação e Leitura de Dados
np.arange(1, 88, 1)


Cria um array NumPy de 1 até 87, com passo 1.

dado = np.loadtxt(url, delimiter=',', usecols=np.arange(1, 88, 1))


Carrega dados de um arquivo .csv localizado em url, usando , como separador e apenas as colunas desejadas.

🔹 Propriedades de Arrays
dado.ndim     # Retorna o número de dimensões do array
dado.size     # Retorna o número total de elementos
dado.shape    # Retorna o formato (linhas, colunas)
dado.T        # Transpõe o array (linhas ↔ colunas)
dado.T.shape  # Mostra o formato da matriz transposta

🔹 Seleção e Fatiamento de Dados
precos = dado_transposto[:, 

Você disse:
entre tudo em bloco de codigo
O ChatGPT disse:

Perfeito 👍
Aqui está todo o README do Curso 3 (NumPy) formatado inteiramente dentro de um único bloco de código, pronto para copiar e colar:

# 🧮 Curso 3 — NumPy: Análise Numérica Eficiente com Python

Este módulo apresenta o **NumPy**, uma das bibliotecas fundamentais para **análise numérica e científica com Python**.  
Com o NumPy, é possível manipular grandes conjuntos de dados de forma eficiente e realizar cálculos matemáticos e estatísticos com alta performance.

---

## 📦 Instalação

```python
pip install numpy matplotlib

📚 Importação de Bibliotecas
import numpy as np
import matplotlib.pyplot as plt

🔹 Criação e Leitura de Dados
np.arange(1, 88, 1)  
# Cria um array NumPy de 1 até 87 com passo 1

dado = np.loadtxt(url, delimiter=',', usecols=np.arange(1, 88, 1))
# Carrega dados de um arquivo CSV usando apenas colunas selecionadas

🔹 Propriedades de Arrays
dado.ndim       # Número de dimensões do array
dado.size       # Quantidade total de elementos
dado.shape      # Formato (linhas, colunas)
dado.T          # Transpõe o array (linhas <-> colunas)
dado.T.shape    # Verifica o formato após a transposição

🔹 Seleção e Fatiamento de Dados
precos = dado_transposto[:, 1:6]
# Seleciona colunas 1 até 5 (dados de preços, por exemplo)

plt.plot(datas, precos[:, 0])
# Plota os valores da primeira coluna em função das datas

🔹 Criação de Variáveis para Colunas
Moscow = precos[:, 0]
Kaliningrad = precos[:, 1]
Petersburg = precos[:, 2]
Krasnodar = precos[:, 3]
Ekaterinburg = precos[:, 4]

🔹 Plotando Dados de Múltiplos Anos
plt.plot(np.arange(1, 13, 1), Moscow_ano1)
plt.plot(np.arange(1, 13, 1), Moscow_ano2)
plt.plot(np.arange(1, 13, 1), Moscow_ano3)
plt.plot(np.arange(1, 13, 1), Moscow_ano4)
plt.legend(['ano1', 'ano2', 'ano3', 'ano4'])

🔹 Comparação de Arrays
np.array_equal(Moscow_ano3, Moscow_ano4)
# Verifica se dois arrays são idênticos (True/False)

np.allclose(Moscow_ano3, Moscow_ano4, 10)
# Verifica se dois arrays são "aproximadamente" iguais (com tolerância)

🔹 Verificação de Dados Ausentes (NaN)
np.isnan(Kaliningrad)
# Retorna True para valores ausentes (NaN)

sum(np.isnan(Kaliningrad))
# Conta quantos valores são NaN

np.mean([Kaliningrad[3], Kaliningrad[5]])
# Calcula a média de valores específicos

🔹 Regressão Linear — Equação da Reta

A equação da reta:
y = a·x + b

a → coeficiente angular (inclinação)

b → intercepto (ponto onde a reta cruza o eixo y)

x → variável independente

y → variável dependente

x = datas
y = 2 * x + 80

plt.plot(datas, Moscow)
plt.plot(datas, y)

# Erro entre valores reais e previstos
np.sqrt(np.sum(np.power(Moscow - y, 2)))


A equação do coeficiente angular é:

a = [n * Σ(XiYi) - Σ(Xi) * Σ(Yi)] / [n * Σ(Xi²) - (Σ(Xi))²]

🔹 Plotando a Reta e Pontos Específicos
plt.plot(datas, Moscow)
plt.plot(datas, y)
plt.plot(41.5, a * 41.5 + b, '*r')  # Ponto vermelho (predição)
plt.plot(100, a * 100 + b, '*r')    # Outro ponto de predição

🔹 Geração de Valores Aleatórios com NumPy
np.random.uniform(low=0.10, high=0.90, size=100)
# Gera 100 números aleatórios entre 0.10 e 0.90

np.random.seed(16)
# Define uma semente para reproduzir resultados idênticos

🔹 Cálculo da Norma (Erro Numérico)
norma = np.array([])
np.random.seed(84)
coef_angulares = np.random.uniform(low=0.10, high=0.90, size=100)

for i in range(100):
    norma = np.append(norma, np.linalg.norm(Moscow - (coef_angulares[i] * X + b)))


np.linalg.norm() → calcula a distância (norma) entre dois vetores.

Serve para medir o erro entre valores reais e valores previstos.

🔹 Funções NumPy Mais Usadas
np.arange()        # Cria sequência numérica
np.loadtxt()       # Lê dados de arquivo texto/CSV
np.mean()          # Média dos valores
np.isnan()         # Detecta valores NaN
np.allclose()      # Compara arrays com tolerância
np.array_equal()   # Verifica se arrays são idênticos
np.sqrt()          # Raiz quadrada
np.power()         # Potenciação (x^y)
np.append()        # Adiciona elementos a um array
np.random.uniform()# Gera valores aleatórios uniformemente distribuídos
np.linalg.norm()   # Calcula norma/vetor (erro numérico)

📊 Visualização com Matplotlib
plt.plot(x, y)        # Plota gráfico de linha
plt.bar(x, y)         # Plota gráfico de barras
plt.legend()          # Adiciona legenda
plt.xlabel('Eixo X')  # Nomeia eixo X
plt.ylabel('Eixo Y')  # Nomeia eixo Y
plt.title('Gráfico')  # Define título
plt.show()            # Exibe o gráfico

✅ Resumo Conceitual

NumPy é usado para operações matemáticas vetorizadas e análise numérica rápida.

Arrays NumPy são mais eficientes que listas Python comuns.

Vetorização permite operar sobre todos os elementos de um array sem loops explícitos.

Matplotlib complementa o NumPy permitindo a visualização gráfica dos resultados.

O modelo de regressão linear (y = a·x + b) é uma aplicação clássica para previsão numérica.