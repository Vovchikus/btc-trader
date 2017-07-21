import json


class BtcApi:
    BTC_DOMAIN = 'btc-e.nz'
    SETTINGS_FILE = 'api_settings.json'

    def __init__(self):
        pass

    def get_api_settings(self):
        try:
            with open(self.SETTINGS_FILE) as f:
                j = json.load(f)
        except IOError as e:
            print "Error: {0}".format(e.strerror)
        except TypeError:
            print "Error loading json from file"
        except ValueError:
            print "Broken json loaded"
        else:
            f.close()
            return j
