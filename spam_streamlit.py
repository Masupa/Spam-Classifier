import re
import string
import numpy as np

# Necessary Imports for Keras
from keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model


# Function to clean email text
def clean_email_text(email_text):
    """
    :param email_text: Text from email
    :return: Text stripped off from all characters
    """

    # Remove hyperlink
    email = re.sub(r'http\S+', "", email_text)

    # Make lower
    email = email.lower()

    # Remove number
    email = re.sub(r'\d+', '', email)

    # Remove punctuation
    email = email.translate(str.maketrans(dict.fromkeys(string.punctuation)))

    # Remove white space
    email = email.strip()

    # Replace new_line
    email = email.replace('\n', '')

    # Return email text
    return email


def get_predictions(text):
    """
    :param text:
    :return:
    """
    # Load the tokenizer object
    tokenizer_file = "tokenizer.pkl"
    tokenizer = pickle.load(open(tokenizer_file, "rb"))

    # Prepare user input
    text = [text.split(" ")]
    text_seq = tokenizer.texts_to_sequences(text)
    padded_text_seq = pad_sequences(text_seq, maxlen=2000)

    # Load the model
    model_file = "spam_model.h5"
    model = load_model(model_file, compile=True)

    prediction = model.predict(padded_text_seq)
    return np.argmax(prediction, axis=1)
