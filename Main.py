import requests

response = requests.get('http://192.168.1.154/api/Danboe2009')
print ("Response: {0}".format(response.content))
