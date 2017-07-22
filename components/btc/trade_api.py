import hashlib
import hmac
import httplib
import json
import urllib

import time

from components.btc.btc import BtcApi


class BtcTradeApi:
    API_SLUG = '/tapi'

    __api_settings = ''

    def __init__(self):
        api = BtcApi()
        self.__api_settings = api.get_api_settings()

    def __get_headers(self, params):
        return {'Content-type': 'application/x-www-form-urlencoded',
                'Key': self.__api_settings['apiKey'],
                'Sign': self.__signature(params)}

    def __signature(self, params):
        return hmac.new(str(self.__api_settings['apiSecret']), params, digestmod=hashlib.sha512).hexdigest()

    def __api_call(self, method, params):
        params['method'] = method
        params['nonce'] = str(time.time()).split('.')[0]
        params = urllib.urlencode(params)
        conn = httplib.HTTPSConnection(BtcApi.BTC_DOMAIN)
        conn.request('POST', self.API_SLUG, params, self.__get_headers(params))
        response = conn.getresponse()
        data = json.load(response)
        conn.close()
        return data

    def get_info(self):
        return self.__api_call('getInfo', {})

    def trade_history(self):
        return self.__api_call('TradeHistory', {})

    def transaction_history(self):
        return self.__api_call('TransHistory', {})
