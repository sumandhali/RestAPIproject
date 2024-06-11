import requests,json

baseUrl="https://reqres.in/api/users/"
Id = "2"

#Getting the lists of users
def getlistofusers():
      url = baseUrl
      response = requests.get(url)
      print(response)
      print(response.json())
      print(response.request.headers)
      print(response.headers)
      print(response.status_code)
      print(response.encoding)
      print(response.headers['content-type'])
      print(response.elapsed.total_seconds())
#getlistofusers()

def getsingleUser():
    url = baseUrl + Id
    resp = requests.get(url)
    print(url)
    return resp

print(getsingleUser())







