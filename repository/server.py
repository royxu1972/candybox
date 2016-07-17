import requests
import json

path = "http://localhost:3900/action"
r = requests.post(path + "/allData")
data = json.loads(r.text)
print(data)

# Writing JSON data
#with open('data.json', 'w') as f:
#    json.dump(data, f)

#with open('data.json', 'r') as f:
#    d = json.load(f)
#    print(d[20])

