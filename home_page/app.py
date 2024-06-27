# імпорт flask
import flask
# створюємо додаток сторінки home
home = flask.Blueprint(
    # задаємо ім'я 
    name ='home',
    # задаємо ім'я пакету в якому знаходимося
    import_name = 'home_page',
    # вказуємо шлях до папки template
    template_folder= 'templates', 
    # шлях до папки static сторінки
    static_folder= '/../static/homePage',
    # задаємо посилання на папку static сторінки
    static_url_path= '/../static/homePage'
)

