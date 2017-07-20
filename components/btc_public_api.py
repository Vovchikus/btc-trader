import httplib
import json
import urllib


class BtcPublicApi:
    BTC_DOMAIN = 'btc-e.nz'
    API_SLUG = '/api/3'

    def __init__(self):
        pass

    def __api_call(self, params_slug):
        conn = httplib.HTTPSConnection(self.BTC_DOMAIN)
        conn.request('GET', self.API_SLUG + '/' + params_slug)
        response = conn.getresponse()
        data = json.load(response)
        conn.close()
        return data

    def info(self):
        return self.__api_call('info')

    def ticker_pair(self, pair):
        method_slug = 'ticker/' + pair
        return self.__api_call(method_slug)
