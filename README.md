# 🎨 Virtual Paint using Hand Tracking (Python & OpenCV)

A real-time **Virtual Paint Application** built using **Python**, **OpenCV**, and **Hand Tracking**.  
This project allows users to draw on the screen using **hand gestures** captured through a webcam — no mouse or touchscreen required.

---

## 📌 Features

- 🖐️ Real-time **hand detection and tracking**
- ✏️ Draw using **index finger**
- 🎨 Multiple color selection (Purple, Blue, Green)
- 🧽 **Eraser mode** using gesture
- 📷 Live webcam feed with overlay canvas
- 🚀 Smooth and responsive drawing experience

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Libraries Used:**
  - OpenCV
  - NumPy
  - MediaPipe (via HandTrackingModule)
  - Time
  - OS

---

## 📂 Project Structure
Virtual-Paint/
│
├── Header/
│ └── (UI header images for color selection)
│
├── HandTrackingModule.py
├── virtual_paint.py
├── README.md
└── requirements.txt

### Workflow

1. Webcam captures live video feed
2. Hand landmarks detected using HandTrackingModule
3. Finger positions are analyzed
4. Based on gestures:
   - Select color
   - Draw on canvas
   - Erase drawings
5. Canvas is merged with live feed using bitwise operations

