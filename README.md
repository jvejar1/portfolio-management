# portfolio-management

El código de este repo fue generado usando ChatGPT a través de la siguiente conversación: https://chatgpt.com/share/68fe68d8-d9ec-8007-8632-80f368506666
Al inicio no entendía bien como funciona el rebalanceo, pero con el chat pude resolver dudas y llegar a la solución.

## Ejemplo de Uso
```
# Define current portfolio
stocks = {
    "AAPL": Stock("AAPL", shares=10, current_price=190),
    "META": Stock("META", shares=5, current_price=350),
}

# Define target allocation: 60% AAPL, 40% META
target_alloc = {"AAPL": 0.6, "META": 0.4}

portfolio = Portfolio(stocks, target_alloc)

print("Total portfolio value:", portfolio.total_value())

actions = portfolio.rebalance()
for sym, data in actions.items():
    print(data["action"])
```

## Ejemplo de salida
```
Total portfolio value: 4150
Sell 1.46 shares of META
Buy 3.68 shares of AAPL
```
