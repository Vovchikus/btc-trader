from flask import Flask, render_template, request
from components.btc_public_api import BtcPublicApi
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def info():
    api = BtcPublicApi()
    get_info = api.info()
    return render_template("main.html", info=get_info)


@app.route('/pair')
def pair():
    api = BtcPublicApi()
    ticker_pair = api.ticker_pair(request.args.get('currency'))
    return render_template('ticker_pair.html', pair=ticker_pair)


if __name__ == '__main__':
    app.run(debug=True)
