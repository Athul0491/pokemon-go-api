from flask import Flask
from flask_restful import Api
from resources.gl import GreatLeague
from resources.ml import MasterLeague
from resources.ul import UltraLeague

app = Flask(__name__)
api = Api(app)



api.add_resource(GreatLeague,"/api/great-league")
api.add_resource(MasterLeague,"/api/master-league")
api.add_resource(UltraLeague,"/api/ultra-league")



if __name__ == "__main__":
    app.run()