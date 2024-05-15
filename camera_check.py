import cv2

# Try to open the default camera (index 0)
cap = cv2.VideoCapture(0)

if cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Camera', frame)
        cv2.waitKey(0)  # Wait for a key press to close the window
        cv2.destroyAllWindows()
    else:
        print("Failed to capture image")
else:
    print("Cannot open camera")
    
cap.release()