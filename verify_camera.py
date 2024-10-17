import cv2

# Open the camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open the camera.")
else:
    print("Camera opened successfully.")

# Release the camera
cap.release()

