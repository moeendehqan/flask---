
from flask import Flask, request
from flask_cors import CORS
import pymongo
import warnings
import functions
from waitress import serve


warnings.filterwarnings("ignore")
client = pymongo.MongoClient()
farasahmDb = client['vpn']
userCl = farasahmDb['users']
app = Flask(__name__)
CORS(app)


@app.route('/getconfig',methods = ['POST', 'GET'])
def captcha():
    data = request.get_json()
    return functions.getConfig(data)



if __name__ == '__main__':
    #serve(app, host="0.0.0.0", port=8080,threads= 8)
    app.run(host='0.0.0.0', debug=True)