import requests

print ("Hello world")
print ("Testing CI/CD BNI")

response = requests.get("https://www.google.com")

print (response.text)