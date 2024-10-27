import pickle
import numpy as np
import streamlit as st

# Load the saved model
model = None
try:
    with open('penyakit_jantung.sav', 'rb') as model_file:
        model = pickle.load(model_file)
except FileNotFoundError:
    st.error("Error: File 'penyakit_jantung.sav' not found.")
except ModuleNotFoundError as e:
    st.error(f"Error: Missing module - {e}.")
except Exception as e:
    st.error(f"Other error occurred: {e}")

# Web title
st.title('Prediksi Penyakit Jantung')

# Create input columns
col1, col2, col3 = st.columns(3)

with col1:
    age = st.text_input('Umur', '0')

with col2:
    sex = st.selectbox('Jenis Kelamin', ('0', '1'))  # 0 for Female, 1 for Male

with col3:
    cp = st.selectbox('Jenis Nyeri Dada', ('0', '1', '2', '3'))

with col1:
    trestbps = st.text_input('Tekanan Darah', '0')

with col2:
    chol = st.text_input('Nilai Kolesterol', '0')

with col3:
    fbs = st.selectbox('Gula Darah > 120 mg/dl', ('0', '1'))  # 1 if True, 0 if False

with col1:
    restecg = st.selectbox('Hasil Elektrokardiografi', ('0', '1', '2'))

with col2:
    thalach = st.text_input('Detak Jantung Maksimum', '0')

with col3:
    exang = st.selectbox('Induksi Angina', ('0', '1'))  # 1 if True, 0 if False

with col1:
    oldpeak = st.text_input('ST Depression', '0')

with col2:
    slope = st.selectbox('Slope', ('0', '1', '2'))

with col3:
    ca = st.selectbox('Nilai CA', ('0', '1', '2', '3', '4'))

with col1:
    thal = st.selectbox('Nilai Thal', ('0', '1', '2', '3'))

# Prediction result variable
heart_diagnosis = ''

# Prediction button
if st.button('Prediksi Penyakit Jantung'):
    if model is not None:  # Check if model is loaded
        try:
            # Convert inputs to float
            input_data = [
                float(age), float(sex), float(cp), float(trestbps), float(chol), 
                float(fbs), float(restecg), float(thalach), float(exang), 
                float(oldpeak), float(slope), float(ca), float(thal)
            ]

            # Perform prediction
            heart_prediction = model.predict([input_data])

            # Display the prediction result
            if heart_prediction[0] == 0:
                heart_diagnosis = 'Pasien Tidak Terkena Penyakit Jantung'
            else:
                heart_diagnosis = 'Pasien Terkena Penyakit Jantung'

            st.success(heart_diagnosis)

        except ValueError:
            st.error("Please enter all values in numeric format.")
        except Exception as e:
            st.error(f"Error during prediction: {str(e)}")
    else:
        st.error("Model not loaded. Please check the file and try again.")
