def test_home_get(app, client):
    response = client.get('/')
    assert response.status_code == 200


def test_home_valid(app, client):
    response = client.post('/', data={'years': '1'})
    assert response.status_code == 200

    response = client.post('/', data={'years': '2022'})
    assert response.status_code == 200

    response = client.post('/', data={'years': '9999'})
    assert response.status_code == 200


def test_home_with_command(app, client):
    response = client.post('/', data={'years': '2022; uname -a'})
    assert response.status_code == 400


def test_home_min(app, client):
    response = client.post('/', data={'years': '00'})
    assert response.status_code == 400

    response = client.post('/', data={'years': '0000'})
    assert response.status_code == 400


def test_home_max(app, client):
    response = client.post('/', data={'years': '10000'})
    assert response.status_code == 400