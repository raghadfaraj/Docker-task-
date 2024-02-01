from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql://{os.environ["PROD_DB_USER"]}:' \
                                        f'{os.environ["PROD_DB_PASSWORD"]}@{os.environ["PROD_DB_HOST"]}:5432/' \
                                        f'{os.environ["PROD_DB_NAME"]}'

db = SQLAlchemy(app)

class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)


@app.route("/", methods=["GET"])
def home_route():
    return "hello world"

@app.route("/names",methods=["POST","GET"])
def name_route():
    if request.method == 'POST':
        person = request.get_json()

        new_person = People(name=person["name"],last_name=person["last_name"])
        db.session.add(new_person)
        db.session.commit()
        return "commited"

    elif request.method == 'GET':
        people = People.query.all()
        results = [{
            "first name": person.name,
            "last name": person.last_name
        } for person in people]

        return jsonify(results)




if __name__ == "__main__":
    app.run(port=5000,debug=True ,host="0.0.0.0")
