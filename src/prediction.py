import joblib
import pandas as pd

# Load trained model and preprocessor
model = joblib.load("models/logistic_regression.pkl")
preprocessor = joblib.load("models/preprocessor.pkl")

def predict_churn(customer_data):
    """
    Predict whether a customer is likely to churn.
    """

    data = pd.DataFrame([customer_data])

    # Apply preprocessing
    data_processed = preprocessor.transform(data)

    # Make prediction
    prediction = model.predict(data_processed)[0]

    return prediction
if __name__ == "__main__":
    sample_customer = {
    "gender": "Male",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 12,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "DSL",
    "OnlineSecurity": "Yes",
    "OnlineBackup": "No",
    "DeviceProtection": "No",
    "TechSupport": "Yes",
    "StreamingTV": "No",
    "StreamingMovies": "No",
    "Contract": "One year",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Mailed check",
    "MonthlyCharges": 55.0,
    "TotalCharges": 660.0
}
        # We'll fill these values in the next step


    result = predict_churn(sample_customer)
    print("Churn prediction:", result)