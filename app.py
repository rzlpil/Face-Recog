import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="centered", page_title="Face Detection")

st.title("👤 Face Detection with TensorFlow.js in Streamlit")

st.markdown("Iframe di bawah ini memuat HTML yang mengakses webcam dan mendeteksi wajah dengan model TensorFlow.js.")

# Ganti URL ini dengan alamat hosting GitHub Pages milikmu
components.iframe("https://rzlpil.github.io/Face-Recog/face_detector.html", height=600)
