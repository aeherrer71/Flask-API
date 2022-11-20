from flask import Flask, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('staff', user='', password='', host='localhost', port=5432)

class BaseModel(Model):
  class Meta:
    database = db

class Employee(BaseModel):
  first_name = CharField()
  last_name = CharField()
  department = CharField()
  phone = BigIntegerField()
  email = CharField()
  age = IntegerField()

db.connect()
db.drop_tables([Employee])
db.create_tables([Employee])

Employee(first_name='Alexis', last_name='Herrera', department='CSIS', phone=7182094466, email='alex123@jmail.com', age=32).save()
Employee(first_name='Jules', last_name='Rayden', department='Legal', phone=719293456, email='Jules123@jmail.com', age=38).save()
Employee(first_name='Ramon', last_name='Suzares', department='Marketing', phone=7109094466, email='suzares123@jmail.com', age=44).save()
Employee(first_name='Jermaine', last_name='Wallace', department='Accounting', phone=7182023566, email='JWallace123@jmail.com', age=32).save()

app = Flask(__name__)

@app.route('/')
def index():
  return "This is the API ROOT"

@app.route('/employee/', methods=['GET', 'POST'])
@app.route('/employee/<id>', methods=['GET', 'PUT', 'DELETE'])
def endpoint(id=None):
  if request.method == 'GET':
    if id:
        return jsonify(model_to_dict(Employee.get(Employee.id == id)))
    else:
        staff = []
        for employee in Employee.select():
            staff.append(model_to_dict(employee))
        return jsonify(staff)

  if request.method =='PUT':
    body = request.get_json()
    Employee.update(body).where(Employee.id == id).execute()
    return "Employee " + str(id) + " has been updated."

  if request.method == 'POST':
    new_employee = dict_to_model(Employee, request.get_json())
    new_employee.save()
    return jsonify({"success": True})

  if request.method == 'DELETE':
    Employee.delete().where(Employee.id == id).execute()
    return "Employee " + str(id) + " deleted."

app.run(debug=True, port=9000)