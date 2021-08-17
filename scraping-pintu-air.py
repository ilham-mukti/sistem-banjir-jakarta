import time
import json
import requests
import pandas as pd
from urllib.parse import urlencode
import csv
import os.path

class ScrapingPintuAir:
    def __init__(self):
        pass
        
    def request_data(self, url, header=None, param=None, json_param=None):
        response = requests.get(url, headers=header, params=param).json()
        df = pd.json_normalize(response[json_param], sep='_')
        return df

    def data_pintu_air(self):
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
        self.df_pintu_air = self.request_data("https://sisteminformasibanjir.jakarta.go.id/api/report/pintuAirReports/2021-08-17", headers, params, json_param='data')
        return self.df_pintu_air

    def data_lat_long(self):
        ambil_data = self.request_data("https://sisteminformasibanjir.jakarta.go.id/map_master/pintu_air", json_param='features')
        self.df_lat_long = ambil_data[['properties_pintu_air_id', 'geometry_coordinates']]
        return self.df_lat_long

    def add(self, x):
        sorted = self.df_lat_long[self.df_lat_long.properties_pintu_air_id == x]
        geometry = sorted['geometry_coordinates'].index[0]
        return sorted['geometry_coordinates'][geometry]

    def gabungan(self):
        df_gabungan = self.df_pintu_air.copy()
        df_gabungan['lat_long'] = df_gabungan.pintu_air_id.apply(self.add)
        return df_gabungan  

scrape = ScrapingPintuAir()
scrape.data_pintu_air()
scrape.data_lat_long()
scrape.gabungan()
