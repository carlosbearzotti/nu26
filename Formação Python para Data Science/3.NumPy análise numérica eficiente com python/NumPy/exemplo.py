import numpy as np

# Exemplo prático integrando vários conceitos
# Simulando dados de temperatura de 3 cidades por 5 dias

# Dados fictícios de temperatura (3 cidades × 5 dias)
temperaturas = np.array([
    [25, 26, 24, 23, 27],  # Cidade A
    [30, 29, 31, 28, 32],  # Cidade B  
    [18, 19, 17, 16, 20]   # Cidade C
])

print("Temperaturas das cidades (3×5):")
print(temperaturas)

# Estatísticas por cidade
medias_cidades = np.mean(temperaturas, axis=1)
max_cidades = np.max(temperaturas, axis=1)
min_cidades = np.min(temperaturas, axis=1)

print(f"\nMédias por cidade: {medias_cidades}")
print(f"Máximas por cidade: {max_cidades}")
print(f"Mínimas por cidade: {min_cidades}")

# Aplicando correção (broadcasting)
correcao = np.array([-1, 0, 1])  # Correção diferente para cada cidade
temperaturas_corrigidas = temperaturas + correcao.reshape(3, 1)

print("\nTemperaturas corrigidas:")
print(temperaturas_corrigidas)

# Encontrando dias com temperatura acima de 25°C
dias_quentes = temperaturas > 25
print("\nDias com temperatura > 25°C:")
print(dias_quentes)