import requests

def test_login_page():
    url = "https://cognitos.vercel.app/signin"
    payload = {
        "username": "test@test.com",
        "password": "213fdfs2"
    }

    response = requests.post(url, json=payload)
    

    print(response)

test_login_page()





