import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle  # Importing the pickle module


# Function to perform prediction
def predict_placement(new_data):
    # Load the trained model
    with open('placement_model.pkl', 'rb') as f:
        model = pickle.load(f)

    # Perform prediction
    prediction = model.predict(new_data)
    probability = model.predict_proba(new_data)[0][1]  # Probability of being placed

    return prediction, probability


# Main function to define the Streamlit app
def main():
    st.title("Placement Prediction")

    # Create form for input fields
    with st.form("placement_form"):
        st.subheader("Input Details")

        # Input fields
        gender = st.selectbox("Gender", ["Male", "Female"])
        gender_numeric = 0 if gender == "Male" else 1
        ssc_p = st.number_input("SSC Percentage", min_value=0.0, max_value=100.0, step=0.01, value=67.0)
        ssc_b = st.selectbox("SSC Board", ["Central", "Others"], index=0)
        ssc_b_numeric = 0 if ssc_b == "Central" else 1
        hsc_p = st.number_input("HSC Percentage", min_value=0.0, max_value=100.0, step=0.01, value=91.0)
        hsc_b = st.selectbox("HSC Board", ["Central", "Others"], index=0)
        hsc_b_numeric = 0 if hsc_b == "Central" else 1
        hsc_s = st.selectbox("HSC Stream", ["Science", "Commerce", "Arts"], index=0)
        hsc_s_numeric = 0 if hsc_s == "Science" else 1 if hsc_s == "Commerce" else 2
        degree_p = st.number_input("Degree Percentage", min_value=0.0, max_value=100.0, step=0.01, value=58.0)
        degree_t = st.selectbox("Degree Type", ["Sci&Tech", "Comm&Mgmt", "Others"], index=0)
        degree_t_numeric = 0 if degree_t == "Sci&Tech" else 1 if degree_t == "Comm&Mgmt" else 2
        workex = st.selectbox("Work Experience", ["Yes", "No"], index=0)
        workex_numeric = 1 if workex == "Yes" else 0
        etest_p = st.number_input("E-Test Percentage", min_value=0.0, max_value=100.0, step=0.01, value=55.0)
        specialisation = st.selectbox("Specialisation", ["Mkt&Fin", "Mkt&HR"], index=0)
        specialisation_numeric = 0 if specialisation == "Mkt&Fin" else 1
        mba_p = st.number_input("MBA Percentage", min_value=0.0, max_value=100.0, step=0.01, value=58.8)

        submitted = st.form_submit_button("Predict Placement")

    # Prediction logic
    if submitted:
        new_data = pd.DataFrame({
            'gender': [gender_numeric],
            'ssc_p': [ssc_p],
            'ssc_b': [ssc_b_numeric],
            'hsc_p': [hsc_p],
            'hsc_b': [hsc_b_numeric],
            'hsc_s': [hsc_s_numeric],
            'degree_p': [degree_p],
            'degree_t': [degree_t_numeric],
            'workex': [workex_numeric],
            'etest_p': [etest_p],
            'specialisation': [specialisation_numeric],
            'mba_p': [mba_p],
        })

        prediction, probability = predict_placement(new_data)

        if prediction == 1:
            st.write("Placed")
            st.write(f"You will be placed with a probability of {probability:.2f}")
        else:
            st.write("Not Placed")


# Entry point of the script
if __name__ == "__main__":
    main()
