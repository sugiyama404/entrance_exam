from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

"""
インデックスページを表示します。
Returns:
    JSON形式のレスポンス
"""
@app.route('/image/<dir1>/<dir2>/<filename>', methods=['POST'])
def index(dir1:str ,dir2:str ,filename:str):
    result = random.random()
    if result <= 0.9:
        response = {
            "success": "true",
            "message": "success",
            "estimated_data": {
                "class": 3,
                "confidence": 0.8683
            }
        }
    else:
        response = {
            "success": "false",
            "message": "Error:E50012",
            "estimated_data": {}
        }

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
