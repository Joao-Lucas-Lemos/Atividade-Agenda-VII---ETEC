# Inicialização dos contadores
qtd_excelente = 0
qtd_ruim = 0

# Total de entrevistados (ajustado para 10 para testes rápidos, mude para 50 se necessário)
total_entrevistados = 10

print("=== PESQUISA DE OPINIÃO - TUDOWEB ===")
print(f"Iniciando a pesquisa com {total_entrevistados} entrevistados.\n")

# Estrutura de repetição FOR
for i in range(1, total_entrevistados + 1):
    print(f"--- Entrevistado {i} ---")
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    
    # Validação simples para garantir que a opção é válida
    opiniao = int(input("Informe a opinião sobre o atendimento:\n[1] EXCELENTE\n[2] BOM\n[3] RUIM\nDigite a opção (1, 2 ou 3): "))
    
    # Estrutura de decisão para verificar a opinião
    if opiniao == 1:
        qtd_excelente += 1
    elif opiniao == 3:
        qtd_ruim += 1
    elif opiniao == 2:
        # Apenas para tratar o BOM (caso não precise contar, o programa apenas segue)
        pass
    else:
        print("Opção inválida! Esta resposta não será contabilizada nas estatísticas principais.")
    
    print("-" * 30)

# Exibição dos resultados finais
print("\n" + "="*40)
print(" RESULTADO FINAL DA PESQUISA ")
print("="*40)
print(f"a) Quantidade de respostas 'EXCELENTE': {qtd_excelente}")
print(f"b) Quantidade de respostas 'RUIM': {qtd_ruim}")
print("="*40)