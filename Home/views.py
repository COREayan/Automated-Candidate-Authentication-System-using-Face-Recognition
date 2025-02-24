from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
# from numpy import imag, roll
from django.contrib import messages
from Home.models import Student
import cv2
from Home.forms import UserImageForm
from .models import Student  
import cv2
import numpy as np
import face_recognition

# Create your views here.
def index(request):
    if request.method == "POST":
        user = request.POST.get('username')
        pw = request.POST.get('password')
        if user=="admin" and pw=="user1234":
            return HttpResponseRedirect('/image_request')
        if user=="auth" and pw=="user1234":
            return render(request, 'liveimage.html')
    return render(request, 'index.html')
    # return HttpResponse("this is homepage")



def liveimage(request):
    return render(request, 'liveimage.html')


def cp(request):
    #return HttpResponse(gen(VideoCamera())
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    k = cv2.waitKey(1)
   
    img_name ="static/images/test.png"
    cv2.imwrite(img_name, frame)
 
    cv2.destroyAllWindows()
    cam.release()
    return render(request, 'retake.html')


def rt(request):
    return render(request, 'liveimage.html')


def image_request(request):  
    submitted = False
    if request.method == "POST":
        form = UserImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/image_request?submitted=True')
    else: 
        form = UserImageForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'image_form.html', {'form': form, 'submitted': submitted})  

def auth(request):
    if request.method == "POST":
        roll = request.POST.get('user_id')
    
        imgElon = face_recognition.load_image_file('static/images/test.png')
        imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)

        imgTest = face_recognition.load_image_file('media/images/'+str(roll)+'.png')
        imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

        # faceLoc = face_recognition.face_locations(imgElon)[0]
        encodeElon = face_recognition.face_encodings(imgElon)[0]
        # cv2.rectangle(imgElon, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)

        # faceLocTest = face_recognition.face_locations(imgTest)[0]
        encodeTest = face_recognition.face_encodings(imgTest)[0]
        # cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)

        results = face_recognition.compare_faces([encodeElon], encodeTest)
        # faceDis = face_recognition.face_distance([encodeElon], encodeTest)
        image = face_recognition.load_image_file('static/images/test.png')
        face_locations = face_recognition.face_locations(image)
        f1={'Name':'Real-time Image','Eyes':face_locations[0][0],'Nose':face_locations[0][1],'Mouth':face_locations[0][2],'Chin':face_locations[0][3]}

        image1 = face_recognition.load_image_file('media/images/'+str(roll)+'.png')
        face_locations1 = face_recognition.face_locations(image1)
        f2={'Name':'Pre-saved Image','Eyes':face_locations1[0][0],'Nose':face_locations1[0][1],'Mouth':face_locations1[0][2],'Chin':face_locations1[0][3]}
        print('Matched') if results[0] else print('Not matched')
        print('Face parameters locations of first image:',f1)
        print('Face parameters locations of test image:',f2)
        cv2.putText(imgTest, f'{results}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

        if results[0] :
            return render(request, 'access.html')
        else:
            return render(request, 'denied.html')
    