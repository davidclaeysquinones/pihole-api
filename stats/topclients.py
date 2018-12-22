import flask
import requests
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/stats/top_clients', methods=['GET'])
def top_clients():
    r = requests.get("http://localhost:3000/admin/api.php?topClients")

    print r.text
    return r.text

app.run()