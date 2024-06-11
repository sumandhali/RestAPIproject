import pytest

from My_functions.users import getListofUsers,getsingleUser,postsingleuser,putsingleuser,deleteuser

baseUrl="https://reqres.in/api/users/"
p={"page":2}
Id= '2'


def test_Listusersresp():
    url = baseUrl
    data = getListofUsers(url,p)
    # print(data)
    response_data = data.json()
    print(response_data)
    # print(data.status_code)
    assert len(response_data) > 0 , "empty_response"
    assert data.status_code == 200
    assert response_data['total_pages'] == 2


def test_singleuserresp():
    url = baseUrl + Id
    data = getsingleUser(url)
    resp_data = data.json()
    print(resp_data)
    assert len(resp_data) > 0
    assert data.status_code == 200


def test_postuserresp():
    url = baseUrl
    data = postsingleuser(url)
    resp_data = data.json()
    print(resp_data)
    assert resp_data['id'] != None
    assert data.status_code == 201

def test_putuserresp():
    url = baseUrl + Id
    data = putsingleuser(url)
    resp_data = data.json()
    assert data.status_code == 201
    print(resp_data)

# def test_patchuser():
#     url = baseUrl + Id
#     # print(url)
#     data = patchuser(url)
#     resp_data = data.json()
#     print(resp_data)

def test_deleteuser():
    url = baseUrl + Id
    out_resp = deleteuser(url)
    # response = out_resp.json()
    print(out_resp.status_code)
    assert out_resp.status_code == 204 , "user deletion failed"









