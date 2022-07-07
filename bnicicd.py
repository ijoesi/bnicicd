import requests
from datetime import datetime

print ("Hello world")
print ("Testing CI/CD BNI")

response = requests.get("https://www.google.com")
waktu = datetime.now()

with open("tempResponse/" + str(waktu) + ".txt", "w") as f:
    f.write(response.text)