# ====================================================
# EXEMPLOS DE TRATAMENTO DE EXCEÇÕES EM PYTHON
# ====================================================

# =========================================
# Exemplo 1: Tratando exceções genéricas
# =========================================

try:
    numero_1 = float(input("Digite o primeiro número: "))
    numero_2 = float(input("Digite o segundo número: "))
    divisao = numero_1 / numero_2
except Exception as e:
    print(type(e), f'Erro: {e}')

# =========================================
# Exemplo 2: Tratando exceção específica (KeyError)
# =========================================

idades = {"Ana": 25, "Carlos": 30, "Mariana": 22}

try:
    chave = input("Digite o nome para buscar a idade: ")
    valor = idades[chave]
except KeyError:
    print('Nome não encontrado')
else:
    print(valor)

# =========================================
# Exemplo 3: Uso de try-except-else-finally em função
# =========================================

def converte_lista(lista):
    """Converte todos os elementos de uma lista em float."""
    try:
        nova_lista = [float(elemento) for elemento in lista]
    except Exception as e:
        print(type(e), f'Erro: {e}')
    else:
        return nova_lista
    finally:
        print('Fim da execução da função')

# =========================================
# Exemplo 4: Lançando exceções manualmente (raise)
# =========================================

def soma_listas(lista1, lista2):
    """Soma os elementos de duas listas posição a posição."""
    try:
        if len(lista1) == len(lista2):
            dados = [(lista1[i], lista2[i], lista1[i] + lista2[i]) for i in range(len(lista1))]
        else:
            raise IndexError('A quantidade de elementos em cada lista é diferente.')
    except Exception as e:
        print(type(e), f'Erro: {e}')
    else:
        return dados  

# =========================================
# Exemplo 5: Função corretora de provas com ValueError
# =========================================

gabarito = ['D', 'A', 'B', 'C', 'A']

def corretor(testes: list):
    """
    Recebe uma lista de listas com respostas de estudantes e retorna as pontuações.
    Lança exceção se alguma resposta for inválida.
    """
    pontuacoes = []
    try:
        for teste in testes:
            nota = 0
            for i in range(len(teste)):
                if teste[i] not in ['A', 'B', 'C', 'D']:
                    raise ValueError(f'A alternativa {teste[i]} não é válida.')
                elif teste[i] == gabarito[i]:
                    nota += 1
            pontuacoes.append(nota)
    except Exception as e:
        print(e)
    else:
        return pontuacoes

# Testando casos
testes_sem_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]
print(corretor(testes_sem_ex))

testes_com_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]
print(corretor(testes_com_ex))

# =========================================
# Exemplo 6: Função que valida texto (tratando pontuação)
# =========================================

def avalia_texto(texto: list):
    """
    Verifica se o texto contém pontuação indesejada.
    Lança exceção caso encontre vírgulas, pontos, exclamações ou interrogações.
    """
    for palavra in texto:
        if any(p in palavra for p in [',', '.', '!', '?']):
            raise ValueError(f'O texto apresenta pontuações na palavra "{palavra}".')
    return "Texto já tratado!"

# Testando texto sem exceção
lista_tratada = [
    'Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa', 'versátil',
    'e', 'fácil', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos', 'desde',
    'análise', 'de', 'dados', 'até', 'inteligência', 'artificial'
]

try:
    avaliacao = avalia_texto(lista_tratada)
except Exception as e:
    print(e)
else:
    print(avaliacao)

# Testando texto com exceção
lista_nao_tratada = [
    'Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa,', 'versátil',
    'e', 'fácil,', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos,', 'desde',
    'análise', 'de', 'dados', 'até', 'inteligência', 'artificial!'
]

try:
    avaliacao = avalia_texto(lista_nao_tratada)
except Exception as e:
    print(e)
else:
    print(avaliacao)

# =========================================
# Exemplo 7: Tratando múltiplas exceções (ValueError e ZeroDivisionError)
# =========================================

def divide_colunas(lista_1: list, lista_2: list) -> list:
    """
    Divide os elementos de duas listas par a par.
    Lança exceção se o tamanho das listas for diferente ou se houver divisão por zero.
    """
    try:
        if len(lista_1) != len(lista_2):
            raise ValueError("As listas precisam ter o mesmo tamanho")

        resultado = [round(a / b, 2) for a, b in zip(lista_1, lista_2)]
    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(f"{e}: A 2ª lista não pode possuir um valor igual a 0")
    else:
        return resultado

# Testes
pressoes = [100, 120, 140, 160, 180]
temperaturas = [20, 25, 30, 35, 40]
print(divide_colunas(pressoes, temperaturas))  # Ok

pressoes = [60, 120, 140, 160, 180]
temperaturas = [0, 25, 30, 35, 40]
print(divide_colunas(pressoes, temperaturas))  # ZeroDivisionError

pressoes = [100, 120, 140, 160]
temperaturas = [20, 25, 30, 35, 40]
print(divide_colunas(pressoes, temperaturas))  # ValueError
