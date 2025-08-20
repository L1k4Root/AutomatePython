from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup as bs

app = Flask(__name__)

def get_rates(input_currency, output_currency, amount):
    """Fetch exchange rates from an external API."""
    url = f"https://www.x-rates.com/calculator/?from={input_currency}&to={output_currency}&amount={amount}#google_vignette"
    response = requests.get(url)
    soup = bs(response.content, 'html.parser')
    rate = soup.find("span", class_="ccOutputRslt").contents[0]
    
    
    return rate
    


@app.route('/')
def home():
    return "To access the API, use /api/<input_currency>-<output_currency>/"

@app.route('/api/<input_currency>-<output_currency>/', methods=['GET'])
def convert_currency(input_currency, output_currency):
    amount = 1
    rate = get_rates(input_currency, output_currency, amount)
    output = {
        "input_currency": input_currency,
        "output_currency": output_currency,
        "rate": rate
    }
    return jsonify(output)

app.run(debug=True)