def countIncorrectPrices(products, productPrices, productSold, soldPrice):
    # Validação de entrada
    if not all([products, productPrices, productSold, soldPrice]):
        return 0
    
    if len(products) != len(productPrices):
        raise ValueError("Products e productPrices tem que ter o mesmo tamanho")
    
    if len(productSold) != len(soldPrice):
        raise ValueError("productSold e soldPrice tem que ter o mesmo tamanho")
    
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

products = ['ovos', 'leite', 'queijo', 'abacaxi']
productPrices = [2.89, 3.29, 5.79, 3.33]
productSold = ['ovos', 'ovos', 'queijo', 'leite']
soldPrice = [2.89, 2.99, 5.97, 3.29]

print(countIncorrectPrices(products, productPrices, productSold, soldPrice))