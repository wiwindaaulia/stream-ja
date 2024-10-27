import pickle
import numpy as np
import streamlit as st
import os

# Path to the saved model
model_path = 'penyakit_jantung.sav'

# Check if the model file exists
if not os.path.isfile(model_path):
    st.error("Model file not found. Please check the path.")
else:
    # Load the saved model
    model = pickle.load(open(model_path, 'rb'))

    # Web title
    st.title('Prediksi Penyakit Jantung')

    # Input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Umur', min_value=0, max_value=120, step=1)

    with col2:
        sex = st.selectbox('Jenis Kelamin', options=[0, 1], format_func=lambda x: 'Perempuan' if x == 0 else 'Laki-laki')

    with col3:
        cp = st.selectbox('Jenis Nyeri Dada', options=[0, 1, 2, 3], format_func=lambda x: {0: 'Tanpa Nyeri', 1: 'Nyeri Ringan', 2: 'Nyeri Sedang', 3: 'Nyeri Berat'}[x])

    with col1:
        trestbps = st.number_input('Tekanan Darah', min_value=0)

    with col2:
        chol = st.number_input('Nilai Kolesterol', min_value=0)

    with col3:
        fbs = st.selectbox('Gula Darah', options=[0, 1], format_func=lambda x: 'Normal' if x == 0 else 'Diabetes')

    with col1:
        restecg = st.selectbox('Hasil Elektrokardiografi', options=[0, 1, 2])

    with col2:
        thalach = st.number_input('Detak Jantung Maksimum', min_value=0)

    with col3:
        exang = st.selectbox('Induksi Angina', options=[0, 1])

    with col1:
        oldpeak = st.number_input('ST Depression', min_value=0.0)

    with col2:
        slope = st.selectbox('Slope', options=[0, 1, 2])

    with col3:
        ca = st.number_input('Nilai CA', min_value=0, max_value=4)

    with col1:
        thal = st.selectbox('Nilai Thal', options=[1, 2, 3, 6, 7], format_func=lambda x: {1: 'Normal', 2: 'Dari Akhir', 3: 'Defisiensi', 6: 'Fixed Defect', 7: 'Reversible Defect'}[x])

    # Variable for prediction result
    heart_diagnosis = ''

    # Button to make predictions
    if st.button('Prediksi Penyakit Jantung'):
        try:
            # Prepare input data
            input_data = [
                age, sex, cp, trestbps, chol, 
                fbs, restecg, thalach, exang, 
                oldpeak, slope, ca, thal
            ]

            # Make prediction
            heart_prediction = model.predict([input_data])

            # Determine the prediction result
            if heart_prediction[0] == 0:
                heart_diagnosis = 'Pasien Tidak Terkena Penyakit Jantung'
            else:
                heart_diagnosis = 'Pasien Terkena Penyakit Jantung'

            # Display result
            st.success(heart_diagnosis)

        except Exception as e:
            st.error(f"Terjadi kesalahan: {str(e)}")
