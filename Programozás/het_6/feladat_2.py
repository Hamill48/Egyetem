def currencyExchangeForint(forint, currency):
    result = 0
    if currency == 'chf':
        result = forint / 406.42
    elif currency == 'eur':
        result = forint / 386.77
    elif currency == 'usd':
        result = forint / 366.92
    return result

def currencyExchange(money, currentCurrency, changedCurrency):
    result = 0
    resultInFt = 0

    if currentCurrency == 'chf' and changedCurrency == 'eur':
        result = money * (406.42 / 386.77)
        resultInFt = result * 386.77
    elif currentCurrency == 'chf' and changedCurrency == 'usd':
        result = money * (406.42 / 366.92)
        resultInFt = result * 366.92
    elif currentCurrency == 'chf' and changedCurrency == 'huf':
        result = money * 406.42
        resultInFt = result
    elif currentCurrency == 'chf' and changedCurrency == 'chf':
        result = money
        resultInFt = result * 406.42
    
    if currentCurrency == 'eur' and changedCurrency == 'chf':
        result = money * (386.77 / 406.42)
        resultInFt = result * 406.42
    elif currentCurrency == 'eur' and changedCurrency == 'usd':
        result = money * (386.77 / 366.92)
        resultInFt = result * 366.92
    elif currentCurrency == 'eur' and changedCurrency == 'huf':
        result = money * 386.77
        resultInFt = result
    elif currentCurrency == 'eur' and changedCurrency == 'eur':
        result = money
        resultInFt = result * 386.77
    
    if currentCurrency == 'usd' and changedCurrency == 'chf':
        result = money * (366.92 / 406.42)
        resultInFt = result * 406.42
    elif currentCurrency == 'usd' and changedCurrency == 'eur':
        result = money * (366.92 / 386.77)
        resultInFt = result * 386.77
    elif currentCurrency == 'usd' and changedCurrency == 'huf':
        result = money * 366.92
        resultInFt = result
    elif currentCurrency == 'usd' and changedCurrency == 'usd':
        result = money
        resultInFt = result * 366.92

    if currentCurrency == 'huf' and changedCurrency == 'chf':
        result = money / 406.42
        resultInFt = result
    elif currentCurrency == 'huf' and changedCurrency == 'eur':
        result = money / 386.77
        resultInFt = result
    elif currentCurrency == 'huf' and changedCurrency == 'usd':
        result = money / 366.92
        resultInFt = result
    elif currentCurrency == 'huf' and changedCurrency == 'huf':
        result = money
        resultInFt = result
    
    return f'Your changed money: {result}', f'Your changed money in HUF: {resultInFt}'

print('Your changed money:', currencyExchange(100, 'usd', 'huf'))