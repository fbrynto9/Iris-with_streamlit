import streamlit as st
import pickle

# Function to load the trained model
def load_trained_model():
    with open('best_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    return model

# Function to predict using the loaded model
def predict(input_data, model):
    try:
        prediction = model.predict(input_data)[0]
        return f'Predicted Iris Species: {prediction}'
    except Exception as e:
        return f"Error predicting: {e}"

# Streamlit app
st.title('Iris Flower Prediction App')

# Input attributes
sepal_length = st.slider('Sepal Length', min_value=0.0, max_value=10.0, value=5.0)
sepal_width = st.slider('Sepal Width', min_value=0.0, max_value=10.0, value=3.5)
petal_length = st.slider('Petal Length', min_value=0.0, max_value=10.0, value=1.5)
petal_width = st.slider('Petal Width', min_value=0.0, max_value=10.0, value=0.2)

# Load the trained model
model = load_trained_model()

# Button to submit prediction
if st.button('Submit'):
    input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
    result = predict(input_data, model)
    st.success(result)

# Display NIM and name
st.sidebar.text("NIM: 2020230053")
st.sidebar.text("Name: Tri Febriyanto")