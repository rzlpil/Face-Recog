import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="centered")
st.title("👤 Face Detection in Streamlit (TFJS)")

# Ganti URL model dengan link mentah (raw) dari GitHub kamu
model_url = "https://raw.githubusercontent.com/username/your-repo/main/model/model.json"

html_code = f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Face Detection</title>
  <style>
    body {{ text-align: center; font-family: Arial; background: #f0f0f0; }}
    canvas, video {{ border: 1px solid black; display: block; margin: 10px auto; }}
  </style>
</head>
<body>
  <h2>Webcam Face Detection</h2>
  <video id="video" width="640" height="480" autoplay muted></video>
  <canvas id="canvas" width="640" height="480"></canvas>

  <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs"></script>
  <script>
    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    let model;

    async function setupCamera() {{
      const stream = await navigator.mediaDevices.getUserMedia({{
        video: {{ width: 640, height: 480 }},
        audio: false
      }});
      video.srcObject = stream;
      return new Promise(resolve => {{
        video.onloadedmetadata = () => resolve(video);
      }});
    }}

    async function loadModel() {{
      model = await tf.loadGraphModel('{model_url}');
      console.log("Model loaded");
    }}

    async function detectFaces() {{
      tf.engine().startScope();
      const input = tf.browser.fromPixels(video).toFloat().expandDims(0);
      const predictions = await model.executeAsync(input);
      const boxes = predictions[0].arraySync();
      const scores = predictions[1].arraySync();
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      for (let i = 0; i < boxes.length; i++) {{
        if (scores[i] > 0.5) {{
          const [ymin, xmin, ymax, xmax] = boxes[i];
          const x = xmin * video.width;
          const y = ymin * video.height;
          const width = (xmax - xmin) * video.width;
          const height = (ymax - ymin) * video.height;
          ctx.beginPath();
          ctx.rect(x, y, width, height);
          ctx.lineWidth = 2;
          ctx.strokeStyle = 'red';
          ctx.stroke();
        }}
      }}
      tf.dispose(predictions);
      tf.engine().endScope();
      requestAnimationFrame(detectFaces);
    }}

    async function main() {{
      await setupCamera();
      video.play();
      await loadModel();
      detectFaces();
    }}

    main();
  </script>
</body>
</html>
"""

components.html(html_code, height=700)
