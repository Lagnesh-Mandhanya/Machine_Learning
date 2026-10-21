

import streamlit as st
import joblib
from pathlib import Path

st.set_page_config(
    page_title="Email Spam Detector",
    page_icon="📧",
    layout="centered"
)

MODEL_PATH = Path(__file__).parent / "spam_detection_model.pkl"


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


try:
    model = load_model()
except Exception as error:
    st.error(f"Unable to load the trained model: {error}")
    st.info(
        "Check that spam_detection_model.pkl is in "
        "the same folder as app.py."
    )
    st.stop()


# Sidebar
with st.sidebar:
    st.header("About the Project")
    st.write("An ML application that classifies email text.")
    st.markdown("**Technologies used**")
    st.write("- Python")
    st.write("- Scikit-learn")
    st.write("- TF-IDF")
    st.write("- Multinomial Naive Bayes")
    st.write("- Streamlit")

    st.divider()
    st.caption(
        "Messages entered here are processed by this "
        "local application. This app does not connect "
        "to your email inbox."
    )


# Main page
st.title("📧 Email Spam Detector")
st.write(
    "Check whether an email message resembles spam "
    "or legitimate email based on patterns learned "
    "by the trained model."
)

with st.expander("Try an example"):
    st.write("**Possible spam:**")
    st.code(
        "Subject: You have won a prize\n"
        "Message: Claim your cash reward now!"
    )
    st.write("**Possible legitimate email:**")
    st.code(
        "Subject: Project meeting\n"
        "Message: Our meeting is scheduled for tomorrow."
    )

subject = st.text_input(
    "Email subject",
    placeholder="Enter the subject"
)

body = st.text_area(
    "Email message",
    height=180,
    placeholder="Paste the email message here..."
)

check = st.button(
    "Check Email",
    type="primary",
    use_container_width=True
)

if check:
    email_text = f"{subject}\n{body}".strip()

    if not email_text:
        st.warning("Please enter a subject or message.")
    else:
        try:
            prediction = int(model.predict([email_text])[0])
            probabilities = model.predict_proba([email_text])[0]
            class_index = list(model.classes_).index(prediction)
            confidence = probabilities[class_index] * 100

            st.subheader("Analysis Result")

            if prediction == 1:
                st.error("🚨 This email is classified as SPAM")
            elif prediction == 0:
                st.success("✅ This email is classified as NOT SPAM")
            else:
                st.warning(f"Predicted class: {prediction}")

            st.metric("Model confidence", f"{confidence:.2f}%")
            st.caption(
                "Confidence is the model's estimated probability, "
                "not proof that an email is safe."
            )

        except Exception as error:
            st.error(f"Prediction failed: {error}")

st.divider()
st.caption(
    "Academic ML project | Results may be inaccurate "
    "for new or unfamiliar email patterns."
)
