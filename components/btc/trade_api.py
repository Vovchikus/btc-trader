import hashlib
import hmac
import httplib
import json
import urllib

import time

from components.btc.btc import BtcApi


class BtcTradeApi:
    API_SLUG = '/tapi'

    _api_settings = ''

    def __init__(self):
        api = BtcApi()
        self._api_settings = api.get_api_settings()

    def _get_headers(self, params):
        return {'Content-type': 'application/x-www-form-urlencoded',
                'Key': self._api_settings['apiKey'],
                'Sign': self._signature(params)}

    def _signature(self, params):
        return hmac.new(str(self._api_settings['apiSecret']), params, digestmod=hashlib.sha512).hexdigest()

    def _api_call(self, method, params):
        params['method'] = method
        params['nonce'] = str(time.time()).split('.')[0]
        params = urllib.urlencode(params)
        conn = httplib.HTTPSConnection(BtcApi.BTC_DOMAIN)
        conn.request('POST', self.API_SLUG, params, self._get_headers(params))
        response = conn.getresponse()
        data = json.load(response)
        conn.close()
        return data

    def get_info(self):
        return self._api_call('getInfo', {})

    def trade_history(self):
        return self._api_call('TradeHistory', {})

    def transaction_history(self):
        return self._api_call('TransHistory', {})
