class CurrencyPairsConverter:
    def __init__(self):
        pass

    @staticmethod
    def convert(pair):
        pairs = {
            'eth_rur': 'Ethereum - Ruble',
            'btc_rur': 'Bitcoin - Ruble',
            'dsh_rur': 'Dash - Ruble',
            'ltc_rur': 'Litecoin - Ruble'
        }
        return pairs[pair]
