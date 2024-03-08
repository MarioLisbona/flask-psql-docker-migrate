from flask import jsonify

def init_routes(app):
    
    @app.route("/", methods=["GET"])
    def home():
        return jsonify({
            "msg": "home",
        }), 200

    @app.route("/api", methods=["GET"])
    def get_api_base_url():
        return jsonify({
            "msg": "todos api is up",
            "success": True,
            "data": None
        }), 200