# Internet Provider Churn Rate Prediction

This project aims to predict the churn rate of customers for an internet provider. By analyzing customer data, the model can help identify customers who are likely to leave the service, allowing the provider to take proactive measures to retain them.

## Features

- Data preprocessing and cleaning
- Exploratory data analysis (EDA)
- Model building and evaluation
- Prediction of customer churn

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn

## Prerequisites

- Python 3.x
- Jupyter Notebook or any other preferred IDE

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/iqbaljntra/INTERNET-PROVIDER-CHURN-RATE-PREDICTION.git
    cd INTERNET-PROVIDER-CHURN-RATE-PREDICTION
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Open the Jupyter Notebook:
    ```bash
    jupyter notebook
    ```

2. Open the notebook file `churn_prediction.ipynb` and run the cells to execute the code step-by-step.


## Data Description

The dataset contains various features related to the customers of the internet provider. Key features include:

- `customerID`: Unique identifier for each customer
- `tenure`: Number of months the customer has been with the provider
- `MonthlyCharges`: The amount charged to the customer monthly
- `TotalCharges`: The total amount charged to the customer
- `Churn`: Whether the customer has churned (Yes/No)

## Model Building

The model is built using the following steps:

1. Data preprocessing: Handling missing values, encoding categorical features, etc.
2. Exploratory Data Analysis (EDA): Understanding the data distribution and relationships between features.
3. Model training: Using various algorithms like Logistic Regression, Decision Trees, Random Forests, etc.
4. Model evaluation: Evaluating the performance of the models using metrics like accuracy, precision, recall, and F1-score.

## Acknowledgements

- The dataset used for this project is fictional and created for educational purposes.
- Thanks to the contributors of various Python libraries used in this project.

## Contact

If you have any questions or suggestions, feel free to contact me at [your email address].


