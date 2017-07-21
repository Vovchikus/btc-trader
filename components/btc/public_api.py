import httplib
import json

from components.btc.btc import BtcApi


class BtcPublicApi:
    API_SLUG = '/api/3'

    def __init__(self):
        pass

    def __api_call(self, params_slug):
        conn = httplib.HTTPSConnection(BtcApi.BTC_DOMAIN)
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
