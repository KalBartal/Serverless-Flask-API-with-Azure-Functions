import logging
import azure.functions as func
from flask import Flask, request, jsonify

app = Flask(__name__)  # Create a Flask app instance


# Create a route for the Flask app that listens for POST requests to the '/api/greet' endpoint
@app.route('/api/greet', methods=['POST'])
def greet():
    data = request.get_json()  # Get the JSON data from the request
    name = data['name']  # Extract the 'name' parameter from the JSON data
    # Create a greeting message using the 'name' parameter
    message = f"Hello, {name}!"
    return jsonify(message=message)  # Return the message as JSON


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Try to get the 'name' parameter from the query string of the request
        name = req.params.get('name')
        if not name:  # If the 'name' parameter was not found in the query string
            try:
                req_body = req.get_json()  # Try to get the JSON data from the request body
            except ValueError:
                pass
            else:
                # If the JSON data was found, extract the 'name' parameter from it
                name = req_body.get('name')
        if name:  # If the 'name' parameter was found
            # Return a greeting message with the 'name' parameter
            return func.HttpResponse(f"Hello, {name}!")
        else:  # If the 'name' parameter was not found
            return func.HttpResponse(
                # Return an error message
                "Please pass a name on the query string or in the request body",
                status_code=400
            )
    except Exception as e:  # Catch any exceptions that may occur
        print(str(e))  # Print the error message to the console
