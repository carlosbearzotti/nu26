nomes = ['João', 'Maria', 'José', 'Cláudia', 'Ana']
notas_de_cada_aluno = [
  [8.0, 9.0, 10.0],
  [9.0, 7.0, 6.0],
  [3.4, 7.0, 7.0],
  [5.5, 6.6, 8.0],
  [6.0, 10.0, 9.5]
]
turma = {
    nome: {
        "notas": notas,
        "media": round(sum(notas) / len(notas), 2)
    }
    for nome, notas in zip(nomes, notas_de_cada_aluno)
}
for nome, dados in turma.items():
    print(f"{nome} → Notas: {dados['notas']} → Média: {dados['media']}")