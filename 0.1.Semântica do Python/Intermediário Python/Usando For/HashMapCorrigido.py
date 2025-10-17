def countIncorrectPrices(products, productPrices, productSold, soldPrice):
    # Validação de entrada
    if not all([products, productPrices, productSold, soldPrice]):
        return 0
    
    if len(products) != len(productPrices):
        raise ValueError("Products and productPrices must have the same length")
    
    if len(productSold) != len(soldPrice):
        raise ValueError("productSold and soldPrice must have the same length")
    
    # Criar dicionário de preços corretos
    correct_prices = {}
    for i in range(len(products)):
        if products[i] is None or productPrices[i] is None:
            continue  # Pula entradas nulas
        correct_prices[products[i]] = productPrices[i]
    
    # Contar transações incorretas com precisão de 12 casas decimais
    incorrect_count = 0
    for i in range(len(productSold)):
        product = productSold[i]
        transaction_price = soldPrice[i]
        
        # Validação de dados nulos
        if product is None or transaction_price is None:
            incorrect_count += 1  # Considera transação com dados nulos como incorreta
            continue
        
        # Verifica se o produto existe no dicionário de preços
        if product not in correct_prices:
            incorrect_count += 1  # Produto não encontrado é considerado incorreto
            continue
        
        # Comparação com precisão de 12 casas decimais
        correct_price = correct_prices[product]
        
        # Usando round para evitar problemas de ponto flutuante
        if round(correct_price, 12) != round(transaction_price, 12):
            incorrect_count += 1
    
    return incorrect_count

# Teste com o exemplo original
products = ['ovos', 'leite', 'queijo', 'abacaxi']
productPrices = [2.89, 3.29, 5.79, 3.33]
productSold = ['ovos', 'ovos', 'queijo', 'leite']
soldPrice = [2.89, 2.99, 5.97, 3.29]

print(countIncorrectPrices(products, productPrices, productSold, soldPrice))  # Saída: 2

# Testes adicionais com casos extremos
print("\n=== Testes Adicionais ===")

# Teste com valores nulos
products2 = ['ovos', 'leite', None, 'queijo']
productPrices2 = [2.89, 3.29, 5.79, None]
productSold2 = ['ovos', None, 'queijo', 'leite']
soldPrice2 = [2.89, 2.99, None, 3.29]

print("Teste com nulos:", countIncorrectPrices(products2, productPrices2, productSold2, soldPrice2))

# Teste com precisão decimal
products3 = ['produto1', 'produto2']
productPrices3 = [1.000000000001, 2.000000000000]
productSold3 = ['produto1', 'produto2']
soldPrice3 = [1.000000000002, 2.000000000000]  # Diferença na 12ª casa decimal

print("Teste de precisão:", countIncorrectPrices(products3, productPrices3, productSold3, soldPrice3))

# Teste com diferença mínima
products4 = ['item']
productPrices4 = [0.123456789012]
productSold4 = ['item']
soldPrice4 = [0.123456789013]  # Diferença de 0.000000000001

print("Teste diferença mínima:", countIncorrectPrices(products4, productPrices4, productSold4, soldPrice4))