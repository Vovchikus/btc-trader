class CurrencyPairsConverter:
    PPC = 'ppc'
    USD = 'usd'
    ETH = 'eth'
    RUR = 'rur'
    BTC = 'btc'
    DSH = 'dsh'
    LTC = 'ltc'
    NMC = 'nmc'
    EUR = 'eur'
    CODES = [PPC, USD, ETH, RUR, BTC, DSH, LTC, NMC, EUR]
    ASSOC = {
        PPC: 'Peercoin',
        USD: 'US Dollar',
        ETH: 'Ethereum',
        RUR: 'Ruble',
        BTC: 'Bitcoin',
        DSH: 'Dash',
        LTC: 'Litecoin',
        NMC: 'Namecoin',
        EUR: 'Euro',
    }

    def __init__(self):
        pass

    @staticmethod
    def build_pair(left, right):
        return left + '_' + right

    def readable(self, code):
        return self.ASSOC[code]

    def code_pairs_to_readable(self, code_pair):
        chunks = code_pair.split('_')
        if chunks[0] in self.CODES and chunks[1] in self.CODES:
            first = self.readable(chunks[0])
            second = self.readable(chunks[1])
            return first + ' - ' + second
