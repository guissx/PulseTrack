def test_signup(client):
    response = client.post("/auth/signup", json={
        "name": "Gustavo",
        "email": "gustavo@email.com",
        "password": "123456"
    })
    assert response.status_code == 200
    assert response.json()["email"] == "gustavo@email.com"
    assert "id" in response.json()

def test_login(client):
    response = client.post("/auth/login", json={
        "name": "Gustavo",  
        "email": "gustavo@email.com",
        "password": "123456"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"
