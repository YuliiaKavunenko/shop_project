import flask

auth = flask.Blueprint(
    name ='auth',
    import_name = 'auth_page',
    template_folder= 'templates', 
    static_folder= '/../static/authPage',
    static_url_path= '/../static/authPage'
)