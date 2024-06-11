import requests

# get api call and return response data
def getListofUsers(url,p):
    print("Request Url:",url)
    resp = requests.get(url,params=p)
    return resp

def getsingleUser(url):
    print("Request Url:", url)
    resp = requests.get(url)
    return resp

pay_load = {
    "name": "morpheus",
    "job": "leader"
}

def postsingleuser(url):
    resp = requests.post(url,pay_load)
    return resp

payload = {
    "name": "morpheus",
    "job": "zion resident"
}
def putsingleuser(url):
    resp = requests.put(url,payload)
    return resp


# payload = {"email":"suma.weaver@reqres.in"}
# def patchuser(url):
#     resp = requests.patch(url,payload)
#     return resp


def deleteuser(url):
    out_resp = requests.delete(url)
    return out_resp