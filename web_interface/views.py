from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.conf import settings

from web_interface.models import Student
from web_interface.forms import StudentSignupForm

import cv2
import face_recognition
import numpy as np
import os


def index(request):
    """
    Render login form and handle simple role-based redirection.
    """
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == "admin" and password == "user1234":
            return HttpResponseRedirect('/image_request')
        elif username == "auth" and password == "user1234":
            return render(request, 'liveimage.html')
        
        messages.error(request, "Invalid credentials")
    
    return render(request, 'index.html')


def live_image(request):
    """
    Load camera preview template.
    """
    return render(request, 'liveimage.html')


def capture_image(request):
    """
    Capture a single image from the webcam and save to static folder.
    """
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        return render(request, 'error.html', {'message': 'Camera could not be opened.'})

    ret, frame = cam.read()
    if not ret:
        cam.release()
        return render(request, 'error.html', {'message': 'Failed to capture image from camera.'})

    img_dir = os.path.join(settings.BASE_DIR, 'web_interface', 'static', 'live_images')
    os.makedirs(img_dir, exist_ok=True)

    img_path = os.path.join(img_dir, 'test.png')
    cv2.imwrite(img_path, frame)

    cam.release()
    cv2.destroyAllWindows()

    return render(request, 'retake.html')


def retake_image(request):
    """
    Load camera preview template, for retaking image
    """
    return render(request, 'liveimage.html')


def image_request(request):
    """
    Handle image upload using Django forms.
    """
    submitted = request.GET.get('submitted', False)

    if request.method == "POST":
        form = StudentSignupForm(request.POST, request.FILES)
        if form.is_valid():
            print('form is saving')
            form.save()
            print('Form is valid - saving and redirecting')
            return HttpResponseRedirect('/image_request?submitted=True')
        else:
            print('Form is not valid')
            print(form.errors)
        
    else:
        form = StudentSignupForm()

    return render(request, 'image_form.html', {'form': form, 'submitted': submitted})


def authenticate_user(request):
    """
    Authenticate user by comparing a real-time image with a pre-saved image.
    """
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        try:
            # Load and encode real-time image
            img_live = face_recognition.load_image_file('static/images/test.png')
            img_live_rgb = cv2.cvtColor(img_live, cv2.COLOR_BGR2RGB)
            encode_live = face_recognition.face_encodings(img_live_rgb)[0]

            # Load and encode stored image
            img_stored_path = f'media/images/{user_id}.png'
            img_stored = face_recognition.load_image_file(img_stored_path)
            img_stored_rgb = cv2.cvtColor(img_stored, cv2.COLOR_BGR2RGB)
            encode_stored = face_recognition.face_encodings(img_stored_rgb)[0]

            # Compare encodings
            result = face_recognition.compare_faces([encode_live], encode_stored)[0]

            # Optional: print face feature positions
            face_live = face_recognition.face_locations(img_live)[0]
            face_stored = face_recognition.face_locations(img_stored)[0]

            print('Matched' if result else 'Not matched')
            print('Live face:', face_live)
            print('Stored face:', face_stored)

            if result:
                return render(request, 'access.html')
            else:
                return render(request, 'denied.html')

        except IndexError:
            return render(request, 'error.html', {'message': 'Face not detected in one or both images.'})
        except FileNotFoundError:
            return render(request, 'error.html', {'message': f'File not found for roll number: {user_id}'})
    
    return render(request, 'liveimage.html')