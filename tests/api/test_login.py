import requests

def test_login_page():
    url = "https://cognito-05vd.onrender.com/api/v1/user/signin"
    payload = {
        "username": "test33",
        "password": "213Fdfs2"
    }

    response = requests.post(url, json=payload)
    
        
    assert response.status_code == 200 
    assert "token" in response




