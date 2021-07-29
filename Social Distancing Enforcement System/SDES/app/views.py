from django.http.response import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from app.camera import FaceDetect
from django.shortcuts import render

import cv2, base64

# Create your views here.

class gen():
    def __init__(self, request):
        self.session = request
        self.camera = FaceDetect(self.session.session)

    def frame(self):
        while True:
            try:
                frame = self.camera.get_frame()
                frame = frame.tobytes()
                yield(b'--frame\r\n'
                    b'Content_type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
            except:
                self.__init__(self.session)

data = ""
def read(request):
    global data
    return render(request, 'app/html.html')

@csrf_exempt
def Unread(request):
    global data
    if request.method == 'POST':
        try:
            data = request.POST.get("content").split(",")[1]
            with open(f"app/data/{request.session.session_key}-clientImage.png", 'wb') as f:
                f.write(base64.b64decode(data))
        except:
            return HttpResponse(f"{data}")
    return HttpResponse(f"{data}")

def feed_cam(request):
    x = gen(request)
    return StreamingHttpResponse(x.frame(), content_type='multipart/x-mixed-replace; boundary=frame')
