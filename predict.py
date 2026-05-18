import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.applications import MobileNetV2

IMG_SIZE = 224
SEQUENCE_LENGTH = 30

model = load_model("model/violence_model.h5")

base_model = MobileNetV2(
    weights="imagenet",
    include_top=False,
    pooling="avg",
    input_shape=(224, 224, 3)
)

def extract_frames(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []

    while len(frames) < SEQUENCE_LENGTH:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (IMG_SIZE, IMG_SIZE))
        frame = frame / 255.0
        frames.append(frame)

    cap.release()

    while len(frames) < SEQUENCE_LENGTH:
        frames.append(frames[-1])

    return np.array(frames)

def predict_video(video_path):
    frames = extract_frames(video_path)

    features = []
    for frame in frames:
        frame = np.expand_dims(frame, axis=0)
        feature = base_model.predict(frame, verbose=0)
        features.append(feature.flatten())

    features = np.array(features)
    features = np.expand_dims(features, axis=0)

    pred = model.predict(features)
    
    return "Violence" if np.argmax(pred) == 1 else "Non-Violence"


# TEST
video = "violence_video2.mp4"
print("Prediction:", predict_video(video))