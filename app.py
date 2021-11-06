from flask import Flask
from flask_restful import Api
from resources.gl import GreatLeague
from resources.ml import MasterLeague
from resources.ul import UltraLeague
from resources.wild import Wild
from resources.pvp import Pvp

app = Flask(__name__)
# api = Api(app)



api.add_resource(GreatLeague,"/api/great-league")
api.add_resource(MasterLeague,"/api/master-league")
api.add_resource(UltraLeague,"/api/ultra-league")
api.add_resource(Wild,"/api/wild")
api.add_resource(Pvp,"/api/pvp")



# if __name__ == "__main__":
#     app.run(port=5000)