# Import the libraries
import cv2 as cv
# Configure camera
cap = cv.VideoCapture(0)
# These commands set the codec and create the record video object
fourcc = cv.VideoWriter_fourcc(*'XVID')
# Indicate the avi file to be created
out = cv.VideoWriter('saida.avi', fourcc, 20.0, (640, 480))
# This command defines a variable condition
rec = False
# Here a loop will start
while True:
# read the image
    ret, frame = cap.read()
    if not ret:
        break
# show the image
    cv.imshow('frame', frame)
# Set keyboard recognition
    key = cv.waitKey(1) & 0xff
# save the image when the "s" key is pressed
    if key == ord('s'):
       rec = True
# When the condition is changed to real, start the recording
    if rec:
        out.write(frame)
# close the program by pressing the "q" key
    if key == ord('q'):
        break
# release the objects and close the window
cap.release()
out.release()
cv.destroyAllWindows()
