# Email Spam Detection System

## Overview
The Email Spam Detection System is a machine-learning application that classifies email text as spam or legitimate. It uses text preprocessing and supervised machine learning to identify patterns commonly associated with spam messages.

## Features
- Classifies email subjects and message bodies.
- Displays the predicted class and estimated model confidence.
- Provides a simple web interface built with Streamlit.
- Uses a trained scikit-learn pipeline for predictions.

## Technologies Used
- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorization
- Multinomial Naive Bayes
- Streamlit
- Joblib

## How It Works
1. Email text is provided by the user.
2. TF-IDF converts the text into numerical features.
3. The trained Multinomial Naive Bayes model predicts the class.
4. The application displays the prediction and estimated probability.

## Model Evaluation
Evaluation on the project's held-out test set:

| Metric | Result |
|---|---:|
| Accuracy | 98.14% |
| Precision | 100% |
| Recall | 88.66% |
| F1-score | 93.99% |

These results apply to the dataset and test split used during development. Performance may differ on modern or unseen emails.

## Run Locally
1. Install Python 3.
2. Clone or download this repository.
3. Open a terminal in the project directory.
4. Create and activate a virtual environment.
5. Install the dependencies.
6. Run the application.

Example commands for Windows Command Prompt:

```cmd
py -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Place `spam_detection_model.pkl` in the same directory as `app.py` before running the app.

## Limitations
- The model was trained on an older public email corpus.
- Predictions may be incorrect for new spam techniques or unfamiliar messages.
- Model confidence is not a guarantee of correctness or safety.
- The application does not connect directly to an email inbox.

## Future Improvements
- Evaluate the model on newer email datasets.
- Compare additional machine-learning algorithms.
- Add automated unit tests and error handling.
- Improve the interface and deployment process.

## Disclaimer
This project is intended for educational purposes. Do not rely on its predictions as the sole basis for deciding whether an email is safe.
