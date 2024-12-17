import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import mlflow
import mlflow.sklearn

# Generate Fibonacci dataset
def generate_fib_data(n):
    data = []
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    for i, val in enumerate(fib):
        data.append([i, val])
    return data

# Generate dataset
data = generate_fib_data(50)  # First 50 Fibonacci numbers
df = pd.DataFrame(data, columns=['index', 'value'])

# Prepare features (X) and target (y)
X = df[['index']]
y = df['value']

# Initialize and train the model
model = LinearRegression()

# Start MLflow tracking
with mlflow.start_run():
    # Train the model
    model.fit(X, y)

    # Predict and evaluate
    y_pred = model.predict(X)
    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)

    # Log parameters, metrics, and model with MLflow
    mlflow.log_param("model_type", "LinearRegression")
    mlflow.log_param("data_size", len(df))
    mlflow.log_metric("mse", mse)
    mlflow.log_metric("r2", r2)

    # Log the model
    mlflow.sklearn.log_model(model, "fibonacci_regressor")

    # Save the model locally
    joblib.dump(model, 'fibonacci_model.pkl')
    print("Model trained and saved as 'fibonacci_model.pkl'")
    print(f"Metrics - MSE: {mse}, R2: {r2}")
