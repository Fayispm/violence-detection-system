# Violence Detection System

## Overview

The Violence Detection System is a deep learning-based computer vision project designed to detect violent activities in videos in real time. The system analyzes video frames using machine learning techniques and classifies activities as violent or non-violent.

This project can be used in surveillance systems, public safety monitoring, and smart security applications.

---

## Features

* Real-time violence detection
* Video classification using deep learning
* Frame-by-frame video processing
* Computer vision-based analysis
* User-friendly prediction workflow
* Supports uploaded video files

---

## Technologies Used

* Python
* TensorFlow / Keras
* OpenCV
* NumPy
* Pandas
* Matplotlib
* Scikit-learn

---

## Project Structure

```text id="9td3oe"
Violence_Detection/
│
├── dataset/
├── notebooks/
├── models/
├── src/
├── app.py
├── train.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## How It Works

1. Video input is provided to the system.
2. Frames are extracted from the video.
3. Each frame is preprocessed and resized.
4. The trained deep learning model analyzes the frames.
5. The system predicts whether violence is detected or not.
6. Prediction results are displayed in real time.

---

## Installation

### Clone the Repository

```bash id="6h6ol1"
git clone https://github.com/Fayispm/violence-detection-system.git
```

### Navigate to Project Folder

```bash id="1v9a1u"
cd violence-detection-system
```

### Create Virtual Environment

```bash id="1yz5c8"
python -m venv .venv
```

### Activate Virtual Environment

#### Windows

```bash id="yqg4uq"
.venv\Scripts\activate
```

#### Linux/Mac

```bash id="03u0jy"
source .venv/bin/activate
```

### Install Dependencies

```bash id="pk9oml"
pip install -r requirements.txt
```

---

## Run the Project

```bash id="v8j2pr"
python app.py
```

or

```bash id="s8jlwm"
python realtime.py
```

---

## Dataset

The project uses a violence detection dataset containing violent and non-violent video samples for training and evaluation.

Example classes:

* Violence
* Non-Violence

---

## Applications

* Smart Surveillance Systems
* Public Safety Monitoring
* Crime Prevention
* Security Automation
* CCTV Monitoring

---

## Future Improvements

* Improve model accuracy
* Deploy as a web application
* Integrate live CCTV feed detection
* Add alert notification system
* Optimize real-time performance

---

## Author

Muhammed Fayiz

LinkedIn: https://www.linkedin.com/in/muhammed-fayis-4a5aa3321/

GitHub: https://github.com/Fayispm

---

## License

This project is created for educational and research purposes.
