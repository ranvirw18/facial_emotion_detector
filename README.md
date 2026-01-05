🎭 Real-Time Emotion Detector (Tkinter + OpenCV + FER)

A real-time facial emotion detection desktop application built using Python, Tkinter, OpenCV, and the FER (Facial Expression Recognition) library.
The app captures live video from your webcam, detects faces, and displays the dominant emotion with confidence percentage in real time.

🚀 Features

📷 Live webcam feed using OpenCV

🙂 Real-time face & emotion detection

📊 Displays dominant emotion with confidence score

🖼️ Face bounding box overlay

🧠 Powered by FER with MTCNN face detection

🖥️ Simple and clean Tkinter GUI

🎛️ Start / Stop / Quit controls

🛠️ Tech Stack

Python 3.8+

Tkinter – GUI framework

OpenCV (cv2) – Video capture & image processing

FER – Facial emotion recognition

MTCNN – Accurate face detection

Pillow (PIL) – Image handling

Threading – Smooth real-time performance

📦 Installation
1️⃣ Clone the repository
git clone https://github.com/ranvirw18/emotion-detector-tkinter.git
cd emotion-detector-tkinter

2️⃣ Install dependencies
pip install opencv-python fer mtcnn pillow numpy


⚠️ If you face issues with TensorFlow:

pip install tensorflow

▶️ Usage

Run the application:

python emotion_detector_tkinter.py

Controls:

Start Camera → Begin emotion detection

Stop → Stop camera feed

Quit → Exit the application



🧠 How It Works

Webcam feed is captured using OpenCV

FER detects faces and extracts emotion probabilities

The dominant emotion is selected based on highest confidence

Face box & emotion label are drawn on the video frame

Tkinter updates the GUI in real time using threading

📊 Detected Emotions

Angry

Disgust

Fear

Happy

Sad

Surprise

Neutral

⚠️ Limitations

Accuracy depends on lighting and camera quality

Works best with a single face in frame

Emotion prediction is probabilistic, not absolute

🌱 Future Improvements

Multiple face emotion tracking

Emotion history & analytics

Dark/light UI themes

Emotion-based music or UI response

Save emotion logs to CSV

🤝 Contributing

Contributions are welcome!
Feel free to fork the repository, open issues, or submit pull requests.

📄 License

This project is licensed under the MIT License.
