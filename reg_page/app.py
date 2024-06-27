import flask

registration = flask.Blueprint(
    name ='registration',
    import_name = 'reg_page',
    template_folder= 'templates', 
    static_folder= '/../static/regPage',
    static_url_path= '/../static/regPage'
)