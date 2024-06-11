import requests
import pytest

@pytest.mark.parametrize("data", [
    {"email": "eve.holt@reqres.in","password": "pistol"},
    {"email": "dhali@suman.in","password": "tester"},
    {"email": "jakie@jam.in","password": "abc@123"}
])

def test_creatingmultipleusers(data):
    url = "https://reqres.in/api/register/"
    resp = requests.post(url,json=data)
    print(resp.json())
    assert resp.status_code == 200
