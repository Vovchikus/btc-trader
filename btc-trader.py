from components.btc.trade_api import BtcTradeApi
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

from components.btc.public_api import BtcPublicApi

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def info():
    api = BtcPublicApi()
    get_info = api.info()
    return render_template('main.html', info=get_info)


@app.route('/pair')
def pair():
    api = BtcPublicApi()
    ticker_pair = api.ticker_pair(request.args.get('currency'))
    return render_template('ticker_pair.html', pair=ticker_pair)


@app.route('/personal')
def personal():
    api = BtcTradeApi()
    personal_info = api.get_info()
    return render_template("personal_info.html", personal_info=personal_info)


if __name__ == '__main__':
    app.run(debug=True)
