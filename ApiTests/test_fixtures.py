import pytest
import requests
from My_functions.users import deleteuser

payload = {"email": "eve.holt@reqres.in","password": "pistol"}

@pytest.fixture()
def setup():
    resp = requests.post("https://reqres.in/api/register",payload)
    print(resp.status_code)
    assert resp.status_code == 200
    yield
    url = "https://reqres.in/api/users/2"
    out_resp = deleteuser(url)
    # response = out_resp.json()
    print(out_resp.status_code)
    assert out_resp.status_code == 204, "user deletion failed"

def test_loginuser(setup):
    resp = requests.post("https://reqres.in/api/login",payload)
    print(resp.json())
    print(resp.status_code)
    assert resp.status_code == 200





