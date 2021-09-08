# import requests as rq

# print(rq.__version__)

import requests

r = requests.get('https://raw.githubusercontent.com/poulomi-g/CMPUT404/main/script.py')

print(r.text)