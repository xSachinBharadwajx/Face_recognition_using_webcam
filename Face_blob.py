import cv2
import sys
import os


class Face_blob:
    video_capture=cv2.VideoCapture(0)
    def __init__(self):
        self.faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.video_capture = cv2.VideoCapture(0)
    
    def startwebcam(self,train=False,Name=None):

        if train:
            for i in range(1000):
                # Capture frame-by-frame
                ret, frame = self.video_capture.read()

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                faces = self.faceCascade.detectMultiScale(
                    gray,
                    scaleFactor=1.1,
                    minNeighbors=5,
                    minSize=(30, 30),
                    flags=cv2.CASCADE_SCALE_IMAGE
                )

                # Draw a rectangle around the facesqq
                for (x, y, w, h) in faces:
                    #cv2.rectangle(frame, (x+10, y+10), (x+w+10, y+h+10), (0, 255, 0), 2)
                    if train and Name is not None:
                        crop=frame[y-50:y+h+10,x-20:x+w]
                        if not os.path.exists('Training/{}'.format(Name)):
                            os.mkdir('Training/{}'.format(Name))
                        if not os.path.exists('Validation/{}'.format(Name)):
                            os.mkdir('Validation/{}'.format(Name))
                        T_file=str("Training/{}/{}_{}.png".format(Name,Name,str(i)))
                        V_file=str("Validation/{}/{}_{}.png".format(Name,Name,str(i)))
                        print("collecting {}/1000".format(str(i)))
                        if i<900:
                            cv2.imwrite(T_file,crop)
                        else:
                            cv2.imwrite(V_file,crop)
            cv2.imshow('Video', frame)
                

        else:
            while True:
                 # Capture frame-by-frame
                ret, frame = self.video_capture.read()

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                faces = self.faceCascade.detectMultiScale(
                    gray,
                    scaleFactor=1.1,
                    minNeighbors=5,
                    minSize=(30, 30),
                    flags=cv2.CASCADE_SCALE_IMAGE
                )

                # Draw a rectangle around the facesqq
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x-20, y-50), (x+w, y+h+10), (0, 255, 0), 2)
                    
                # Display the resulting frame
                cv2.imshow('Video', frame)


                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            


    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()