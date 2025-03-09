from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Determine which ranking to fetch based on query parameters
    ranking_type = request.args.get('type', 'compsci')  # Default to compsci

    # API Endpoints
    cs_api_url = "http://127.0.0.1:5000/compsci"
    national_api_url = "http://127.0.0.1:5000/national"

    # Fetch Data
    if ranking_type == "national":
        response = requests.get(national_api_url)
    else:
        response = requests.get(cs_api_url)

    # Parse JSON Responses
    colleges = response.json() if response.status_code == 200 else []

    return render_template('index.html', cs_colleges=colleges, ranking_type=ranking_type)

if __name__ == '__main__':
    app.run(debug=True, port=5001)