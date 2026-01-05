"""
emotion_detector_tkinter.py

Tkinter + OpenCV + FER-based real-time Emotion Detector
"""

import cv2
import numpy as np
from tkinter import Tk, Label, Button, Canvas
from PIL import Image, ImageTk
from fer import FER
import threading
import time

 
class EmotionDetectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Emotion Detector — Feel the Frame")
        self.root.configure(bg="#111111")

        self.vs = None
        self.thread = None
        self.stopEvent = threading.Event()

        # FER emotion detector
        self.detector = FER(mtcnn=True)

        # Canvas for video feed
        self.canvas = Canvas(root, width=640, height=480, bg="#000000", highlightthickness=0)
        self.canvas.pack(padx=10, pady=10)

        # Label for detected emotion
        self.label = Label(root, text="Emotion: --", font=("Helvetica", 18, "bold"), fg="cyan", bg="#111111")
        self.label.pack()

        # Control buttons
        self.btn_start = Button(root, text="Start Camera", command=self.start_camera, bg="#222", fg="white")
        self.btn_start.pack(pady=4)
        self.btn_stop = Button(root, text="Stop", command=self.stop_camera, bg="#222", fg="white")
        self.btn_stop.pack(pady=4)
        self.btn_quit = Button(root, text="Quit", command=self.on_close, bg="#500", fg="white")
        self.btn_quit.pack(pady=4)

    def start_camera(self):
        if self.vs is None:
            self.vs = cv2.VideoCapture(0)
        if not self.vs.isOpened():
            self.label.config(text="Error: Camera not accessible.")
            return

        self.stopEvent.clear()
        self.thread = threading.Thread(target=self.video_loop, daemon=True)
        self.thread.start()
        self.label.config(text="Detecting emotions...")

    def stop_camera(self):
        self.stopEvent.set()
        if self.vs:
            try:
                self.vs.release()
            except:
                pass
            self.vs = None
        self.label.config(text="Camera stopped.")

    def video_loop(self):
        while not self.stopEvent.is_set():
            ret, frame = self.vs.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)  # mirror effect

            # Detect emotions
            try:
                results = self.detector.detect_emotions(frame)
                if results:
                    (x, y, w, h) = results[0]["box"]
                    emotions = results[0]["emotions"]
                    dominant = max(emotions, key=emotions.get)
                    confidence = emotions[dominant] * 100

                    # Draw face rectangle
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
                    cv2.putText(frame, f"{dominant} ({confidence:.1f}%)", (x, y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
                    self.label.config(text=f"Emotion: {dominant.capitalize()} ({confidence:.1f}%)")
                else:
                    self.label.config(text="Emotion: --")
            except Exception as e:
                self.label.config(text=f"Error: {e}")

            # Convert frame to ImageTk
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            imgtk = ImageTk.PhotoImage(image=image)
            self.canvas.create_image(0, 0, anchor="nw", image=imgtk)
            self.canvas.image = imgtk

            time.sleep(0.03)

    def on_close(self):
        self.stop_camera()
        self.root.quit()
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    app = EmotionDetectorApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()
