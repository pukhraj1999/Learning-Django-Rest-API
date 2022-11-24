import requests

endpoint="http://localhost:8000/api/about/"

get_response=requests.post(endpoint,json={"title":"Hi There!!","content":"Love Yourself"})
print(get_response.text)