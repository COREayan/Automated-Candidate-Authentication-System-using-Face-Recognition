# 🧠 Automated Candidate Authentication System using Face Recognition

A Django-based web application that enables secure and automated candidate registration and authentication using face recognition. This project aims to streamline the identity verification process for exams, interviews, or any environment requiring controlled access.

---

## 🔍 Features

- 📷 **Live Image Capture**: Capture candidate's photo in real-time using webcam.
- 📝 **Candidate Registration**: Register candidates with name and roll number along with their facial image.
- 🧠 **Face Recognition Authentication**: Authenticate a person by comparing live camera feed with registered facial data.
- 🗃️ **Admin Dashboard**: View all registered candidates from the admin panel.
- 🔐 **Secure Image Upload**: Validates file format and handles media storage safely.

---

## 🛠️ Tech Stack

- **Backend**: Django 5.1.2
- **Frontend**: HTML, CSS (custom styling)
- **Face Recognition**: `face_recognition` Python library (built on dlib)
- **Database**: SQLite (default) or extendable to PostgreSQL
- **Media Handling**: Django Media Files

---

## 🚀 Getting Started

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/yourusername/automated-face-authentication.git
cd automated-face-authentication

2️⃣ Create and Activate Virtual Environment
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Run the Server
python manage.py runserver

Visit http://127.0.0.1:8000/ to get started!

📷 Face Recognition Setup
The system uses the face_recognition library to encode and compare faces. Make sure your webcam is connected. You may need to install additional system packages for dlib.

pip install face_recognition opencv-python

✅ Usage
Go to /image-request/ to register a candidate.

Visit /authenticate/ to authenticate a candidate using live face recognition.

Admin can access the database through /admin/.

🧑‍💻 Author
Ayanabha Pramanik

📍 From West Bengal, India
🔗 LinkedIn
📧 ayanabha@example.com