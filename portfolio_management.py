class Stock:
    def __init__(self, symbol, shares, current_price):
        self.symbol = symbol
        self.shares = shares
        self.current_price = current_price

    def value(self):
        """Return total market value of this stock."""
        return self.shares * self.current_price


class Portfolio:
    def __init__(self, stocks, target_allocation):
        """
        stocks: dict {symbol: Stock}
        target_allocation: dict {symbol: target_percentage (0-1)}
        """
        self.stocks = stocks
        self.target_allocation = target_allocation

    def total_value(self):
        return sum(stock.value() for stock in self.stocks.values())

    def rebalance(self):
        total = self.total_value()
        actions = {}

        for symbol, stock in self.stocks.items():
            current_value = stock.value()
            target_value = total * self.target_allocation.get(symbol, 0)

            diff = target_value - current_value
            shares_diff = diff / stock.current_price

            if abs(diff) < 1e-6:
                continue  # ignore tiny rounding errors

            if diff > 0:
                action = f"Buy {shares_diff:.2f} shares of {symbol}"
            else:
                action = f"Sell {abs(shares_diff):.2f} shares of {symbol}"

            actions[symbol] = {
                "current_value": current_value,
                "target_value": target_value,
                "difference": diff,
                "action": action
            }

        return actions