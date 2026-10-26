# Student Mental Health Score Predictor

A machine learning web application that estimates a student's mental health score based on lifestyle habits, academic activities, sleep patterns, stress levels, and social media usage.

The project combines a trained machine learning model with a FastAPI backend and an interactive frontend built using HTML, CSS, and JavaScript.

## Features

- **Machine Learning Prediction:** Uses a trained Random Forest regression pipeline to estimate a mental health score.
- **Lifestyle Analysis:** Accepts study hours, sleep duration, physical activity, and social media usage.
- **Student Information:** Takes age, gender, country, academic level, and other relevant inputs.
- **REST API:** Uses FastAPI to handle prediction requests.
- **Input Validation:** Uses Pydantic to validate incoming data.
- **Interactive Frontend:** Provides a user-friendly interface for entering details and viewing predictions.
- **Automated Preprocessing:** Applies the preprocessing steps saved with the trained model.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data handling |
| NumPy | Numerical operations |
| Scikit-learn | Machine learning and preprocessing |
| Random Forest Regressor | Score prediction |
| FastAPI | Backend API |
| Pydantic | Request validation |
| HTML | Webpage structure |
| CSS | Styling and layout |
| JavaScript | Frontend interactions |
| Git and GitHub | Version control |

## Project Structure

```text
Student_Mental_Health_Predictor/
├── main.py
├── Mental_Health_Model.pkl
├── index.html
├── style.css
├── script.js
├── requirements.txt
├── ML_Project.ipynb
└── Student Social Media And Mental Health Impact.csv
```

## Dataset

The project uses student-related data containing features such as:

- Age, gender, and country
- Academic level
- Most-used social media platform
- Purpose of social media use
- Average daily usage hours
- Daily phone unlocks
- Study hours
- Physical activity hours
- Sleep hours per night
- Stress level

The model uses these features to estimate the target variable, `Mental_Health_Score`.

## How It Works

1. The user enters student information through the frontend.
2. JavaScript sends the information to the FastAPI `/predict` endpoint.
3. FastAPI validates the submitted data.
4. The saved machine learning pipeline preprocesses the inputs and generates a prediction.
5. The API returns the estimated score.
6. The frontend displays the result to the user.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Lagnesh-Mandhanya/machine_learning.git
cd machine_learning/Student_Mental_Health_Predictor
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Start the FastAPI backend

```bash
python -m uvicorn main:app --reload
```

The API will be available locally at:

`http://127.0.0.1:8000`

### 5. Open the API documentation

Visit:

`http://127.0.0.1:8000/docs`

Use the interactive documentation to test the `/predict` endpoint.

### 6. Run the frontend

Open `index.html` using the VS Code Live Server extension or another local static web server.

Ensure that the API URL configured in `script.js` points to the running backend. For local development, use:

```javascript
const API_BASE = "http://127.0.0.1:8000";
```

## API Endpoint

### `POST /predict`

Accepts student information and returns a predicted mental health score.

Example response:

```json
{
  "predicted_mental_health_score": 5.76
}
```

The number above is an illustrative example, not a guaranteed result for every input.

## Future Improvements

- Deploy the application online.
- Improve validation of input categories and data quality.
- Add informative visualizations for lifestyle factors.
- Improve accessibility and mobile responsiveness.
- Evaluate model performance on suitable unseen data.
- Add automated tests for the API and frontend.

## Limitations and Responsible Use

This project is intended for educational and machine learning demonstration purposes. Its output is a model-estimated score, not a clinical assessment, mental health diagnosis, or substitute for professional support.

Predictions depend on the quality and representativeness of the dataset and the model's training process. They should not be used for medical decisions.

## Author

**Lagnesh Mandhanya**

- GitHub: [Lagnesh-Mandhanya](https://github.com/Lagnesh-Mandhanya)

---

If you find this project useful, feel free to explore the code and learn more about machine learning, model deployment, and full-stack development.
