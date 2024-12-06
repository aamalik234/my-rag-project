import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
data = {
  "question": "How can I request a refill for my prescription at Lamna Healthcare?",
  "chat_history": []
}


body = str.encode(json.dumps(data))

url = 'https://rag-1359-endpoint.eastus2.inference.ml.azure.com/score'
# Replace this with the primary/secondary key, AMLToken, or Microsoft Entra ID token for the endpoint
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Inp4ZWcyV09OcFRrd041R21lWWN1VGR0QzZKMCIsImtpZCI6Inp4ZWcyV09OcFRrd041R21lWWN1VGR0QzZKMCJ9.eyJhdWQiOiJodHRwczovL21sLmF6dXJlLmNvbSIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzE2YjNjMDEzLWQzMDAtNDY4ZC1hYzY0LTdlZGEwODIwYjZkMy8iLCJpYXQiOjE3MzM1MTA3NDYsIm5iZiI6MTczMzUxMDc0NiwiZXhwIjoxNzMzNTE1ODAyLCJhY3IiOiIxIiwiYWlvIjoiQWFRQVcvOFlBQUFBTDVtd2pwcFBvbSswMHFKZ3lXMmVKTU01TjlOMTFVYWVNTU9YNFdWbkptTU1zZHh0VWRROEpSTFBMbUVIT3B4MDdZS2RQZUMxTU5VbHlIUUV1eE5pdnQ0YmN2SUgydWpzbE5naXRodHkxbTEzcUNzMVdZSzFvYUsxM2NYd09wYVZsT0p1VmMxcXdHMVprRUoyYzJZb2dYTmZNSzA5T0haTEJZdzAyeUZFT1JFRjRKSjI5UFBZSloxdUJzeUFobldUSXBqLzNURzF1SzVOUlVGZG5NZk1Gdz09IiwiYWx0c2VjaWQiOiI1OjoxMDAzMjAwMDNDMTUwM0I4IiwiYW1yIjpbImZpZG8iLCJyc2EiLCJtZmEiXSwiYXBwaWQiOiJjYjJmZjg2My03ZjMwLTRjZWQtYWI4OS1hMDAxOTRiY2Y2ZDkiLCJhcHBpZGFjciI6IjAiLCJkZXZpY2VpZCI6Ijg5MjZiMmI3LWQ1N2YtNDQ0Zi1iZTc3LWE1MzIzMWIwODIxMCIsImVtYWlsIjoiQWxpLk1hbGlrQG1pY3Jvc29mdC5jb20iLCJmYW1pbHlfbmFtZSI6Ik1hbGlrIiwiZ2l2ZW5fbmFtZSI6IkFsaSIsImdyb3VwcyI6WyJiMTMwNDAyMi0wOGU2LTQ0N2QtYjA5NC0xNTM3MDU5N2M2YjYiLCIwOTUzMWE3Mi0yYzNlLTRlMDYtYmUxZS0yNTk2YmQwOGRjZGQiLCJkMzRjNGViZS00OTg0LTQ5MDMtYTY0ZC04YzIwMjgzZDUxNmIiLCJlMzA5NmRmNy1iNjVjLTRlMzItYWIxYS03YTM1ZGM2ODRmMGEiXSwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNzJmOTg4YmYtODZmMS00MWFmLTkxYWItMmQ3Y2QwMTFkYjQ3LyIsImlkdHlwIjoidXNlciIsImlwYWRkciI6IjE3Mi41Ni4xMDkuMTYiLCJuYW1lIjoiQWxpIE1hbGlrIiwib2lkIjoiZGU5NDQwN2QtNzk0Mi00OThmLTg1NjgtYmE0NTdjNWM3YWQxIiwicHVpZCI6IjEwMDMyMDAyNUFCMUJGODciLCJyaCI6IjEuQVVZQUU4Q3pGZ0RUalVhc1pIN2FDQ0MyMDE5dnBoamYyeGRNbmRjV05IRXFuTDd4QU1OR0FBLiIsInNjcCI6InVzZXJfaW1wZXJzb25hdGlvbiIsInNpZCI6ImFiNmY1MTczLTIxYzktNDIwOC1iNTQ2LTM5YjcxOWQ1YTBkZiIsInN1YiI6IlR4bGM1QjFVWHNOZHY1ZVlDTGYxM3RFTnltcmpDQnJ5NUVWcVk2OTNMUU0iLCJ0aWQiOiIxNmIzYzAxMy1kMzAwLTQ2OGQtYWM2NC03ZWRhMDgyMGI2ZDMiLCJ1bmlxdWVfbmFtZSI6IkFsaS5NYWxpa0BtaWNyb3NvZnQuY29tIiwidXRpIjoiQ1BWc1dxa3ZCa1NHczdDWURsWVZBQSIsInZlciI6IjEuMCIsInhtc19pZHJlbCI6IjEgNiJ9.iK7FAJmF6ZgOjKNZj5lREFnxTu2YLtje-YKxz1BQo-O-TCtp6zJuG8DGL-BgmZPe0vK8FCCV0SJxN3igXvOL1lTMdguvd5TkoWqvdUudQOJo0LFMl03BKcbQFGbo7e7OvPLu_6gR5eOZ9wdiebDR6doX1ZnkEXzpTcSta7KiH8MVU_o_IbvgvwE-iu9J8OBiOqMzaM2LWHh1_N5RnEtZxXd7JxmD1M7f8I9V9tBB0lUVLPkTMCD16ztsAVggpGGTf9gfaupTdE6lZJOkIgfYD-ZsACFIe1y8nOsXxUjecyv-Djefa8gFI6EGxm2c51Kp16vEAoUniIfFzwkkE6-cNg'
if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")


headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))
