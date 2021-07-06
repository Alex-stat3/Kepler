from bs4 import BeautifulSoup
import pandas as pd

import requests
output = open("example.txt", "w", encoding="utf-8")
r = requests.get('https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=cumulative').text
output.write(r)
output.close()


df = pd.read_csv('example.txt')
df.to_csv('output.csv', sep=',')

