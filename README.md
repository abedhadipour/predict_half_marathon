# half_marathon


# 🏃‍♂️ Half Marathon Finish Time Predictor

This project builds a regression-based model to predict half marathon finish times using training history and personal best times. It includes detailed exploratory data analysis (EDA), model evaluation, and a small web application using Streamlit.

---

## 📌 Overview

- Predicts finish times based on features like training volume, 5K personal best, and sex.
- Implements and compares multiple regression models:
  - Linear Regression
  - Ridge Regression
  - Lasso Regression
  
- Built for data science portfolio purposes.
- Provides a Streamlit app for users to test the model.

---

## 🚀 Demo

<img width="730" height="676" alt="image" src="https://github.com/user-attachments/assets/b68923e1-2e16-4099-a446-cabfa45d394e" />


---

## 📁 Project Structure

```bash
half_marathon/
├── data/                  # Raw and preprocessed data
├── notebooks/             # Jupyter notebooks containing EDA, modeling, comparisons, etc.,
├── models/                # Saved .pkl regression models and scalers
├── src/                   # Python scripts (i.e., prediction function)
├── app/                   # Streamlit web app
├── requirements.txt       # Dependencies
├── .gitignore
├── README.md
```

---

## 🧪 Getting Started

1. **Clone the repository:**

```bash
git clone https://github.com/abedhadipour/half_marathon.git
cd half_marathon
```

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv env
source env/bin/activate
# On Windows use `env\Scripts\activate`
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## ⚙️ Usage

You can use the model in two ways:

### 1. Python Function

Inside `src/predict.py`:

```python
from predict import predict_half_marathon_finish_time

input_data = {
    'ANNO': 1995,
    '2025_km': 500,
    '5K_PB': 1300,
    'total_km': 2500,
    'SESSO_M': 1
}

in which, "ANNO" would be the year of birth, "2025_km" would be the mileage in the last 4 months before the race, "5K_PB"
would be the 5K personal best record, "total_km" would the total mileage covered in the whole running career, and "SESSO_M"
would be the sex, 1: male, 0: female.
 
result = predict_half_marathon_finish_time(input_data)
print(result)  # e.g., '1:38:52'
```

### 2. Run the Streamlit App

```bash
streamlit run streamlit_app.py
```

---

## 📊 Data

The data includes around 2,300 entries 123 of which include information both regarding the race day and history of the racer such as:

- Total yearly kilometers
- Recent 5K race times
- Sex

---

## 🤖 Models

All models were evaluated with R², adjusted R², and 5-fold cross-validation. Ridge and Lasso showed slightly better generalization but only marginal gains over standard Linear Regression.

Final model is saved under `models/regression_model.pkl`.

---

## 🌐 Web App

A basic Streamlit interface allows users to input their race and training data and receive a predicted finish time. Try it locally with:

```bash
streamlit run streamlit_app.py
```

---

## 📦 Requirements

```txt
numpy
pandas
matplotlib
seaborn
statsmodels
scikit-learn
streamlit
joblib
```

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).
