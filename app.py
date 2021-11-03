from flask import Flask
from flask_restful import Api
from gl import GreatLeague
from ml import MasterLeague
from ul import UltraLeague

app = Flask(__name__)
api = Api(app)



api.add_resource(GreatLeague,"/api/great-league")
api.add_resource(MasterLeague,"/api/master-league")
api.add_resource(UltraLeague,"/api/ultra-league")



if __name__ == "__main__":
    app.run(host="localhost", port=8005, debug=True)