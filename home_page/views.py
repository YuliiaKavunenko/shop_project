import flask, flask_login
import os

def render_home():
    if flask_login.current_user.is_authenticated:
        user_name = flask_login.current_user.name
        is_admin = flask_login.current_user.is_admin

        return flask.render_template(
            template_name_or_list = 'home.html',
            name = user_name,
            is_admin = is_admin
        )
    else: 
        user_name = ""     
        is_admin = ''
        return flask.render_template(
            template_name_or_list = 'home.html',
            name = user_name,
            is_admin = is_admin
        )

