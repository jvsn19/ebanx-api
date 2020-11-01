from flask import json

DEPOSIT = 'deposit'
WITHDRAW = 'withdraw'
TRANSFER = 'transfer'

def test_event_deposit_nonexisting_account(app, db):
    db.reset()
    response = app.post('/event', data={'type': DEPOSIT, 'destination': '789', 'amount': 100})
    assert response.status_code == 201
    data = json.loads(response.get_data(as_text=True))
    assert data.get('id') == '789'
    assert data.get('balance') == '100'

def test_event_deposit_existing_account(app, db):
    db.reset()
    acc_1 = db.create_account(1000)
    # The mocked account obj with id 123 has a previous balance == 200
    response = app.post('/event', data={'type': DEPOSIT, 'destination': f'{acc_1}', 'amount': 100})
    assert response.status_code == 201
    data = json.loads(response.get_data(as_text=True))
    assert data.get('id') == f'{acc_1}'
    assert data.get('balance') == '1100'

def test_event_withdraw_nonexisting_account(app, db):
    db.reset()
    response = app.post('/event', data={'type': WITHDRAW, 'origin': '789', 'amount': 100})
    assert response.status_code == 404

def test_event_withdraw_existing_account(app, db):
    db.reset()
    acc_1 = db.create_account(1000)
    # The mocked account obj with id 123 has a previous balance == 200
    response = app.post('/event', data={'type': WITHDRAW, 'origin': f'{acc_1}', 'amount': 100})
    assert response.status_code == 201
    data = json.loads(response.get_data(as_text=True))
    assert data.get('id') == f'{acc_1}'
    assert data.get('balance') == '900'

def test_event_transfer_exist_exist(app, db):
    db.reset()
    origin, destiny = [db.create_account(1000) for _ in range(2)]
    # The mocked account obj with id 123 has a previous balance == 200
    response = app.post('/event', data={'type': TRANSFER, 'origin': f'{origin}', 'destination': f'{destiny}', 'amount': 100})
    assert response.status_code == 201
    data = json.loads(response.get_data(as_text=True))
    assert data.get('origin').get('id') == f'{origin}'
    assert data.get('origin').get('balance') == '900'
    assert data.get('destination').get('id') == f'{destiny}'
    assert data.get('destination').get('balance') == '1100'

def test_event_transfer_exist_nonexist(app, db):
    db.reset()
    origin, destiny = db.create_account(1000), '9999'
    # The mocked account obj with id 123 has a previous balance == 200
    response = app.post('/event', data={'type': TRANSFER, 'origin': f'{origin}', 'destination': f'{destiny}', 'amount': 100})
    assert response.status_code == 201
    data = json.loads(response.get_data(as_text=True))
    assert data.get('origin').get('id') == f'{origin}'
    assert data.get('origin').get('balance') == '900'
    assert data.get('destination').get('id') == f'{destiny}'
    assert data.get('destination').get('balance') == '100'

def test_event_transfer_origin_nonexist(app, db):
    db.reset()
    response = app.post('/event', data={'type': TRANSFER, 'origin': '0', 'destination': '1', 'amount': 100})
    assert response.status_code == 404
