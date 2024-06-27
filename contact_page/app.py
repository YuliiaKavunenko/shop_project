import flask

contact = flask.Blueprint(
    name = "contact",
    import_name= "contact_page",
    template_folder= "templates",
    static_folder= "/../static/contactPage",
    static_url_path= "/../static/contactPage"
    
)