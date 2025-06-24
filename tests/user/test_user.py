def test_update_user(client):
    # Primeiro, cria um usuário
    response = client.post("/auth/signup", json={
        "name": "Gustavo",
        "email": "gustavo@email.com",
        "password": "123456"
    })
    print("Resposta Signup:", response.status_code, response.json())
    assert response.status_code == 200
    user_id = response.json()["id"]

    # Faz login para obter o token
    login_response = client.post("/auth/login", json={
        "email": "gustavo@email.com",
        "password": "123456"
    })
    print("Resposta Login:", login_response.status_code, login_response.json())
    assert login_response.status_code == 200
    token = login_response.json()["access_token"]

    # Atualiza o usuário
    update_response = client.put(f"/users/{user_id}", json={
        "name": "Gustavo Atualizado",
        "email": "gustavo@email.com",
        "password": "nova_senha"
    }, headers={"Authorization": f"Bearer {token}"})
    print("Resposta Update:", update_response.status_code, update_response.json())
    assert update_response.status_code == 200
    assert update_response.json()["name"] == "Gustavo Atualizado"
