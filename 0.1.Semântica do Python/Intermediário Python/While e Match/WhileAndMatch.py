alunos = {}  # Dicionário para armazenar {nome: média}

while True:
    print("\n=== Menu de Notas ===")
    print("1 - Adicionar aluno")
    print("2 - Mostrar médias")
    print("3 - Sair")
    
    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            nome = input("Nome do aluno: ")
            notas = input("Notas separadas por espaço: ").split()
            notas = [float(n) for n in notas]
            media = sum(notas) / len(notas)
            alunos[nome] = round(media, 2)
            print(f"Aluno {nome} adicionado com média {alunos[nome]}")
        
        case "2":
            if alunos:
                print("Médias dos alunos:")
                for n, m in alunos.items():
                    print(f"{n}: {m}")
            else:
                print("Nenhum aluno cadastrado.")
        
        case "3":
            print("Saindo do programa...")
            break  # encerra o loop
        
        case _:
            print("Opção inválida. Tente novamente.")

# while → usado para repetir uma ação até que uma condição seja atendida (ou até o usuário decidir sair).
# match → usado para decidir o que fazer com base em diferentes valores ou padrões.