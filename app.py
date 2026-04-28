from flask import Flask, request, render_template, jsonify
import os
import pickle

application = Flask(__name__)
app = application

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, 'model/model_lr.pkl'), 'rb') as f:
    model = pickle.load(f)

with open(os.path.join(BASE_DIR, 'model/vectorization.pkl'), 'rb') as f:
    vector = pickle.load(f)

print("Model Loaded")
print("Vocab size:", len(vector.vocabulary_))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['POST'])
def predict_datapoint():
    try:
        data = request.get_json(force=True)
        news = data.get('news', '').strip()

        if not news:
            return jsonify({"error": "Empty input"}), 400

        vec = vector.transform([news])

        result = model.predict(vec)

        prediction = "Real News" if result[0] == 1 else "Fake News"

        return jsonify({"result": prediction})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)