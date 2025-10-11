aluno = {
    "nome": "João",
    "idade": 17,
    "notas": [8.0, 9.5, 7.5],
    "aprovado": True
}

print(aluno["nome"])     # João
print(aluno["notas"])    # [8.0, 9.5, 7.5]

aluno["media"] = sum(aluno["notas"]) / len(aluno["notas"])

print(aluno)

for chave, valor in aluno.items():
    print(chave, "→", valor)

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
for nome, dados in turma.items():
    print(f"{nome} → Notas: {dados['notas']} → Média: {dados['media']}")