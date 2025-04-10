from flask import request, jsonify
from app.recommender import get_recommendations  # Import recommendation logic

def configure_routes(app):
    @app.route("/recommend", methods=["GET"])
    def recommend():
        """
        API Endpoint: /recommend
        Query Parameters: user_id (int)
        """
        try:
            # Get user ID from query parameters
            user_id = int(request.args.get("user_id"))

            # Generate recommendations using the recommendation system
            recommendations = get_recommendations(user_id)

            # Return recommendations as JSON
            return jsonify({
                "status": "success",
                "recommendations": recommendations
            })
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)})