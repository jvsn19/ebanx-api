from flask import json

DEPOSIT = 'deposit'
WITHDRAW = 'withdraw'
TRANSFER = 'transfer'

def test_event_deposit_nonexisting_account(app, db):
    db.reset()
    data = {
        'type': DEPOSIT,
        'destination': '789', # non-existing id
        'amount': 100,
    }
    response = app.post('/event', json=data)
    assert response.status_code == 201
    response_destination = response.get_json().get('destination')
    assert response_destination.get('id') == data.get('destination')
    assert response_destination.get('balance') == data.get('amount') 

def test_event_deposit_existing_account(app, db):
    db.reset()
    acc_1 = db.create_account(1000)
    # The mocked account obj with id 123 has a previous balance == 200
    data = {
        'type': DEPOSIT,
        'destination': acc_1,
        'amount': 100, 
    }
    response = app.post('/event', json=data)
    assert response.status_code == 201
    response_destination = response.get_json().get('destination')
    assert response_destination.get('id') == acc_1
    assert response_destination.get('balance') == 1100

def test_event_withdraw_nonexisting_account(app, db):
    db.reset()
    data = {
        'type': WITHDRAW,
        'origin': '789',
        'amount': 1000,
    }
    response = app.post('/event', json=data)
    assert response.status_code == 404

def test_event_withdraw_existing_account(app, db):
    db.reset()
    acc_1 = db.create_account(1000)
    data = {
        'type': WITHDRAW,
        'origin': acc_1,
        'amount': 100,
    }
    response = app.post('/event', json=data)
    assert response.status_code == 201
    response_origin = response.get_json().get('origin')
    assert response_origin.get('id') == acc_1
    assert response_origin.get('balance') == 900

def test_event_transfer_exist_exist(app, db):
    db.reset()
    origin, destination = [db.create_account(1000) for _ in range(2)]
    data = {
        'type': TRANSFER,
        'origin': origin,
        'destination': destination,
        'amount': 100,
    }
    # The mocked account obj with id 123 has a previous balance == 200
    response = app.post('/event', json=data)
    assert response.status_code == 201
    response_json = response.get_json()
    response_origin = response_json.get('origin')
    response_destination = response_json.get('destination')
    assert response_origin.get('id') == origin
    assert response_origin.get('balance') == 900
    assert response_destination.get('id') == destination
    assert response_destination.get('balance') == 1100

def test_event_transfer_exist_nonexist(app, db):
    db.reset()
    origin, destination = db.create_account(1000), '789'
    data = {
        'type': TRANSFER,
        'origin': origin,
        'destination': destination,
        'amount': 100,
    }
    response = app.post('/event', json=data)
    assert response.status_code == 201
    response_json = response.get_json()
    response_origin = response_json.get('origin')
    response_destination = response_json.get('destination')
    assert response_origin.get('id') == origin
    assert response_origin.get('balance') == 900
    assert response_destination.get('id') == destination
    assert response_destination.get('balance') == 100

def test_event_transfer_origin_nonexist(app, db):
    db.reset()
    data = {
        'type': TRANSFER, 
        'origin': '0', 
        'destination': '1', 
        'amount': 100
    }
    response = app.post('/event', json=data)
    assert response.status_code == 404
