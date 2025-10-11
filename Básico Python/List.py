# Lista
notas_turma = [
    'João', 8.0, 9.0, 10.0,
    'Maria', 9.0, 7.0, 6.0,
    'José', 3.4, 7.0, 7.0,
    'Cláudia', 5.5, 6.6, 8.0,
    'Ana', 6.0, 10.0, 9.5
]

nomes = []
notas_juntas = []

# --- Separa nomes e notas ---
for i in range(len(notas_turma)):
    if i % 4 == 0:  # a cada 4 elementos há um nome, cada elemento 0 é nome
        nomes.append(notas_turma[i])
    else:
        notas_juntas.append(notas_turma[i])

print("Nomes:", nomes)
print("Notas juntas:", notas_juntas)

# --- Agrupa as notas de 3 em 3 (cada aluno tem 3 notas) ---
notas_de_cada_aluno = []
for i in range(0, len(notas_juntas), 3):
    notas_de_cada_aluno.append([
        notas_juntas[i],
        notas_juntas[i+1],
        notas_juntas[i+2]
    ]) # Percorre 3 elementos até o limite e separa em SubLista dentro da Lista Principal

print("Notas de cada aluno:", notas_de_cada_aluno)

# --- Calcula a média de cada aluno ---
medias = []
for notas in notas_de_cada_aluno: # Pega os valores da Lista formatada considerando o Limite das Sublistas assim identificando quantos grupos de SubListas tem e fazendo a média de cada
    media = sum(notas) / len(notas)
    medias.append(media)

print("Médias:", medias)

# --- Mostra tudo junto ---
for i in range(len(nomes)):
    print(f"{nomes[i]} → Notas: {notas_de_cada_aluno[i]} → Média: {medias[i]:.2f}") # Formatação Final da qual após A busca por todos os alunos e notas e criando as médias dos alunos retorna