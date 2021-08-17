import time
import json
import requests
import pandas as pd
from urllib.parse import urlencode
import csv
import os.path


headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '^\\^Chromium^\\^;v=^\\^92^\\^, ^\\^',
    'Accept': 'application/json, text/plain, */*',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'token': 'T4EgIr1xIwsy7vr9UiAY64L61HWlDVN4V6qE3cc7OCvGzEg4hqhiagqatihAFgGB',
    'Origin': 'https://pantaubanjir.jakarta.go.id',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://pantaubanjir.jakarta.go.id/',
    'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
}

params = (
    ('format', 'json'),
)

response = requests.get('https://sisteminformasibanjir.jakarta.go.id/api/report/pintuAirReports/2021-08-17', headers=headers, params=params)
response.json()