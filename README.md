In this project, we have developed a Machine Learning (ML) service to predict Fibonacci numbers using a Linear Regression model. The main objective of this task was to create an ML service that can solve a specific problem by leveraging a trained model and exposing it via a web service. The solution is designed to be scalable, reliable, and fault-tolerant.

Task Definition
Problem Statement: The task is to predict the Fibonacci numbers based on the index position in the sequence. Given an index n, the goal is to predict the corresponding Fibonacci number at that position.

Input Description: The input to the service is a query parameter n, representing the index of the Fibonacci sequence for which we want to predict the value. The input is expected to be an integer value representing the index (e.g., n=10 for the 10th Fibonacci number).

Output Description: The output is a JSON response containing the predicted Fibonacci value for the given index. For example, if n=10, the output might look like:

json
Copy code
{
  "result": 55
}
Approach:

The task is solved using a Linear Regression model. Although Fibonacci numbers are based on a recursive pattern, we use Linear Regression for simplicity and demonstration purposes. In this case, the model learns to predict Fibonacci numbers based on the index in the sequence.
We use a dataset of Fibonacci numbers up to the 50th index, which is used to train the model.
Fallback Solution: A simple fallback solution (such as a pre-calculated Fibonacci lookup table) can be used in case the model experiences issues, ensuring reliability and availability of the service.
Dataset
Dataset: Generate a dataset containing the first 50 Fibonacci numbers. The dataset is structured with two columns: index (representing the position in the sequence) and value (the corresponding Fibonacci number).
This dataset is used to train the Linear Regression model to predict Fibonacci numbers based on their index.
Runtime Architecture
The service is built using Flask for creating the API that exposes the Fibonacci prediction functionality. The model is trained using scikit-learn and saved using joblib. The service runs inside a Docker container, making it portable and easy to deploy.

The service follows a microservices architecture, where:

The Flask app handles HTTP requests and invokes the model for predictions.
MLflow is used for experiment tracking and logging model parameters, metrics (such as R2 score and Mean Squared Error), and the trained model itself.
The service is containerized using Docker and can be deployed and scaled using Kubernetes. 
