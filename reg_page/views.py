import flask, flask_login
from project.settings import db
from .models import User

def render_reg(): 
    if flask.request.method == 'POST':
        print('Hello')
        print(flask.request.form)
        user = User(
            name = flask.request.form['login'],
            email = flask.request.form['email'],
            password = flask.request.form['password'],
            is_admin = 'admin'
        )
        
        
        try:
            print(user)
            db.session.add(user)
            db.session.commit()
            return flask.redirect('/authorization/')
        except:
            return 'Error'

    return flask.render_template(template_name_or_list = 'reg.html')
