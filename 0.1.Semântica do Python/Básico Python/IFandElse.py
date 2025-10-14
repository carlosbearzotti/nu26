NotasAluno = (7, 5, 6)

media = sum(NotasAluno) / len(NotasAluno)

if media > 6.5:
    print(media, 'Aprovado')
elif media > 5:
    print(media, 'Recuperação')
else:
    print(media, 'Reprovado')