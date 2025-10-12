# Transforma Lista em Dicionário
nomes = ['João', 'Maria', 'José', 'Cláudia', 'Ana']
notas_de_cada_aluno = [
  [8.0, 9.0, 10.0],
  [9.0, 7.0, 6.0],
  [3.4, 7.0, 7.0],
  [5.5, 6.6, 8.0],
  [6.0, 10.0, 9.5]
]

# Criando um dicionário de alunos
turma = {}

for i in range(len(nomes)):
    media = sum(notas_de_cada_aluno[i]) / len(notas_de_cada_aluno[i])
    turma[nomes[i]] = {
        "notas": notas_de_cada_aluno[i],
        "media": round(media, 2)
    }

print(turma)
# {
#   'João': {'notas': [8.0, 9.0, 10.0], 'media': 9.0},
#   'Maria': {'notas': [9.0, 7.0, 6.0], 'media': 7.33},
#   'José': {'notas': [3.4, 7.0, 7.0], 'media': 5.8},
#   'Cláudia': {'notas': [5.5, 6.6, 8.0], 'media': 6.7},
#   'Ana': {'notas': [6.0, 10.0, 9.5], 'media': 8.5}
# }

# Modelo comprehension 

for nome, dados in turma.items():
    print(f"{nome} → Notas: {dados['notas']} → Média: {dados['media']}")

# {
#   'João': {'notas': [8.0, 9.0, 10.0], 'media': 9.0},
#   'Maria': {'notas': [9.0, 7.0, 6.0], 'media': 7.33},
#   'José': {'notas': [3.4, 7.0, 7.0], 'media': 5.8},
#   'Cláudia': {'notas': [5.5, 6.6, 8.0], 'media': 6.7},
#   'Ana': {'notas': [6.0, 10.0, 9.5], 'media': 8.5}
# }
