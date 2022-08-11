from os import getenv
from flask import Flask, render_template, request, flash, url_for, redirect
from flask_migrate import Migrate
from models.database import db
from models.users import Users
from forms.add_user import UserForm
from sqlalchemy.exc import IntegrityError

app = Flask(__name__,  template_folder='templates')
config_name = "config.%s" % getenv("CONFIG", "ProductionConfig")
app.config.from_object(config_name)

db.init_app(app)
migrate = Migrate(app, db, compare_type=True)


@app.route("/", endpoint="list")
def index_page():
    users = Users.query.all()
    return render_template(
        "list.html",
        users=users,
    )


@app.route('/add/', methods=["GET", "POST"], endpoint='add')
def add_users():
    form = UserForm()
    if request.method == "GET":
        return render_template('add.html', form=form)

    name = form.name.data
    username = form.username.data
    email = form.email.data

    user = Users(name=name, username=username, email=email)
    db.session.add(user)

    try:
        db.session.commit()
    except IntegrityError:
        error_text = f"Could not save product {name!r}, he's not unique!"
        form.form_errors.append(error_text)
        return render_template("add.html", form=form), 400

    flash(f"Created new user: {name}", "success")
    url = url_for("list")

    return redirect(url)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
