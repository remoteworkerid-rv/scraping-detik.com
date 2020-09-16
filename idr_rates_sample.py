import requests

# json_data = requests.get('http://www.floatrates.com/daily/idr.json')

json_data = {"usd":{"code":"USD","alphaCode":"USD","numericCode":"840","name":"U.S. Dollar","rate":6.7489735409818e-5,"date":"Wed, 16 Sep 2020 00:00:01 GMT","inverseRate":14817.068016754},
             "eur":{"code":"EUR","alphaCode":"EUR","numericCode":"978","name":"Euro","rate":5.6820238272191e-5,"date":"Wed, 16 Sep 2020 00:00:01 GMT","inverseRate":17599.363015861}}

# harus .values supaya bisa ambil data diatas
for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])