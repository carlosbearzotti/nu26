def countIncorrectPrices(products, productPrices, productSold, soldPrice):
    # Criar dicionário de preços corretos
    correct_prices = {}
    for i in range(len(products)):
        correct_prices[products[i]] = productPrices[i]
    
    # Contar transações incorretas
    incorrect_count = 0
    for i in range(len(productSold)):
        product = productSold[i]
        transaction_price = soldPrice[i]
        if correct_prices[product] != transaction_price:
            incorrect_count += 1
    
    return incorrect_count

products = ['ovos', 'leite', 'queijo', 'abacaxi']
productPrices = [2.89, 3.29, 5.79, 3.33]
productSold = ['ovos', 'ovos', 'queijo', 'leite']
soldPrice = [2.89, 2.99, 5.97, 3.29]

print(countIncorrectPrices(products, productPrices, productSold, soldPrice))

# Teste Técnico 1 Nubank 2026