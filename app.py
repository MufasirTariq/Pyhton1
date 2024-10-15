from flask import Flask, jsonify, request
from databases import dbinitialization
from databases.models import teacher

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'host':"mongodb://localhost:27017/test"}
dbinitialization.initialize_db(app)

@app.route('/getteacher')
def getTeacher():
    data=teacher.objects()
    return jsonify(data)

@app.route('/addteacher', methods=["POST"])
def addTeacher():
    try:
        data = request.get_json()
        t = teacher(name=data["name"], empcode=data["empcode"], edu=data["edu"], exp=data["exp"]).save()
        res = {'id': str(t.id), 'inserted': "done"}
    except Exception as e:
        res = {'exp': str(e), 'inserted': "failed"}
    return jsonify(res)

@app.route("/getteacherbyid/<id>")
def getTeacherData(id):
    data = teacher.objects(id=id)
    return jsonify(data)

@app.route("/updateteacher/<id>", methods=["PUT"])
def updateteacher(id):
    try:
        data = request.get_json()
        teacher.objects(id=id).update(name=data["name"], empcode=data["empcode"],  edu=data["edu"], exp=data["exp"])
        res = {'id': str(id), "updated": "done"}
    except Exception as e:
        print(str(e))
        res = {'id': str(id), "updated": "failed"}
    return jsonify(res)

@app.route("/deleteteacher/<id>", methods=["DELETE"])
def deleteteacher(id):
    try:
        teacher.objects(id=id).delete()
        res = {'id': str(id), "deleted": "done"}
    except Exception as e:
        print(str(e))
        res = {'id': str(id), "deleted": "failed"}
    return jsonify(res)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
