# Smart Heart: Predicting Cardiovascular Disease with XGBoost
The prediction of cardiovascular disease (CVD) is crucial in healthcare analytics, aiming to identify at-risk individuals. This dataset provides valuable insights into forecasting CVD occurrence using various health attributes, enhancing early detection and preventive measures.

This Streamlit application predicts the presence or absence of cardiovascular disease based on input features such as age, gender, height, weight, blood pressure, cholesterol levels, glucose levels, smoking status, alcohol consumption, and physical activity level.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [File Structure](#file-structure)
- [Dependencies](#dependencies)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/cardiovascular-disease-prediction.git
    cd cardiovascular-disease-prediction
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure you have the trained model file (`xgb_model.pkl`) in the specified directory:
    ```plaintext
    D:/Jerushaa/AML/xgb_model.pkl
    ```

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and navigate to `http://localhost:8501`.

3. Fill out the form with the required information to get a prediction on cardiovascular disease.

## Model Training

The model used in this application is an XGBoost classifier trained on a dataset of cardiovascular disease records. The training process includes data preprocessing steps such as removing outliers and encoding categorical features.

To train the model (this step is optional if you already have the trained model):

1. Prepare your dataset and save it as a CSV file.
2. Load and preprocess the data.
3. Train the XGBoost model.
4. Save the trained model to a file using `joblib`.

