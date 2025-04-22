from flask import request, jsonify, render_template
from app.recommender import get_recommendations_with_user_data  # Import recommendation logic

def configure_routes(app):
    @app.route("/")
    def index():
        """
        Render the main page.
        """
        return render_template("index.html")

    @app.route("/recommend", methods=["GET"])
    def recommend():
        """
        API Endpoint: /recommend
        Query Parameters: user_id (int)
        """
        try:
            # Get user ID from query parameters
            user_id = int(request.args.get("user_id"))
            n_recommendations = 10  # Default number of recommendations

            # Generate recommendations using the recommendation system
            recommendations = get_recommendations_with_user_data(user_id, n_recommendations)

            # Return recommendations as JSON
            return jsonify({
                "status": "success",
                "recommendations": recommendations
            })
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)})