import csv
import random

# Definir nomes de colunas
colunas = [
    "id_transacao", "valor", "horario", "localizacao",
    "tipo_pagamento", "tempo_conta", "qtd_transacoes_dia", "fraude"
]

# Valores possíveis para campos categóricos
locais = ["SP", "RJ", "MG", "BA", "RS", "PR"]
pagamentos = ["cartao", "pix", "boleto"]

# Criar o dataset fictício
with open("transacoes.csv", "w", newline="", encoding="utf-8") as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(colunas)

    for i in range(1, 1001):  # 1000 linhas
        valor = round(random.uniform(10, 5000), 2)
        horario = random.randint(0, 23)
        localizacao = random.choice(locais)
        tipo_pagamento = random.choice(pagamentos)
        tempo_conta = random.randint(1, 120)
        qtd_transacoes_dia = random.randint(1, 20)

        # Lógica simples para simular fraude:
        # Fraude mais provável em valores altos, horários noturnos e contas novas
        prob_fraude = 0.02
        if valor > 3000:
            prob_fraude += 0.10
        if horario >= 22 or horario <= 5:
            prob_fraude += 0.05
        if tempo_conta < 6:
            prob_fraude += 0.05

        fraude = 1 if random.random() < prob_fraude else 0

        writer.writerow([
            i, valor, horario, localizacao,
            tipo_pagamento, tempo_conta,
            qtd_transacoes_dia, fraude
        ])

print("✅ Arquivo 'transacoes.csv' criado com sucesso!")