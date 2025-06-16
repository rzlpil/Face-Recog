import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(layout="centered", page_title="Face Detection")

st.title("👤 Face Detection with TensorFlow.js (in Streamlit)")

st.markdown("Deteksi wajah langsung dari webcam menggunakan model TensorFlow.js. Halaman ini memuat kamera dan model di dalam iframe.")

# Jalankan server lokal di luar Streamlit:
# python -m http.server 8000
components.iframe("http://localhost:8000/face_detector.html", height=600, scrolling=True)
