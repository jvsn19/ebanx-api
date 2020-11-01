def test_create_new_account(app, db):
    db.reset()
    new_acc_id = db.create_account()
    new_acc = db.get_account(new_acc_id)
    assert new_acc.id == new_acc_id
