import requests

def test_register_user():
    url = "https://cognito-05vd.onrender.com/api/v1/user/signup"

    payload = {
        "username": "test33",
        "email": "test33@gmail.com",
        "password": "213Fdfs2"
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 201
    assert "token" in response.json()
    assert "msg" in response.json()