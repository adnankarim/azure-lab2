from flask import Flask, request, jsonify
import logging
from flask_cors import CORS
from numerical_integration import numerical_integration

app = Flask(__name__)

# Enabling CORS for the app
CORS(app)

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Allowiing both trailing and non-trailing slashes
app.url_map.strict_slashes = False

@app.route("/")
def helloworld():
	return 'Hello World!'


@app.route("/numericalintegralservice/<float:lower>/<float:upper>", methods=["GET"])
@app.route("/numericalintegralservice/<int:lower>/<int:upper>", methods=["GET"])
@app.route("/numericalintegralservice/<float:lower>/<int:upper>", methods=["GET"])
@app.route("/numericalintegralservice/<int:lower>/<float:upper>", methods=["GET"])

def integration_service(lower, upper):
    app.logger.info(f"Received request: {request.method} {request.url}")
    app.logger.info(f"Processing numerical integration request for range [{lower}, {upper}]")
  
    """
    Return 7 integral results for N=[10, 100, 1000, 10k, 100k, 1M].
    """
    N_values = [10, 100, 1000, 10_000, 100_000, 1_000_000]
    results = {}

    try:
        # Compute results
        for N in N_values:
            results[f"N={N}"] = numerical_integration(lower, upper, N)

        # Log the successful response
        app.logger.info("Successfully computed numerical integration results")
        return jsonify(results), 200

    except Exception as e:
        # Log the error details
        app.logger.error(f"An error occurred: {str(e)}", exc_info=True)
        
        # Return an error response
        return jsonify({
            "error": "An error occurred during numerical integration.",
            "details": str(e)
        }), 500

if __name__ == "__main__":
    # Running on port 5000
    app.run(host="0.0.0.0", port=5000, debug=True)
