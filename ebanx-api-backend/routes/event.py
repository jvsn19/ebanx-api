from . import routes

@routes.route('/event')
def event():
    return 'Event'
