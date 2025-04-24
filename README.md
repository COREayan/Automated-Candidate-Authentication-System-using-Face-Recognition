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
<pre lang="bash"><code>git clone https://github.com/COREayan/Automated-Candidate-Authentication-System-using-Face-Recognition.git
cd Automated-Candidate-Authentication-System-using-Face-Recognition</code></pre>

### 2️⃣ Create and Activate Virtual Environment
<pre lang="bash"><code>python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows</code></pre>

### 3️⃣ Install Dependencies
<pre lang="bash"><code>pip install -r requirements.txt</code></pre>

### 4️⃣ Apply Migrations
<pre lang="bash"><code>python manage.py makemigrations
python manage.py migrate</code></pre>

### 5️⃣ Run the Server
<pre lang="bash"><code>python manage.py runserver</code></pre>

Visit http://127.0.0.1:8000/ to get started!

![image](https://github.com/user-attachments/assets/7a218c0b-b49c-4ffc-a623-e82360251537) 

if logged in as admin
![image](https://github.com/user-attachments/assets/bf4cd40e-385b-4508-8166-68c035c893b3) 

after successfully filling the form 
![image](https://github.com/user-attachments/assets/effa67fd-5d14-4b12-9c50-9c66a76686f6)



if logged in as authenticator 
![image](https://github.com/user-attachments/assets/b16ad00f-0754-4ae0-a24e-6d1a94d688ea)




📷 Face Recognition Setup
The system uses the face_recognition library to encode and compare faces. Make sure your webcam is connected. You may need to install additional system packages for dlib.

<pre lang="bash"><code>pip install face_recognition opencv-python</code></pre>

✅ Usage
Go to /image-request/ to register a candidate.

Visit /authenticate/ to authenticate a candidate using live face recognition.

Admin can access the database through /admin/.

🧑‍💻 Author
Ayanabha Pramanik

📍 From West Bengal, India
🔗 LinkedIn
📧 ayanabha.pramanik.ee@gmail.com
