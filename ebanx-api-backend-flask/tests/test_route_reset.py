def test_reset(app):
    response = app.post('/reset')
    assert response.status_code == 200
