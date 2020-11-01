from flask import json

def test_balance_empty_db(app, db):
    db.reset()
    response = app.get('/balance?account_id=0')
    assert response.status_code == 404

def test_balance_valid_id(app, db):
    db.reset()
    id = db.create_account(1000)
    response = app.get(f'/balance?account_id={id}')
    assert response.status_code == 200

    data = json.loads(response.get_data(as_text=True))

    assert data == 1000
