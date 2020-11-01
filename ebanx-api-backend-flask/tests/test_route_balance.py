from flask import json

def test_balance_empty_db(app, db):
    response = app.get('/balance?account_id=0')
    assert response.status_code == 404

def test_balance_valid_id(app, db):
    response = app.get('/balance?account_id=123')
    assert response.status_code == 200

    data = json.loads(response.get_data(as_text=True))

    assert data == 200
