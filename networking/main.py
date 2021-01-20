import urllib.request
import json

#response=urllib.request.urlopen("https://google.com")
#print(f"Result code is: {response.getcode()}")
#print(f"Data: {response.read()}")

response=urllib.request.urlopen("https://randomuser.me/api")
print(f"Result code is: {response.getcode()}")

if response.getcode()==200:
    #print(f"Data: {response.read()}")
    data=response.read()
    print(f"Data: {response.read()}")
    nativeObject=json.loads(data)
    print(nativeObject)
else:
    print("Error")
