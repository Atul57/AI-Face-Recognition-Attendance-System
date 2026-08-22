# 🤖 AI Face Recognition Attendance System

An **AI-powered face recognition attendance system** built with Python. The system uses a webcam to detect and recognize faces and automatically records attendance in a **MySQL database**.

## ✨ Features

* 📷 Real-time face detection using webcam
* 🧠 AI-based face recognition using **DeepFace**
* 👤 Automatic identification of registered users
* 📝 Automatic attendance recording
* 🗄️ MySQL database integration
* ⚡ Real-time image processing with OpenCV

## 🛠️ Tech Stack

* **Python**
* **DeepFace**
* **OpenCV**
* **NumPy**
* **MySQL**

## 📁 Project Workflow

```text
Webcam
   ↓
OpenCV
   ↓
Face Detection
   ↓
DeepFace Recognition
   ↓
Identify Person
   ↓
MySQL Database
   ↓
Attendance Recorded
```

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Atul57/AI-Face-Recognition-Attendance-System.git
cd AI-Face-Recognition-Attendance-System
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

The project uses:

```text
deepface
opencv-python
numpy
mysql-connector-python
```

## 🗄️ Database Setup

1. Install and start **MySQL**.
2. Create a database for the attendance system.
3. Configure your MySQL connection details in the Python application.
4. Create the required tables for storing user and attendance information.

Example:

```sql
CREATE DATABASE attendance_system;
```

## 🚀 How It Works

1. Start the application.
2. The webcam captures the user's face.
3. OpenCV processes the camera frames.
4. DeepFace compares the detected face with registered faces.
5. When a person is recognized, their attendance is recorded in MySQL.

## 📊 Future Improvements

* Add a web-based admin dashboard
* Add login/authentication for administrators
* Generate daily/monthly attendance reports
* Add email notifications
* Improve recognition accuracy
* Add anti-spoofing/liveness detection

## ⚠️ Note

This project is intended for educational and demonstration purposes. Face recognition accuracy can depend on lighting, camera quality, facial angle, and the quality of registered images.

## 👨‍💻 Author

**Atul Kumar**

GitHub: [Atul57](https://github.com/Atul57?utm_source=chatgpt.com)
