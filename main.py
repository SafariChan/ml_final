<<<<<<< HEAD
from flask import Flask, request, jsonify

app = Flask(__name__)

memo = {}

def fib(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]

@app.route('/fib', methods=['GET'])
def fibonacci():
    n = int(request.args.get('n', 10))
    return jsonify({'result': fib(n)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
=======
from flask import Flask, request, jsonify

app = Flask(__name__)

memo = {}

def fib(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]

@app.route('/fib', methods=['GET'])
def fibonacci():
    n = int(request.args.get('n', 10))
    return jsonify({'result': fib(n)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
>>>>>>> 984116590b372c42be01395146a901379956eda7
