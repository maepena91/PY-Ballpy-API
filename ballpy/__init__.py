# config                    
from flask import Flask, redirect
from flask_migrate import Migrate

# factory
def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/ballpy'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from . import models 
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    # index route
    @app.route('/')
    def index(): 
        return redirect('/reptiles')

    # register reptiles blueprint 
    from . import reptile 
    app.register_blueprint(reptile.bp)

    # return the app 
    return app