from flask import Flask
from flask_restful import Api
from src.gl import GreatLeague
from src.ml import MasterLeague
from src.ul import UltraLeague
from src.wild import Wild
from src.pvp import Pvp
from src.details import Details
app = Flask(__name__)
api = Api(app)



api.add_resource(GreatLeague,"/api/great-league")
api.add_resource(MasterLeague,"/api/master-league")
api.add_resource(UltraLeague,"/api/ultra-league")
api.add_resource(Wild,"/api/wild")
api.add_resource(Pvp,"/api/pvp-iv")
api.add_resource(Details,"/api/pvp-details")



if __name__ == "__main__":
    app.run()