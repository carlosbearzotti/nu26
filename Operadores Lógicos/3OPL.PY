x1 = x2 = True
y1 = y2 = False

if x1 and x2:
    print('True') # A tabela verdade do operador and nos mostra que a saída somente retorna Verdade (True) se ambos os operandos são Verdade. Caso contrário, retorna Falso (False)
else:
    print('False')

if x1 and y2:
    print('True')
else:
    print('False')

if x1 or y2:
    print('True') # A tabela verdade do operador or nos mostra que a saída somente retorna Falso (False) se ambos os operandos são Falsos, caso contrário, retorna Verdade (True). Ou seja, será retornado True se pelo menos um dos operandos for True
else:
    print('False')

if x1 or x2:
    print('True')
else:
    print('False')

if not x2:
    print('True') # O operador not tem uma tabela verdade menor, uma vez que ele apenas inverte o valor do operando. Se o operando for Verdadeiro
else:
    print('False')

if not y2:
    print('True')
else:
    print('False')