try:
    numero_1 = float(input())
    numero_2 = float(input())
    divisao = numero_1 / numero_2
except Exception as e:
    print(type(e), f'Erro: {e}')

try:
    chave = input()
    valor = idades[chave]
except KeyError:
    print('Nome não encontrado')
else:
    print(valor)

def converte_lista(lista):
    try:
        nova_lista = [float(elemento) for elemento in lista]
    except Exception as e:
        print(type(e), f'Erro: {e}')
    else:
        return nova_lista
    finally:
        print('Fim da execução da função')

def soma_listas(lista1, lista2):
    try:
        if len(lista1) == len(lista2):
            dados = [(lista1[i], lista2[i], lista1[i]+lista2[i]) for i in range(len(lista1))]
        else:
            raise IndexError('A quantidade de elementos em cada lista é diferente.')
    except Exception as e:
        print(type(e), f'Erro: {e}')
    else:
        return dados  
    
gabarito = ['D', 'A', 'B', 'C', 'A']

# Criando a função que recebe a lista de listas com as notas dos estudantes
def corretor(testes: list):
  pontuacoes = [] # criando a lista que receberá as pontuações caso a exceção não seja lançada
  try:
    for teste in testes:
      nota = 0 # variável que acumula a nota de cada estudante
      for i in range(len(teste)):
        if teste[i] not in ['A', 'B', 'C', 'D']: # Verificamos se temos uma alternativa valida
          raise ValueError(f'A alternativa {teste[i]} não é uma opção de alternativa válida')
        elif teste[i] == gabarito[i]: # Verificamos se as respostas são iguais e adicionamos à nota
          nota += 1
      pontuacoes.append(nota) # adicionamos a nota do(a) estudante na lista de pontuações
  except Exception as e:
    print(e)
  else:
    return pontuacoes # retornando a lista de pontuações se não lançarmos a exceção
  
# Testando no exemplo que não lança exceção
testes_sem_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]
corretor(testes_sem_ex)

# Testando no exemplo que lança exceção
testes_com_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]
corretor(testes_com_ex)

# criando a função que recebe a lista de palavras
def avalia_texto(texto: list):
    for palavra in texto:
        if ',' in palavra or '.' in palavra or '!' in palavra or '?' in palavra:
            raise ValueError(f'O texto apresenta pontuações na palavra "{palavra}".')
    return "Texto já tratado!" # retornando a verificação se não lançada a exceção 

# Testando no exemplo que não lança exceção
lista_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa', 'versátil',
                  'e', 'fácil', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos', 'desde',
                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial']

try:
  avaliacao = avalia_texto(lista_tratada)
except Exception as e:
  print(e)
else:
  print(avaliacao)

# Testando no exemplo que lança exceção
lista_nao_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa,', 'versátil',
                  'e', 'fácil,', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos,', 'desde',
                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial!']

try:
  avaliacao = avalia_texto(lista_nao_tratada)
except Exception as e:
  print(e)
else:
  print(avaliacao)

# criando a função que recebe as duas listas e a operação a ser realizada
def divide_colunas(lista_1: list, lista_2: list) -> list:
  # try-except que verifica se é possível calcular a divisão e lança exceção se as listas tem tamanhos diferentes
  # ou se temos alguma divisão por zero em um dos cálculos entre os números das listas
  try:
    if len(lista_1) != len(lista_2): # Verificando se as listas tem o mesmo tamanho, se não lança uma exceção
      raise ValueError("As listas precisam ter o mesmo tamanho")

    # A função zip pareia os elementos das listas e uma lista é gerada por meio da razão entre os pares
    resultado = [round(a / b, 2) for a, b in zip(lista_1, lista_2)] 
  except ValueError as e:
    print(e)
  except ZeroDivisionError as e:
    print(f"{e}: A 2ª lista não pode possuir um valor igual a 0")
  else:
    return resultado
  
# Testando no exemplo que não lança exceção
pressoes = [100, 120, 140, 160, 180]
temperaturas = [20, 25, 30, 35, 40]

divide_colunas(pressoes, temperaturas)

# Testando no exemplo que lança exceção (ZeroDivisionError)
pressoes = [60, 120, 140, 160, 180]
temperaturas = [0, 25, 30, 35, 40]

divide_colunas(pressoes, temperaturas)

# Testando no exemplo que lança exceção (ValueError)
pressoes = [100, 120, 140, 160]
temperaturas = [20, 25, 30, 35, 40]

divide_colunas(pressoes, temperaturas)