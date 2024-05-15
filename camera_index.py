import cv2

# Function to find a working camera index
def find_camera_index():
    for index in range(10):  # Try up to 10 different camera indices
        cap = cv2.VideoCapture(index)
        if cap.isOpened():
            print(f"Camera index {index} is available.")
            cap.release()
            return index
    return None

camera_index = find_camera_index()
if camera_index is None:
    print("No camera found.")
else:
    print(f"Using camera index: {camera_index}")
