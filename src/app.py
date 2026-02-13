from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "f1228154cd3b2b357fc51a901dd6e702"

@app.route("/weather")
def get_weather():
    city = request.args.get("city")

    if not city:
        return jsonify({"error": "Please provide a city name"}), 400

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return jsonify({"error": "City not found"}), 404

    result = {
        "city": city,
        "temperature": data["main"]["temp"],
        "condition": data["weather"][0]["description"]
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
