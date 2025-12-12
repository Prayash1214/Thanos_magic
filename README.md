Webcam Image Blend (OpenCV)

This small project is made for learning and having fun with OpenCV.
It behaves a bit like those playful “snap” effects — you can fade a chosen image in and out over your live webcam feed.

🎯 What It Does

Opens your webcam and continuously shows your video feed.

Loads a reference image from your system.

Smoothly blends that image into the live feed using a fade-in / fade-out effect.

Lets you toggle the effect using keyboard controls.

🎮 Controls
Key	Action
c	Fade the image in over the webcam feed
v	Fade the image out
q	Quit the program

The blending uses a gradually changing opacity value to create a smooth transition rather than an instant swap.

🛠️ Requirements

Python

OpenCV (cv2)

Webcam

Install OpenCV (if not already installed):

pip install opencv-python

📸 How It Works (Conceptually)

The webcam frame is captured and flipped horizontally to simulate a mirror view.

The external image is resized to match the frame’s dimensions.

An opacity variable slowly increases or decreases depending on which key you press.

Both images are then combined using weighted blending.

Everything updates in real-time for a smooth visual effect.

🚀 Purpose

This project is mainly for practice with:

OpenCV

Real-time video processing

Image blending techniques

Interaction using keyboard events

It’s a lightweight experiment built for learning, exploring, and having fun with computer vision.
