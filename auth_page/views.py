import flask, flask_login
from reg_page.models import User

def render_auth(): 
    if flask.request.method == "POST":
        users = User.query.filter_by(
            name = flask.request.form["login"],
            password = flask.request.form["password"]
        )
    
        if len(list(users)) == 0:
            print('ERROR REG')
            return flask.render_template(template_name_or_list = 'auth.html', error = True)
        else:
            print('GOOD REG')
            flask_login.login_user(users[0])
            return flask.redirect("/")
    print('NONE REG')
    print(User.query.all())
    return flask.render_template(template_name_or_list = 'auth.html', error = False)
