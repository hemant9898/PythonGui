import numpy as np
import cv2
import pickle
TRAINNER="D:\\trainner.yml" #PATH FOR TRAINNER FILE

def recog():
    recognizer=cv2.face.LBPHFaceRecognizer_create()
    face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    # Define the codec and create VideoWriter object
    recognizer.read(TRAINNER)
    labels ={"person_name": 1}

    with open("labels.pickle",'rb') as f:
        og_labels=pickle.load(f)
        labels={v:k for k,v in og_labels.items()}

    average = []
    average.append(-1)
    cap = cv2.VideoCapture(0)
    time_count = 0
    while(time_count < 300):

        ret, frame = cap.read()
        if ret == True:
            frame = cv2.flip(frame,1)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.5, 5)
            # write the flipped frame

            for x, y, w, h in faces:
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]

                id_, conf = recognizer.predict(roi_gray)
                if conf>= 56:
                    print(id_)
                    average.append(id_)
                    print(labels[id_])
                    font= cv2.FONT_HERSHEY_SIMPLEX
                    name=labels[id_]
                    cv2.putText(frame,name,(x,y),font,1,(255,255,255),2)
            

                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.imshow('frame',frame)
            time_count+=1
        

            if cv2.waitKey(1) & 0xFF == ord('q') :

                break
        else:
            break

    # Release everything if job is finished
    print(time_count)
    print (average)
    cap.release()


    def most_frequent(list):
        counter = 0
        num = list[0]

        for i in list:
            curr_frequency = list.count(i)
            if (curr_frequency > counter):
                counter = curr_frequency
                num = i
        return num
    most =  most_frequent(average)
    m = average.count(most)
    
    
    if(most==-1):
        return("no face",0)
    else:
        print(labels[most])
        print(len(average))
        accu=(m/(len(average)-1)*100)
        print(" Accuracy percentage = ",accu,"%" )
        print("final/////////////////////\n")
        print('label=',labels[most],"accuracy",accu)
        return(labels[most],accu)
    
    cv2.destroyAllWindows()

#recog()