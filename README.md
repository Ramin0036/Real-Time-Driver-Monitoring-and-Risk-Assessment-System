# Real-Time Driver Monitoring and Risk Assessment System

A real-time Driver Monitoring System (DMS) that analyzes driver alertness, attention, and behavior on the fly.

## Demo

Real-time dashboard output:

<img width="400" height="192" alt="gif" src="https://github.com/user-attachments/assets/99a6428c-3bba-459d-ba51-6f633d542629" />

---

## About the Project

This project is a prototype of a Driver Monitoring System designed and implemented to analyze driver alertness, attention, and behavior in real time. The system uses **Python, OpenCV, MediaPipe Face Mesh, and YOLO** to process incoming camera video in real time and extract several behavioral driver indicators simultaneously.

The goal of the project is to demonstrate a complete Driver Monitoring pipeline: from image acquisition to feature extraction, behavior analysis, decision-making, and event logging. For technical details of each module, see [ARCHITECTURE.md](ARCHITECTURE_en.md).

### Key Features

- **Face analysis** with MediaPipe Face Mesh to extract key points around the eyes, mouth, and iris
- **Eye Aspect Ratio (EAR)** for eye-closure and drowsiness detection
- **Mouth Aspect Ratio (MAR)** for yawn detection
- **Head Pose Estimation** for head angle estimation
- **Gaze Estimation** to assess gaze direction
- Distinction between a natural blink and prolonged eye closure (based on duration and consecutive frame count)
- **Object detection with YOLO** (including mobile phones), using frame skipping to reduce computational cost
- Simple **Face Tracking** based on bounding boxes and IoU to preserve driver identity across consecutive frames
- **Real-time dashboard** showing Driver ID, Risk Score, EAR, MAR, Gaze, Head Pose, blink count, phone-usage status, distraction status, FPS, and latency
- Logging of key events (Drowsiness, Yawning, Distraction, Mobile Phone Usage) to a CSV file for post-run analysis
- A combined **Risk Score** that produces driver states: SAFE, WARNING, DROWSY, DISTRACTED, and CRITICAL

The system is designed to reduce input resolution, use a lightweight YOLO model, and run object detection periodically, allowing it to run in real time even on standard hardware.

### Full Project Description

> This project is a prototype of a Driver Monitoring System that I designed and implemented to analyze driver alertness, attention, and behavior in real time.
>
> The system uses **Python, OpenCV, MediaPipe Face Mesh, and YOLO** to process incoming camera video in real time and extract several behavioral driver indicators simultaneously.
>
> For face analysis, **MediaPipe Face Mesh** is used to extract key facial points around the eyes, mouth, and iris. Based on these landmarks, indicators such as **Eye Aspect Ratio (EAR)** for eye-closure detection, **Mouth Aspect Ratio (MAR)** for yawn detection, **Head Pose Estimation** for head angle estimation, and **Gaze Estimation** for assessing gaze direction are computed.
>
> For drowsiness detection, a single frame of closed eyes is not used as the criterion; instead, **the duration of eye closure and the number of consecutive frames** are examined, to distinguish between a natural blink and prolonged eye closure. The number of blinks and the closure duration are also logged throughout the system's runtime.
>
> Alongside face analysis, a **YOLO** model has been added to detect driving-related objects, including mobile phones. To reduce computational cost, YOLO does not run on every frame; it runs at a defined **frame-skipping / inference interval**, and its results are reused for the frames in between. This approach reduces computational load and increases the system's processing rate.
>
> To improve system stability, a simple **Face Tracking** mechanism has also been implemented, which uses bounding boxes and IoU to track driver identity across consecutive frames.
>
> Finally, the system's output is displayed as a **real-time dashboard**, which includes Driver ID, driver state, Risk Score, EAR, MAR, Gaze, head-pose angle, blink count, eye-closure duration, phone-usage status, distraction status, FPS, and latency.
>
> In addition to the real-time display, important events such as **Drowsiness, Yawning, Distraction, and Mobile Phone Usage** are logged to a CSV file, enabling post-test performance analysis as well.
>
> For final decision-making, a **Risk Score** has been designed that estimates the driver's risk level based on a combination of drowsiness indicators, prolonged eye closure, distraction, yawning, and phone usage, and produces states such as **SAFE, WARNING, DROWSY, DISTRACTED, and CRITICAL**.
>
> One of the main design goals was to preserve **real-time processing** capability. For this reason, in addition to reducing input resolution and using a lightweight YOLO model, object detection is run periodically, and MediaPipe is used for face analysis. As a result, the system can run in real time even on ordinary hardware, and it reports FPS and latency in real time as well.
>
> This project is currently a **Proof of Concept for a DMS**, and its purpose is to demonstrate the complete pipeline of a Driver Monitoring system — from image acquisition to feature extraction, behavior analysis, decision-making, and event logging. In future versions, capabilities such as **more accurate gaze estimation, detection of different driver states, a dedicated drowsiness model, more advanced tracking, temporal deep learning, and optimization for embedded/automotive hardware** could be added.

---

## Installation and Usage

### Requirements

- Python 3.10.x

### Installation

It is recommended to create an isolated virtual environment for this project:

```bash
python -m venv dms_env
```

Activate the virtual environment:

**Windows**
```bash
dms_env\Scripts\activate
```

**Linux / macOS**
```bash
source dms_env/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Running the Project

Navigate to the project root directory and run:

```bash
python main.py
```

Once launched, the application automatically performs the following steps:

1. Initializes system configuration
2. Sets up the camera and receives real-time frames
3. Loads the YOLO model for object detection
4. Runs face processing using MediaPipe Face Mesh
5. Extracts facial features (EAR, MAR, Head Pose, Gaze)
6. Analyzes driver behavior (drowsiness, yawning, distraction, phone usage)
7. Computes the risk level and overall driver state
8. Displays the real-time dashboard
9. Logs events and system performance data

### Controls

| Key | Action |
|---|---|
| `Q` | Quit the application |
| `R` | Start or stop video output recording |

### Configuration

To change parameters such as thresholds, camera settings, or model parameters, edit the following file (no changes to core logic required):

```text
config/settings.py
```

---

## Outputs

| File | Description |
|---|---|
| `results/dms_demo.mp4` | Recorded output video of the system |
| `results/driver_events.csv` | Log of driver events |
| `results/performance_metrics.csv` | Report of FPS, latency, and module processing times |

---

## Requirements

The project was developed and tested with Python 3.10.x.

Main dependencies:

| Package | Version |
|---|---|
| NumPy | 1.26.4 |
| OpenCV | 4.10.0.84 |
| MediaPipe | 0.10.21 |
| Ultralytics YOLO | 8.0.190 |
| psutil | 5.9.5 |

```bash
pip install -r requirements.txt
```

---

## Project Structure

```
DMS_Project/
│
├── main.py
├── requirements.txt
│
├── config/
│   └── settings.py
│
├── perception/
│   ├── landmarks.py
│   └── face_geometry.py
│
├── tracking/
│   └── face_tracker.py
│
├── detection/
│   └── phone_detector.py
│
├── monitoring/
│   └── risk_engine.py
│
├── visualization/
│   └── dashboard.py
│
├── logger/
│   ├── event_logger.py
│   └── performance_logger.py
│
├── utils/
│   └── face_bbox.py
│
├── models/
│   └── yolov8n.pt
│
└── results/
    ├── driver_events.csv
    ├── performance_metrics.csv
    └── dms_demo.mp4
```

Architecture details and the role of each module are described in [ARCHITECTURE.md](ARCHITECTURE_en.md).

---

## Technical Highlights

- Real-time video processing pipeline
- Modular Computer Vision architecture
- Face landmark based behavioral analysis
- Temporal filtering for reducing false alarms
- Lightweight YOLO inference scheduling
- Runtime performance monitoring
- Event logging system

## Future Work

- Advanced gaze estimation
- Driver-specific calibration
- Embedded deployment
- TensorRT optimization
- Multi-person tracking
- Additional behavior detection

## Status

This project is currently a **Proof of Concept for a DMS**. The implemented Risk Score is an initial model intended for validation and simulation purposes, and is not claimed to be a definitive, industrial-grade risk assessment model. A production version would require calibration with real driver data and diverse scenarios.
