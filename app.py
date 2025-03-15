from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # API Endpoints (Replace with actual URLs)
    cs_api_url = "http://127.0.0.1:5000/compsci"
    national_api_url = "http://127.0.0.1:5000/national"

    # Fetch Data
    cs_response = requests.get(cs_api_url)
    national_response = requests.get(national_api_url)

    # Parse JSON Responses
    cs_colleges = cs_response.json() if cs_response.status_code == 200 else []
    national_colleges = national_response.json() if national_response.status_code == 200 else []

    # Extract unique states
    states = sorted(set(college['State'] for college in cs_colleges))

    return render_template('index.html', cs_colleges=cs_colleges, national_colleges=national_colleges, states=states)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
