from . import routes

@routes.route('/reset')
def reset():
    return 'Reset'
