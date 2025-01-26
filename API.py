from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)


json_path = 'putanja/do/vasih/podataka.json' 
data = pd.read_json(json_path)

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)