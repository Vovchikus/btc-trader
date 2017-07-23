from components.btc.trade_api import BtcTradeApi
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

from components.btc.public_api import BtcPublicApi
from components.converter.currency_pairs import CurrencyPairsConverter

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def info():
    api = BtcPublicApi()
    inf = api.info()
    conv = CurrencyPairsConverter()
    pairs = {}

    for item in inf['pairs']:
        pairs[item] = conv.code_pairs_to_readable(item)

    return render_template('main.html', result=pairs)


@app.route('/pair')
def pair():
    api = BtcPublicApi()
    ticker_pair = api.ticker_pair(request.args.get('currency'))
    return render_template('ticker_pair.html', pair=ticker_pair)


@app.route('/personal')
def personal():
    api = BtcTradeApi()
    personal_info = api.get_info()
    return render_template('personal_info.html', personal_info=personal_info)


@app.route('/convert')
def convert():
    api = BtcPublicApi()
    rur_pair = request.args.get('pair') + '_rur'
    result = api.ticker_pair(rur_pair)
    sell_price = float(result[rur_pair]['sell'])
    sell_value = float(request.args.get('val'))
    return render_template('rur_pair.html', r=sell_price * sell_value)


@app.route('/trade_history')
def trade_history():
    api = BtcTradeApi()
    history = api.trade_history()
    return render_template('trade_history.html', history=history)


@app.route('/transaction_history')
def transaction_history():
    api = BtcTradeApi()
    transactions = api.transaction_history()
    return render_template('transaction_history.html', transactions=transactions)


if __name__ == '__main__':
    app.run(debug=True)
