# ebanx-api

A simple API for learning purpose. This API works like a bank account, where the user can create accounts and do transactions like deposit, withdraw and transference. The methods are listed below:

- GET
    - `/balance?account_id=<account_id: id>`
- POST
    - `/event {"type":<"deposit" | "withdraw" | "transfer">, "destination":<account_id: id>, "amount":<value: int>}`
    - `/event {"type":<"withdraw" | "withdraw" | "transfer">, "origin":<account_id: id>, "amount":<value: int>}`
    - `/event {"type":<"transfer" | "withdraw" | "transfer">, "origin": <account_id: id>, "destination":<account_id: id>`

The API will be in the following [automated test suit website](https://ipkiss.pragmazero.com/)

## API with Flask
- [x] Application with Flask
- [x] Custom Database
- [x] Tests

## [Optional] API with pure Python
- [ ] Application with Flask
- [ ] Custom Database
- [ ] Tests

## [Optional] Extras
- [ ] Use a real database
    - [ ] Postgres
    - [ ] Redis
- [ ] Use Docker
