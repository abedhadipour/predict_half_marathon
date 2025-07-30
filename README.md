# half_marathon


# Half Marathon Finish Time Predictor

This project builds a regression-based model to predict half marathon finish times using training history and personal best times. It includes detailed exploratory data analysis (EDA), model evaluation, and a small web application using Streamlit.

---

## 📌 Overview

- Predicts finish times based on 4 different features: total training volume until the race day, mileage during the last 4 month before the race, 5 Kilometer personal best record, and sex.

- Implements and compares multiple regression models:
  - Simple Linear Regression
  - Ridge Regression
  - Lasso Regression
  - Random Forest
  
- This is built for data science portfolio purposes and provides a Streamlit app for users to test the model with their personal data.

---

## 🚀 Demo


Please click on the link below to use the application to predict your half-marathon performance:

https://predicthalfmarathon-8ufp2cmcqmrexgtdgqcmgj.streamlit.app/


---

## 📁 Project Structure

```bash
half_marathon/
├── data/                  # Raw and preprocessed data (to train the random forest model)
├── notebooks/             # Jupyter notebooks containing EDA, models, plots, comparisons, etc.,
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

2. **Create a virtual environment (optional)**

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

The data includes around 2,300 entries, 123 of which include information both regarding the race day and history of the racer such as:

- Total kilometers covered during running career and the last 4 months before the race
- 5K and 10K personal best record times
- Race data such as Sex, race finish time, country of origin, etc.

---

## 🤖 Models

All models were evaluated with R², adjusted R², and 5-fold cross-validation. Ridge and Lasso showed slightly better generalization but only marginal gains over standard Linear Regression. The Random Forest Regressor achieved slightly higher R² scores across training, test, and cross-validation sets, its mean absolute percentage error (MAPE) was higher than that of the simpler Linear Regression model.

Given the close performance and the added benefit of interpretability and simplicity, the final prediction function was built using ordinary least squares Linear Regression. The Random Forest results are included for comparison and to demonstrate further model exploration. 

Final model is saved under `models/regression_model.pkl`.

---

## 🌐 Web App

A basic Streamlit interface allows users to input their data and receive a predicted finish time. Try it locally with:

```bash
streamlit run streamlit_app.py
```

or using the following link:

https://predicthalfmarathon-8ufp2cmcqmrexgtdgqcmgj.streamlit.app/

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

## Limitations



This is indeed a beginner level peek into the question of performance prediction in the context of (half)marathon considering the size of the sample and the range of the methods used. Here are some of the limitations some of which may be slowly addressed in the commits to come:

 - The sample size is definitely small. Looking only at the profiles of ~120 individuals cannot produce highly reliable indices for performance prediction.

 - The sample is not representative. The absolute majority of the included athletes are of Italian nationality and due to the very likely highly local participation, the majority of those may be of the origins or residents of the Veneto region. These are issues to deal with when conducting an analysis to then be able to generalize its findings.

 - The potential regressors that were available for the current analysis were of course limited. Potentially significant variables that were not available to us in the current analysis included but are not limited to:

	- VO2Max (Measured in milliliters of O2 per Kg of body weight per minute, which simply put, captures the ability of the body to efficiently consume Oxygen)
 
	- The spread of the running activity during the running career of the individual. Here we only got two variables that shows how prior activity before the race, i.e., the last 4 months and the total km. However, it may be the case that some person ran 1000 km 3 years ago and covered very little thereafter. This can be problematic as you certainly want to be able to track the carry-over effect and one needs to take that in consideration. In a nutshell, the trend is important.
	
	- Heart rate and heart rate variability before, during, and after preparation runs could act as a significant predictor of race performance. These data were not available for this analysis but may provide a great insight about the cardiovascular capacity of the runner and much they can push for a personal best on the race day.  

 	- Elevation gain is another factor that may provide insight about the race day performance. How much hill work a runner does and in general the type and variety of exercises they engage in to prepare themselves for the race may be insightful.
 




## 📝 License

This project is licensed under the [MIT License](LICENSE).
