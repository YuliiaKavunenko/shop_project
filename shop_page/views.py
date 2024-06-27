import flask, flask_login, os, pandas
from reg_page.models import Product
import project

def delete_all_products():
    # Удаляем все записи из таблицы
    Product.query.delete()
    project.db.session.commit()

def render_shop():
    delete_all_products()
    is_admin = flask_login.current_user.is_admin
    xl_path = os.path.abspath(__file__ + '/../../project/products_shop.xlsx')
    xl_read = pandas.read_excel(
        io=xl_path,
        header=None,
        names=["name", "description", "image", "count", "memory", "discount","price"]
    )


    if Product.query.count() == 0:
        for product in xl_read.iterrows():
            row_data = product[1]
            products = Product(
                name = row_data["name"],
                description = row_data["description"],
                image =  row_data["image"],
                count = row_data["count"],
                memory = row_data["memory"],
                discount = row_data["discount"],
                price = row_data["price"]

                
            )
            project.db.session.add(products)
        project.db.session.commit()

    user_name = flask_login.current_user.name

    return flask.render_template(template_name_or_list="shop.html", name = user_name, product = Product.query.all(), count = products.count, is_admin = is_admin)
