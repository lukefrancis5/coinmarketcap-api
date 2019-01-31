import json
import requests
from datetime import datetime

global_url = 'https://api.coinmarketcap.com/v2/global'

request = requests.get(global_url)
results = request.json()

# print(json.dumps(results, sort_keys = True, indent = 4))

active_currencies = results['data']['active_cryptocurrencies']
active_markets = results['data']['active_markets']
bitcoin_percentage = results['data']['bitcoin_percentage_of_market_cap']
last_updated = results['data']['last_updated']
global_cap = int(results['data']['quotes']['USD']['total_market_cap'])
global_volume = int(results['data']['quotes']['USD']['total_volume_24h'])


active_currencies_str = '{:,}'.format(active_currencies)
active_markets_str = '{:,}'.format(active_markets)
global_cap_str = '{:,}'.format(global_cap)
global_volume_str = '{:,}'.format(global_volume)

last_updated_str = datetime.fromtimestamp(last_updated).strftime('%B %d, %Y at %I:%M%p')


print()
print('There are ' + active_currencies_str + ' active crypto currencies and ' + active_markets_str + ' active markets.')
print('The global cap of all cryptocurrencies is ' + global_cap_str + ' and the 24h global volume is ' + global_volume_str + '.')
print('Bitcoin\'s percentage of the global cap is ' + str(bitcoin_percentage) + '%.')
print('This information was last updated on ' + str(last_updated) + '.')