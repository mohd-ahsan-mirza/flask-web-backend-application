from flask import Flask,render_template,request
from flask_migrate import Migrate
from models import db, InfoModel
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://user1:password@localhost:5432/app"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)
 
if __name__ == '__main__':
    app.run(debug=True)
 
db.init_app(app)
 

@app.route('/')
def hello():
    new_user = InfoModel(name='Ahsan', age=29)
    db.session.add(new_user)
    db.session.commit()
    return 'Hello, World!'