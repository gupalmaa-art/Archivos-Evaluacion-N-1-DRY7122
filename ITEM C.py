
pwd 
ls
ls -l datosjson.py

cd ~/labs/devnet-src/parsing
nano datosjson.py

import json

with open('myfile.json', 'r') as json_file:
    ourjson = json.load(json_file)

print("Token:", ourjson['access_token'])
print("Tiempo antes de caducar:", ourjson['expires_in'], "segundos")

python3 datosjson.py
