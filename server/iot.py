from flask_restplus import Namespace,Resource
api_ns = Namespace("iot", description="API.")
@api_ns.route("/main_menu")
class AdvertiseTcpserver(Resource):
    def get(self):
        #TODO return the correct ip value
        return {"main_menu": "ip"}