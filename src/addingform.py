from flask import Blueprint, render_template, request
from src.pydanticmodels import Person_pydantic
from src.db.dbmodels import Person
from src.db.dbscripts import adding_person

adding = Blueprint('adding',__name__)

@adding.route('/addingform')
def return_form():
    return render_template('form.html')

@adding.route('/goodluck', methods = ['POST'])
def post_send_form():
    name = request.form.get('name')
    email = request.form.get('email')
    dict_person = {'name' : name , 'email' : email}
    person = Person_pydantic(**dict_person)
    person = Person(name = person.name, email = person.email)
    output = adding_person(person)
    if output == 200:
        return render_template('goodluck.html')
    else:
        return render_template('uniquenesserror.html')
