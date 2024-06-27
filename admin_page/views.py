import flask
import flask_login
from reg_page.models import Product
from project.settings import db
import pandas, os

def render_admin():
    is_admin = flask_login.current_user.is_admin
    if is_admin == 'admin':
        if flask.request.method == "POST":
            xl_path = os.path.abspath(__file__ + '/../../project/products_shop.xlsx')

            xl_read = pandas.read_excel(
                io=xl_path,
                header=None,
                names=["name", "description", "image", "count", "memory", "discount","price"]
            )

            delete_product_id = flask.request.form.get("delete_product_id")
            print(f'ID DELETE ------------------------------ {delete_product_id}')
            if delete_product_id != None:
                print(delete_product_id)
                product_delete = Product.query.get(int(delete_product_id))
                print(f"PDELETE - -- --   -- ---  -- -  - {product_delete}")
                db.session.delete(product_delete)
                db.session.commit()
                xl_read = xl_read.drop(int(delete_product_id) - 1)



            print("hezbala")
            name = flask.request.form.get("name")
            description = flask.request.form.get("description")
            image = flask.request.files.get("image")
            price = flask.request.form.get("price")
            discount = flask.request.form.get("discount")
            count = flask.request.form.get("count")
            memory = flask.request.form.get("memory")
            print(f"HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHI {name}")
            if name and description and image and price and discount and count and memory != None:
                print("MAMMFKJSHDJKLHSKJLDALHKJDGKJLSDFHGJKLSADLKJHG")
                new_product = Product(
                    name = name,
                    description = description,
                    image = image.filename,
                    count = count,
                    memory = memory,
                    discount = discount,
                    price = price

                )
                
                db.session.add(new_product)
                db.session.commit()
                image.save(os.path.abspath(__file__ + f"/../../static/shopPage/img/{image.filename}"))
                new_product_data = {
                    "name": name,
                    "description": description,
                    "image": image.filename,
                    "count": count,
                    "memory": memory,
                    "discount": discount,
                    "price": price
                    
                }
                xl_read = xl_read._append(new_product_data, ignore_index = True)


            
            product_id = flask.request.form.get('product_id')
            # print(f'product_id - {int(product_id)}')

            new_name = flask.request.form.get('new_name')
            print(new_name)
            new_price = flask.request.form.get('new_price')
            print(new_price)
            new_discount = flask.request.form.get('new_discount')
            print(new_discount)
            new_memory = flask.request.form.get('new_memory')
            new_image = flask.request.files.get("new_image")


            # print(f'product ---- {product}')
            # print(f'product NAME -  {product.name}')
            
            if new_name != None:
                product = Product.query.get(int(product_id))
                product.name = new_name
                xl_read.loc[int(product_id)- 1, "name"] = new_name
                # xl_read.to_excel(xl_path, index = False)
            if new_price != None:
                product = Product.query.get(int(product_id))
                product.price = new_price
                xl_read.loc[int(product_id) - 1, "price"] = int(new_price)
                # xl_read.to_excel(xl_path, index = False)
            if new_discount != None: 
                product = Product.query.get(int(product_id))
                product.discount = new_discount
                xl_read.loc[int(product_id) - 1, "discount"] = int(new_discount)
            if new_image != None:
                product = Product.query.get(int(product_id))
                file_name = new_image.filename
                new_image.save(os.path.abspath(__file__ + f"/../../static/shopPage/img/{file_name}"))
                product.image = file_name
                
                xl_read.loc[int(product_id) - 1, "image"] = file_name
            if new_memory != None:
                product = Product.query.get(int(product_id))
                memory_index = int(flask.request.form.get(f"index_button_{product_id}"))
                print( f'INDEX BUTTON - {memory_index} iiiiiii PRODUCT ID - {product_id}')
                memories = product.memory.split(",")
                memories[memory_index] = new_memory
                product.memory = ",".join(memories)
                print(memories)
                xl_read.loc[int(product_id) - 1, "memory"] = product.memory
                db.session.commit()

            xl_read.to_excel(xl_path, index = False, header = None)



            db.session.commit()
            
        flask.redirect("/adminshop/")
        user_name = flask_login.current_user.name

        return flask.render_template(template_name_or_list = 'admin.html', product = Product.query.all(),name=user_name, is_admin = is_admin)
    else:
        return "Ви не є адміністратором!"