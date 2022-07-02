from flask import Blueprint, redirect, request
from . import models 

bp = Blueprint('reptile', __name__, url_prefix='/reptiles')

@bp.route('/', methods=['GET', 'POST'])
def index(): 
    # POST
    if request.method == 'POST':
        # create new reptile 
        new_reptile = models.Reptile(
            common_name = request.form['common_name'],
            scientific_name = request.form['scientific_name'],
            conservation_status = request.form['conservation_status'],
            native_habitat = request.form['native_habitat'],
            fun_fact = request.form['fun_fact']
        )
        
        # commit the new reptile to the database 
        models.db.session.add(new_reptile)
        models.db.session.commit()
        # redirect to index
        return redirect('/reptiles')
    
    # GET 
    # find all reptiles 
    found_reptiles = models.Reptile.query.all()

    # create empty dictionary with an empty list value
    reptile_dict = {'reptiles': []}

    # loop through all reptiles and append it to the list 
    for reptile in found_reptiles:
        reptile_dict["reptiles"].append({
            'common_name': reptile.common_name,
            'scientific_name': reptile.scientific_name,
            'conservation_status': reptile.conservation_status,
            'native_habitat': reptile.native_habitat,
            'fun_fact': reptile.fun_fact
        })

    # return the dictionary, which will get returned as JSON by default
    return reptile_dict

@bp.route('/<int:id>')
def show(id): 
    user = models.User.query.filter_by(id=id).first()
    user_dict = {
        'username':user.username
    }

    return user_dict
    
    # find the reptile by id
    reptile = models.Reptile.query.filter_by(id=id).first()

    # create a dictionary of the reptile's information
    reptile_dict = {
    
    'common_name': 'Ball python',
    'scientific_name': 'Python regius',
    'conservative_status': 'Near threatened',
    'native_habitat': 'Forest, savanna, shrubland, grassland',
    'fun_fact': 'Ball pythons recieved their common name from their behavior of curling up into a ball when threatened.'

    }
    
    
    # return the dictionary, which will get returned as JSON by default
    return reptile_dict
