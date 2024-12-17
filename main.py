from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained ML model
try:
    model = joblib.load('fibonacci_model.pkl')
except Exception as e:
    model = None
    print(f"Failed to load model: {e}")

# Fallback recursive Fibonacci
memo = {}
def fallback_fib(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fallback_fib(n - 1) + fallback_fib(n - 2)
    return memo[n]

@app.route('/fib', methods=['GET'])
def fibonacci():
    n = int(request.args.get('n', 10))
    try:
        if model:
            result = model.predict([[n]])[0]  # Proper Solution (ML model)
        else:
            raise Exception("Model unavailable")
    except:
        result = fallback_fib(n)  # Fallback Solution (recursive)
    return jsonify({'result': result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

