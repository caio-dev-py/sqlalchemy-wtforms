from flask import Flask
from models import mail, db
from config import Config

# Aplicar configurações
app = Flask(__name__)
app.config.from_object(Config)

mail.init_app(app)
db.init_app(app)


# Blueprints
from routes.home import home_route
from routes.form import form_route

app.register_blueprint(home_route)
app.register_blueprint(form_route)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)