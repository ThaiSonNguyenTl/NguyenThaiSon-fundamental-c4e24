from urllib.request import urlopen
import json

url = "https://wind.waqi.info/nsearch/full/hanoi?n=4&fbclid=IwAR2D1Ysxqhjluw9n7M69lCRwweyPtgfvpWt1hCxLnKdpgQyUgm_EpQHimJs"
#1. open connection
conn = urlopen(url)
#2. read data
raw_data = conn.read()
#3.decode data
text = raw_data.decode("utf-8")
# print(type(text))
#4. 
data = json.loads(text)
# print(type(data))
print(data["dt"])
print(data)
results = data["results"]
# print(results)
result = results[0]
print(result["s"],["a"])
result = results[1]
print(result["n"])

