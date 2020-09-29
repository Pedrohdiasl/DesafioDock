import requests
import html2text
from datetime import datetime

req = requests.get('https://www.dan.me.uk/torlist/?exit').text
timegen = datetime.now().strftime("%d/%m/%Y-%I:%M:%S-%p")
doc = open("Lista_ips_"+timegen+".txt",'w')

with open (doc) as file:
    file.write(html2text.html2text(req))
