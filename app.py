import streamlit as st
import spam_streamlit as sp_st

html_temp = """
            <div style="background-color:green;padding:10px">
                <h1 style="color:white;text-align:center;">Spam Classification App</h1>
            </div>
            """

st.markdown(html_temp, unsafe_allow_html=True)

# Get user input
user_input = st.text_area("Enter Email Text Below")

# Clean email text
email = sp_st.clean_email_text(email_text=user_input)

if st.button("Predict"):
    # Prediction
    prediction = sp_st.get_predictions(text=email)

    if prediction[0] == 0:
        st.write("Prediction: ***Spam***")
    elif prediction[0] == 1:
        st.write("Prediction: ***Not Spam***")
