from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import decimal
import flask.json
from flask_cors import CORS
import os

app = Flask(__name__)   
CORS(app)          

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class MyJSONEncoder(flask.json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        return super(MyJSONEncoder, self).default(obj)

from models import Drink 

@app.route("/api/getall", methods=['GET'])
def get_all():
    try:
        drinks=Drink.query.all()
        print([e.serialize() for e in drinks])
        return jsonify([e.serialize() for e in drinks])
    except Exception as e:
        return(str(e))

@app.route("/api/drinks", methods=['POST'])
def add_drink():
    if request.method == 'POST':
        print(request.json)
        date=request.json['date']
        btype=request.json['btype']
        name=request.json['name']
        place=request.json['place']
        try:
            drink=Drink(
                date=date,
                btype=btype,
                name=name,
                place=place
            )
            print(date)
            db.session.add(drink)
            db.session.commit()
            return "Drink added. Drink id={}".format(drink.id)
        except Exception as e:
            return(str(e))
    

@app.route("/api/drinks/<id_>", methods=["GET"])
def get_by_id(id_):
    try:
        drink=Drink.query.filter_by(id=id_).first()
        return jsonify(drink.serialize())
    except Exception as e:
        return(str(e))

@app.route("/add/form",methods=['GET', 'POST'])
def add_new_drink():
    if request.method == 'POST':
        date=request.form.get('date')
        btype=request.form.get('btype')
        name=request.form.get('name')
        try:
            drink=Drink(
                date=date,
                btype=btype,
                name=name,
            )
            db.session.add(drink)
            db.session.commit()
            return "Drink added. Drink id={}".format(drink.id)
        except Exception as e:
            return(str(e))
    return render_template("getData.html")
    




if __name__ == "__main__":        
    app.run()     
