media = 6
match media:
        case media if media < 5:
            print('Você foi reprovado')
        case media if 5 <= media < 7:
            print('Fará Recuperação')
        case media if media >= 7:
          print('Você foi Aprovado')

        #   forma 3.10 do python de se fazer if e else