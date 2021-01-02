from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from recognition.camera import FaceDetect
# Create your views here.

def index(request):
	return render(request, 'recognition/index.html')


class gen():

	def __init__(self):
		self.camera = FaceDetect()
		# while True:
		# 	pass# self.frame, self.distance = self.camera.get_frame()

	def frame(self):
		while True:
			frame = self.camera.get_frame()
			frame = frame.tobytes()
			yield(b'--frame\r\n'
				b'Content_type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
			# yield(b'--distance\r\n'
			# 	b'Content_type: text/plain\r\n\r\n' + self.data() + b'\r\n\r\n')
		# self.winner = self.list.sort(key = lambda x: x[1])
		# print(f"[INFO] {self.list}")
		# print(f"[INFO] {sorted(self.list,key = lambda x: x[1])}")

x = gen()

def facecam_feed(request):
	frame = x.frame()
	return StreamingHttpResponse(frame,
					content_type='multipart/x-mixed-replace; boundary=frame')

# def facecam_data(request):
# 	x = gen()
# 	return StreamingHttpResponse(x.frame(),
# 					content_type='multipart/x-mixed-replace; boundary=distance')
