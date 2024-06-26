# import cv2
# import urllib.request
# import numpy as np
#
# url = 'http://192.168.0.8/cam-lo.jpg'
#
# while (True):
#     img = urllib.request.urlopen(url)
#     img_np = np.array(bytearray(img.read()), dtype=np.uint8)
#     frame = cv2.imdecode(img_np,-1)
#     cv2.imshow("img", frame)
#     if cv2.waitKey(10) & 0xFF == ord('q'):
#         frame.release()
#         cv2.destroyAllWindows()
#         break

# import cv2
# import urllib.request
# import numpy as np
#
# url = 'http://192.168.0.8/cam-lo.jpg'
#
# while (True):
#     img = urllib.request.urlopen(url)
#     img_np = np.array(bytearray(img.read()), dtype=np.uint8)
#     frame = cv2.imdecode(img_np, -1)
#     # convert frame(urllib) to img(opencv)
#     ret, buffer = cv2.imencode('.jpg', frame)
#     img = buffer.tobytes()
#
#     cv2.imshow("img",cv2.imdecode(np.frombuffer(img, dtype=np.uint8),-1))
#     if cv2.waitKey(10) & 0xFF == ord('q'):
#         frame.release()
#         cv2.destroyAllWindows()
#         break

# import cv2
# import urllib.request
# import numpy as np
#
# url = 'http://192.168.0.8/cam-lo.jpg'
#
# while (True):
#     resp = urllib.request.urlopen(url)
#     img = np.asarray(bytearray(resp.read()), dtype="uint8")
#     img = cv2.imdecode(img, cv2.IMREAD_COLOR)
#     cv2.imshow('image', img)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cv2.destroyAllWindows()

url = 'http://192.168.0.8/cam-lo.jpg'
import urllib.request
import cv2
import numpy as np
import os

recognizer = cv2.face.LBPHFaceRecognizer.create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

font = cv2.FONT_HERSHEY_SIMPLEX

id = 0

names = ['Minh Nhat','Duy Tin','Anh Quan','Ngoc Anh']

# cam = cv2.VideoCapture(0)
# cam.set(3, 640)
# cam.set(4, 480)
#
minW = 0.1 * 640
minH = 0.1 * 480

while True:
    # ret, img = cam.read()
    resp = urllib.request.urlopen(url)
    img = np.asarray(bytearray(resp.read()), dtype="uint8")
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH)),
    )
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

        if (confidence < 100):
            id = names[id]
        else:
            id = "Unknown"

        confidence = " {0}%".format(round(100 - confidence))

        cv2.putText(img, str(id), (x + 10, y), font, 1, (0, 0, 255), 2)
        # cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

    cv2.imshow('Nhan dien khuon mat', img)

    k = cv2.waitKey(10) & 0xff
    if (k == 27):
        break
print("Thoat")
# cam.release()
cv2.destroyAllWindows()
