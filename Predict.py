import cv2
from keras.models import load_model
from keras_preprocessing import image
import numpy as np

img_width, img_height = 224, 224
model = load_model('sach_pandit_binu.h5')

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video_capture = cv2.VideoCapture(0)


while True:
    # Capture frame-by-frame
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # Draw a rectangle around the facesqq
        for (x, y, w, h) in faces:
             cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
             resized = cv2.resize(frame[y:y+h,x:x+h], (img_width,img_height))
             resized = resized.astype("float") / 255.0
             resized = np.expand_dims(resized, axis=0)
             pred = model.predict(resized)[0]
             if pred.max() > 0.6:
                if pred.argmax() ==0:
                    res='Binu'
                if pred.argmax() ==1:
                    res='Pandit'
                if pred.argmax() ==2:
                    res='Sachin'
                cv2.putText(frame,str(res)+'-'+str(pred.max()),(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 255, 0),2)
             

        # Display the resulting frame
        cv2.imshow('Video', frame)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()