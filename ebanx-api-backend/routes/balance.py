from . import routes

@routes.route('/balance')
def balance():
    return 'Balance'
