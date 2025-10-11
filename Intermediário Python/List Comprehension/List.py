# Lista
notas_turma = [
    'João', 8.0, 9.0, 10.0,
    'Maria', 9.0, 7.0, 6.0,
    'José', 3.4, 7.0, 7.0,
    'Cláudia', 5.5, 6.6, 8.0,
    'Ana', 6.0, 10.0, 9.5
]

# Versão Otimizada da lista básica
nomes = [notas_turma[i] for i in range(0, len(notas_turma), 4)]
notas_juntas = [notas_turma[i] for i in range(len(notas_turma)) if i % 4 != 0]
notas_de_cada_aluno = [notas_juntas[i:i+3] for i in range(0, len(notas_juntas), 3)]
medias = [sum(notas)/3 for notas in notas_de_cada_aluno]
