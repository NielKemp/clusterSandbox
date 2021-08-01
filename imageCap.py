import numpy as np #import numpy cause images are matrices.. 
import cv2 #importing CV library, add with pip install opencv-python


#cap = cv2.VideoCapture(0) #initialize videocapture object, 0 is webcam?!?!
cap = cv2.VideoCapture(2) #initialize videocapture object, 0 is webcam?!?!
#cap.set(cv2.CAP_PROP_FRAME_WIDTH,2000)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT,2000)

currentWidth = cap.get(3)
currentHeight = cap.get(4)

imageCount = 0
savePath = 'C:/Users/Niel/Kaggle/gestureRecognition/data/'
imageMainName = 'gestureUp'


while(True):
    #capture frame-by-frame
    ret, frame = cap.read() #read a frame from cap object
    
    frame = cv2.flip(frame,1)
    
    #draw a rectangle on the frame topleft is (150,150), bottom right is (450,450), colour is (255,0,255) size is 3   
    cv2.rectangle(frame, (150, 150), (450, 450), (255, 0, 255), 3)
        
   
    
    keyPress = cv2.waitKey(1) #readKeyboardAction
    
    #if press 's' then do this
    if keyPress == ord('s'):
        
        regionToCapture = frame[150:450, 150:450]
        #save_path = os.path.join(label_name, '{}.jpg'.format(image_name + 1))
        fullPath =  ('data/{}{}.jpg'.format(imageMainName,imageCount))
        cv2.imwrite(fullPath, regionToCapture)
        imageCount += 1
        
        
    #add text to frame that is displayed
    cv2.putText(frame, "Frame subject and press 's' to capture image", 
                (20,30),cv2.FONT_HERSHEY_SIMPLEX , 0.6, (255,255,255), 1, cv2.LINE_AA)
    cv2.putText(frame, "Press 'q' to quit", 
                (20,60),cv2.FONT_HERSHEY_SIMPLEX , 0.6, (255,255,255), 1, cv2.LINE_AA)
    cv2.putText(frame, "Image count: {}".format(imageCount),
                (20,90),cv2.FONT_HERSHEY_SIMPLEX , 0.6, (255,255,255), 1, cv2.LINE_AA)    
    cv2.putText(frame, "Current resolution {} x {}".format(currentWidth, currentHeight),
                (475,20),cv2.FONT_HERSHEY_SIMPLEX , 0.3, (150,0,150), 1, cv2.LINE_AA)
    
    
    #display resulting frame
    cv2.imshow('frame', frame)
    
    
    if keyPress == ord('q'): #press 'q' on the keyboard to quit videoplaying
        break

        
#closes camera, kills video frame window
cap.release()
cv2.destroyAllWindows()
