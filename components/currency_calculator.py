class CurrencyCalculator:
    EQUALS = 1.00
    RESULT_UNDEFINED = -1.00

    _sell_price = 0.00
    _sell_value = 0.00

    def __init__(self, sell_price, value):
        self._sell_price = float(sell_price)
        self._sell_value = float(value)

    def calculate(self):
        return self._sell_price * self._sell_value
