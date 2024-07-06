import requests
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/hello', methods=['GET'])
def hello():
    visitor_ip = request.args.get('visitor_ip')
    visitor_name = request.args.get('visitor_name', 'Guest')
    
    if not visitor_ip:
        return jsonify({"error": "Visitor IP not provided"}), 400

    try:
        ipinfo_response = requests.get(f'https://ipinfo.io/{visitor_ip}/json')
        ipinfo_response.raise_for_status()
        ipinfo_data = ipinfo_response.json()
        
        ip = ipinfo_data.get('ip')
        city = ipinfo_data.get('city')

        if not city:
            return jsonify({"error": "City information not available"}), 500

        weather_api_key = 'ce703f28c689a16bcfbefe0544b5a96c'
        weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={weather_api_key}'
        weather_response = requests.get(weather_url)
        weather_response.raise_for_status()
        weather_data = weather_response.json()
        weather = weather_data.get('main', {}).get('temp')

        greeting = f"Hello, {visitor_name}!, the temperature is {weather} degrees Celsius in {city}"

        return jsonify({
            "client_ip": ip,
            "location": city,
            "greeting": greeting
        })
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
