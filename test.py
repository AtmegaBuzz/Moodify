import requests

url = "https://shazam.p.rapidapi.com/search"

querystring = {"term":"kiss the rain","locale":"en-US","offset":"0","limit":"5"}

headers = {
    'x-rapidapi-host': "shazam.p.rapidapi.com",
    'x-rapidapi-key': "df854d7e2dmshc942aed14451dfdp1ed725jsn8e8d2e16f58b"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)